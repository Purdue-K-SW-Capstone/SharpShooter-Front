import binascii

import pandas as pd
import numpy as np
import datetime
import json
import base64
import matplotlib.pyplot as plt


pd.options.mode.chained_assignment = None


# Returns integer from base64 encoded payload
def payload_to_int(payload):
    try:
        payload_byte = payload.encode('ascii')
        decoded_text = base64.decodebytes(payload_byte)
        return int(decoded_text[:1].hex(), 16)
    except binascii.Error:
        return -1


# Returns integer by calculating frame count, as payload is from 0 to 100 - total 101
def chirpstack_to_int(payload):
    while payload > 100:
        payload -= 101
    return payload


# Returns dataframe with selected columns from the full dataframe
# Columns: time, payload inside uplink_message.frm_payload,
# rssi, snr, consumed airtime inside uplink_message.consumed_airtime
def post_process(full_data):
    # From datas only find ApplicationUp packets
    application_up_data = full_data[full_data["@type"].str.contains("ApplicationUp", na=False)]

    # Select time, received time, frame counter, frame payload, consumed airtime, rssi, snr
    selected_data = application_up_data[["time", "received_at", "uplink_message.f_cnt", "uplink_message.frm_payload",
                                         "uplink_message.consumed_airtime"]]
    selected_data.loc[:, "rssi"] = np.nan
    selected_data.loc[:, "snr"] = np.nan

    # rssi and snr is in rx_metadata
    rx_metadata = application_up_data[["uplink_message.rx_metadata"]]
    rx_metadata.columns = ["rx_metadata"]

    # Process payload as integer
    selected_data['uplink_message.frm_payload'] = selected_data['uplink_message.frm_payload'].astype(str)
    selected_data['uplink_message.frm_payload'] = selected_data['uplink_message.frm_payload'].apply(payload_to_int)

    # Exception handling for empty rssi and snr inside rx_metadata
    for index, row in rx_metadata.iterrows():
        if row["rx_metadata"] is np.nan:
            continue
        try:
            selected_data.loc[index, "rssi"] = row["rx_metadata"][0]["rssi"]
        except KeyError:
            selected_data.loc[index, "rssi"] = np.nan
        try:
            selected_data.loc[index, "snr"] = row["rx_metadata"][0]["snr"]
        except KeyError:
            selected_data.loc[index, "snr"] = np.nan

    # Make string to numeric
    selected_data['uplink_message.consumed_airtime'] = selected_data['uplink_message.consumed_airtime'].str.replace(
        pat=r's', repl=r'', regex=True)
    selected_data['uplink_message.consumed_airtime'] = pd.to_numeric(selected_data['uplink_message.consumed_airtime'])
    # Change format into time series 2022-12-02T20:45:36.202684Z

    selected_data['time'] = pd.to_datetime(selected_data['time'], format='%Y-%m-%dT%H:%M:%S', errors='raise')

    return selected_data


# Returns full dataframe with normalized data columns
def data_loader(file=""):
    df = pd.read_json(file)

    # find time and data
    df = df[["time", "data"]]
    time_frame = df["time"]

    # normalize the data and concat with time to process further
    normalized_data = pd.json_normalize(df["data"])
    full_data = pd.concat([time_frame, normalized_data], axis=1)

    return post_process(full_data)


# Returns full dataframe with normalized data columns from the gateway file for selected end node
def data_loader_for_gateway(file='', eui='723F'):
    df = pd.read_json(file)

    time_frame = df['time']
    normalized_data = pd.json_normalize(df["data"])

    full_data = pd.concat([time_frame, normalized_data], axis=1)
    full_data = full_data[full_data['end_device_ids.dev_eui'].str.contains(eui, na=False)]

    return post_process(full_data)


# Returns dataframe with selected columns from the chirpstack json file
# Columns: time, payload inside uplink_message.frm_payload, rssi, snr
def data_loader_for_chirpstack(file=''):
    if file == '':
        file = 'chirp_stack_data.json'
    with open(file) as f:
        data = json.load(f)
    time = []
    rssi = []
    snr = []
    frame_count = []
    frame_payload = []
    airtime = []
    for i in range(len(data)):
        if data[i]['phyPayload']['mhdr']['mType'] == 'UnconfirmedDataUp':
            # time format is 2022-12-02T20:45:36.202684Z, save as datetime format from data[i]['rxInfo'][0]['time']
            time.append(pd.to_datetime(data[i]['rxInfo'][0]['time'], format='%Y-%m-%dT%H:%M:%S', errors='raise'))
            rssi.append(data[i]['rxInfo'][0]['rssi'])
            snr.append(data[i]['rxInfo'][0]['loRaSNR'])
            frame_count.append(data[i]['phyPayload']['macPayload']['fhdr']['fCnt'])
            try:
                frame_payload.append(chirpstack_to_int(data[i]['phyPayload']['macPayload']['fhdr']['fCnt']))
            except TypeError:
                frame_payload.append(-1)
            airtime.append(-1)
    data = {'time': time, 'rssi': rssi, 'snr': snr, 'fCnt': frame_count, 'uplink_message.frm_payload': frame_payload,
            'uplink_message.consumed_airtime': airtime}
    data = pd.DataFrame(data)
    return data


