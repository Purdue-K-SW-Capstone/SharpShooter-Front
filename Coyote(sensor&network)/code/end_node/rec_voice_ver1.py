import sounddevice as sd
import time
import serial
from datetime import datetime

fs = 44100
second = 0.001
i = 0
# FILE_PATH = '/home/coyote/code'

ser = serial.Serial('/dev/ttyUSB_DEV1', 115200, timeout=1)
ser.reset_output_buffer()

while(True):
    arr_high =[]
    # FILE_NAME = 'REC_FILE'+str(i)
    record_voice = sd.rec( int(second*fs), samplerate=fs, channels=2 ) # per 0.001 sec
    sd.wait()
    
    #real code
    for arr in record_voice:
        if(arr[0]>0.057):
            output = datetime.now()
            output = output.strftime('%Y-%m-%d %H:%M:%S.%f')[14:26]
            print(output)
            output = output.encode('utf-8')
            ser.write(output)
            time.sleep(1)
            break
    
    '''
    for arr in record_voice:
        if(arr[0]>0.15):
            arr_high.append(arr[0])
            output = datetime.now().strftime("%M:%S.%f") # type: str
            print('type')
            print(type(output))
            print('output')
            print(output)
    print('arr_high: '+str(i))
    print(arr_high)
    #write(FILE_NAME+'.wav', fs, record_voice)
    #wav_file_path = FILE_PATH + FILE_NAME
    #playsound(wav_file_path + '.wav')
    i+=1
    '''