# Returns dataframe between the start_time and end_time
# start_time and end_time should be datetime format(ex: “2022-11-17 19:17:11.123+00:00”
def time_retrieval(target_dataframe, start_time, end_time):
    s = pd.to_datetime(start_time, format='%Y-%m-%d %H:%M:%S', errors='raise')
    e = pd.to_datetime(end_time, format='%Y-%m-%d %H:%M:%S', errors='raise')
    for i in target_dataframe.index:
        time_val = target_dataframe["time"][i]
        if s < time_val < e:
            continue
        else:
            target_dataframe = target_dataframe.drop([i])
    return target_dataframe


# Returns average time to send 100 packets for 1 End Node
def separate_100_packets(data_frame):
    end_times = {}
    start_times = {}

    checked = False
    exist = False
    count = 0
    packet_count = []
    # Because LoRa signal is NOT consistent, 0 or 1 can be skipped, also 99 and 100 can be skipped.
    # As timeline starts with 100, if 100 or 99 exists, exist = True and 1 or 0 should be counted as a start time
    # If not checked on 100, but 99 exists, checked = False, as checked decides finishing with 1 or 0
    # If not checked on 100, and also not checked on 99, the whole 100 packets will be skipped
    for i in data_frame.index:
        target = data_frame['uplink_message.frm_payload'][i]
        if target != -1:
            count += 1
        if target == 1 and checked and exist:
            start_times[data_frame['time'][i]] = 1
            packet_count.append(count)
            checked = False
            exist = False
        if target == 0 and not checked and exist:
            start_times[data_frame['time'][i]] = 0
            packet_count.append(count)
            exist = False
        if target == 100 and not exist:
            end_times[data_frame['time'][i]] = 100
            checked = True
            exist = True
            count = 0
        elif target == 100 and exist:
            end_times.popitem()
            end_times[data_frame['time'][i]] = 100
            checked = True
            exist = True
            count = 0
        if target == 99 and not checked and not exist:
            end_times[data_frame['time'][i]] = 99
            checked = False
            exist = True
            count = 0
        elif target == 99 and not checked and exist:
            end_times.popitem()
            end_times[data_frame['time'][i]] = 99
            checked = False
            exist = True
            count = 0

    # if end time is one more than start time, pop the last one (because it starts with end time)
    if len(end_times) > len(start_times):
        end_times.popitem()

    return start_times, end_times, packet_count


# Returns basic_statistics of the list
def basic_statistics(target_list):
    # remove np.nan
    target_list = [x for x in target_list if str(x) != 'nan']
    if len(target_list) == 0:
        return 0, 0, 0, 0
    else:
        average = np.mean(target_list)
        standard_deviation = np.std(target_list)
        min_, max_ = np.min(target_list), np.max(target_list)
        return average, standard_deviation, min_, max_


# Returns data_frame from the file name as String for automation
def dataframe_by_file(folder='', file_prefix='', device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    dataframes = {}

    for eui in device_eui_list:
        try:
            dataframes[eui] = data_loader(file='./jsonFiles/' + folder + '/' + file_prefix + eui + '.json')

        except FileNotFoundError:
            dataframes[eui] = data_loader_for_gateway(
                file='./jsonFiles/' + folder + '/' + file_prefix + 'fromGateway' + '.json',
                eui=eui.upper())

    return dataframes


# Returns result of normal data analysis for 1 End Node
def before_jamming_result(before_jamming_dataframe=None):
    return_dict = {}
    start_times, end_times, packet_count = separate_100_packets(before_jamming_dataframe)
    return_dict['jamming_start_times'] = start_times
    return_dict['jamming_end_times'] = end_times
    return_dict['packet_count'] = packet_count

    time_sum = datetime.timedelta()
    timed_dataframes = []
    for (end_time, _), (start_time, _) in zip(end_times.items(), start_times.items()):
        time_sum += end_time - start_time
        timed_dataframes.append(time_retrieval(before_jamming_dataframe, start_time, end_time))

    return_dict['average_time'] = time_sum / len(start_times)
    return_dict['average_packet_count'] = sum(packet_count) / len(packet_count)
    return_dict['timed_dataframes'] = timed_dataframes
    consumed_airtime_list = []
    rssi_list = []
    snr_list = []

    for df in timed_dataframes:
        consumed_airtime_list.append(df['uplink_message.consumed_airtime'])
        rssi_list.append(df['rssi'])
        snr_list.append(df['snr'])

    return_dict['consumed_airtime_list'] = consumed_airtime_list
    return_dict['rssi'] = rssi_list
    return_dict['snr'] = snr_list

    return return_dict


# Returns number of successfully sent packets for 1 End Node
def count_packet(data_frame):
    count = 0
    for i in data_frame.index:
        target = data_frame['uplink_message.frm_payload'][i]
        if target != -1:
            count += 1
    return count


# Returns result of jamming data analysis for 1 End Node
def after_jamming_result(before_jamming_rs=None, after_jamming_dataframe=None, start_time="", end_time=""):
    return_dict = {}

    after_jamming_dataframe = time_retrieval(after_jamming_dataframe, start_time, end_time)

    s = pd.to_datetime(start_time, format='%Y-%m-%d %H:%M:%S', errors='raise')
    e = pd.to_datetime(end_time, format='%Y-%m-%d %H:%M:%S', errors='raise')

    return_dict['data_frame'] = after_jamming_dataframe
    return_dict['packet_count'] = count_packet(after_jamming_dataframe)
    # how many packets should be sent for e - s minutes before before_jamming
    return_dict['assumed_pdr'] = return_dict['packet_count'] / ((e - s) * 100 / (before_jamming_rs['average_time']))
    return_dict['jamming_effectiveness'] = 1 - (return_dict['assumed_pdr']
                                                / (np.mean(before_jamming_rs['average_packet_count']) / 100))
    return_dict['consumed_airtime'] = after_jamming_dataframe['uplink_message.consumed_airtime']
    return_dict['rssi'] = after_jamming_dataframe['rssi']
    return_dict['snr'] = after_jamming_dataframe['snr']

    return return_dict


# Returns analysis of one cycle of jamming as before and after result
def jamming_info_one_cycle(df_before=None, df_after=None, device_eui_list=None, start_time='', end_time=''):
    if device_eui_list is None:
        device_eui_list = []
    before_jamming = {}
    for eui in device_eui_list:
        before_jamming[eui] = before_jamming_result(before_jamming_dataframe=df_before[eui])

    after_jamming = {}

    for eui in device_eui_list:
        after_jamming[eui] = after_jamming_result(before_jamming[eui], df_after[eui], start_time, end_time)

    return before_jamming, after_jamming


# Prints before jamming results as CLI
def before_print_average_time(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    print('Device\t Average time\t\t\t\t Packet count\t Mean')
    for eui in device_eui_list:
        print(eui, '\t', jamming_result[eui]['average_time'], '\t', jamming_result[eui]['packet_count'], '\t',
              np.mean(jamming_result[eui]['average_packet_count']))


# Prints information of snr before jamming
def before_print_rssi(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    print('Device\t Average RSSI\t\t Standard Deviation\t\t Min\t\t Max')
    for eui in device_eui_list:
        rssi_list = [item for sublist in jamming_result[eui]['rssi'] for item in sublist]
        average_, standard_dev_, min_, max_ = basic_statistics(rssi_list)
        print(eui + '\t {:03.6f}'.format(average_), '\t\t {:.6f}'.format(standard_dev_),
              '\t\t\t\t {:03.0f}'.format(min_), '\t\t {:03.0f}'.format(max_))


# Prints information of snr before jamming
def before_print_snr(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    print('Device\t Average SNR\t\t Standard Deviation\t\t Min\t\t Max')
    for eui in device_eui_list:
        snr_list = [item for sublist in jamming_result[eui]['snr'] for item in sublist]
        average_, standard_dev_, min_, max_ = basic_statistics(snr_list)
        print(eui + '\t {:03.6f}'.format(average_), '\t\t\t {:.6f}'.format(standard_dev_),
              '\t\t\t\t {:03.0f}'.format(min_), '\t\t {:03.0f}'.format(max_))


# Prints after jamming results as CLI
def after_print_effectiveness(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    print('Device\t Packets\t Assumed PDR\t Jamming Effectiveness\t')
    for eui in device_eui_list:
        if jamming_result[eui]['packet_count'] > 9:
            print(eui, '\t', jamming_result[eui]['packet_count'],
                  '\t\t {:.6f}'.format(jamming_result[eui]['assumed_pdr']),
                  '\t\t {:.6f}'.format(jamming_result[eui]['jamming_effectiveness']))
        else:
            print(eui, '\t', jamming_result[eui]['packet_count'],
                  '\t\t\t {:.6f}'.format(jamming_result[eui]['assumed_pdr']),
                  '\t\t {:.6f}'.format(jamming_result[eui]['jamming_effectiveness']))


# Prints information of snr after jamming
def after_print_rssi(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    print('Device\t Average RSSI\t\t Standard Deviation\t\t Min\t\t Max')
    for eui in device_eui_list:
        rssi_list = jamming_result[eui]['rssi']
        average_, standard_dev_, min_, max_ = basic_statistics(rssi_list)
        print(eui + '\t {:03.6f}'.format(average_), '\t\t {:.6f}'.format(standard_dev_),
              '\t\t\t\t {:03.0f}'.format(min_), '\t\t {:03.0f}'.format(max_))


# Prints information of snr before jamming
def after_print_snr(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    print('Device\t Average SNR\t\t Standard Deviation\t\t Min\t\t Max')
    for eui in device_eui_list:
        snr_list = jamming_result[eui]['snr']
        average_, standard_dev_, min_, max_ = basic_statistics(snr_list)
        print(eui + '\t {:03.6f}'.format(average_), '\t\t\t {:.6f}'.format(standard_dev_),
              '\t\t\t\t {:03.0f}'.format(min_), '\t\t {:03.0f}'.format(max_))


# Plots bar graph of packet count
def after_plot_packet_count(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    packet_count_list = []
    for eui in device_eui_list:
        packet_count_list.append(jamming_result[eui]['packet_count'])

    plt.bar(device_eui_list, packet_count_list)
    plt.title('Packet Count')
    plt.xlabel('Device EUI')
    plt.ylabel('Packet Count')
    plt.show()


# Plots bar graph of assumed PDR
def after_plot_assumed_pdr(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    assumed_pdr_list = []
    for eui in device_eui_list:
        assumed_pdr_list.append(jamming_result[eui]['assumed_pdr'])

    plt.bar(device_eui_list, assumed_pdr_list)
    plt.title('Assumed PDR')
    plt.xlabel('Device EUI')
    plt.ylabel('Assumed PDR')
    plt.show()


# Plots bar graph of jamming effectiveness
def after_plot_jamming_effectiveness(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    jamming_effectiveness_list = []
    for eui in device_eui_list:
        jamming_effectiveness_list.append(jamming_result[eui]['jamming_effectiveness'])

    plt.bar(device_eui_list, jamming_effectiveness_list)
    plt.title('Jamming Effectiveness')
    plt.xlabel('Device EUI')
    plt.ylabel('Jamming Effectiveness')
    plt.show()


# Plots O graph of packets timeline per device
def after_plot_packet_timeline(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    y_pos = np.arange(len(device_eui_list))
    plt.ylim(y_pos[0] - 1, y_pos[-1] + 1)
    plt.yticks(y_pos, device_eui_list)

    for eui in device_eui_list:
        plt.plot(jamming_result[eui]['data_frame']['time'], [eui] * len(jamming_result[eui]['data_frame']['time']), 'o')

    plt.title('Packets Timeline')
    plt.xlabel('Time')
    plt.ylabel('Device EUI')
    plt.legend(device_eui_list)
    plt.show()


# Plots O graph of rssi
def after_plot_rssi(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    for eui in device_eui_list:
        df = jamming_result[eui]['data_frame']
        plt.plot('time', 'rssi', 'o', data=df, label=eui)
    plt.title('RSSI')
    plt.xlabel('Time')
    plt.ylabel('RSSI')
    plt.legend()
    plt.show()


# Plots O graph of snr
def after_plot_snr(jamming_result=None, device_eui_list=None):
    if device_eui_list is None:
        device_eui_list = []
    for eui in device_eui_list:
        df = jamming_result[eui]['data_frame']
        plt.plot('time', 'snr', 'o', data=df, label=eui)
    plt.title('SNR')
    plt.xlabel('Time')
    plt.ylabel('SNR')
    plt.legend()
    plt.show()

# %%

# %%
