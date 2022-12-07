import paho.mqtt.subscribe as subscribe
import json
import websocket
from sympy import *
import math
from datetime import datetime
import base64

#websocket connection
ws = websocket.WebSocket()
ws.connect("ws://192.168.2.222:3333")

dictData = {}
output_x = 0.0
output_y = 0.0

# getting message data: sound id, time, lat, lng
def get_coordinate(m):
    payload = m.payload
    content = json.loads(payload)

    # get coordinates
    if("uplink_message" in content):
        uplink_message = content["uplink_message"]
        
        if("frm_payload" in uplink_message):
            id = content["end_device_ids"]["device_id"]
            lat = content["uplink_message"]["rx_metadata"][0]["location"]["latitude"] #float
            lng = content["uplink_message"]["rx_metadata"][0]["location"]["longitude"] #float
            time = content["uplink_message"]["frm_payload"][0:16] #datetime now in str
            
            if id not in dictData:
                time_rm = base64.b64decode(time)
                time_rm = time_rm.decode('ascii')

                time_obj = datetime.strptime(time_rm,'%M:%S.%f')
                dictData[id]=time_obj
                
                return (id,time_obj,lat,lng)
            else:
                return 'already in'

# getting area
def get_area(t0,t1,t2):
    if (t0<t1 and t1<t2):
        area = 1
    elif (t1<t0 and t0<t2):
        area = 2
    elif (t1<t2 and t2<t0):
        area = 3
    elif (t2<t1 and t1<t0):
        area = 4
    elif (t2<t0 and t0<t1):
        area = 5
    elif (t0<t2 and t2<t1):
        area = 6
    else:
        area = 0
    return (area)

# localization
def localization(r, m, n, t0, t1, t2, area, theta):
    x = Symbol('x')
    y = Symbol('y')

    #input: r, m, n, t0, t1, t2 (it will be received from the sensors)
    #location of three sensors :(x0, y0), (x1, y1), (x2, y2)
    # ==> (m-r/float(2), n+r/sqrt(3)), (m+r/float(2), n+r/sqrt(3)), (m, n-2*r/sqrt(3))
    # 2r: the distance between two sensors
    #(m,n): the center of the triangle(made with sensors)
    #t1, t2, t3: TDOA between sensors
    #v: the velocity of sound (34.3cm/ms)

    v =  34.3 # cm/ms 

    # EQUATION
    # hyperbola between sensor0, sensor1
    # f(x,y) -> f(x,y-r/math.sqrt(3))
    eq_0 = Eq((4*(x**2)/float((v*t0)**2)-4*((y-r/math.sqrt(3))**2)/float(4*(r**2)-((v*t0)**2))),1)

    # hyperbola between sensor1, sensor2
    # [rotate movement] +60 degree (from origin, counterclockwise)
    # g(x,y) -> g((x-r/float(2))/float(2)+math.sqrt(3)*(y+r/(2*math.sqrt(3)))/float(2),-(x-r/float(2))*math.sqrt(3)/float(2)+(y+r/(2*math.sqrt(3)))/float(2))
    eq_1 = Eq((4*(((x-r/float(2))/float(2)+math.sqrt(3)*(y+r/(2*math.sqrt(3)))/float(2))**2)/float((v*t1)**2)-4*((-(x-r/float(2))*math.sqrt(3)/float(2)+(y+r/(2*math.sqrt(3)))/float(2))**2)/float(4*(r**2)-((v*t1)**2))),1)

    # hyperbola between sensor2, sensor0
    # [rotate movement] -60 degree (from origin, counterclockwise)
    # h(x,y) -> h(x/float(2)-math.sqrt(3)*y/float(2)+r/float(2),math(3)*x/float(2)+y/float(2)-r/float(2))
    eq_2 = Eq((4*(((x+r/float(2))/float(2)-math.sqrt(3)*(y+r/(2*math.sqrt(3)))/float(2))**2)/float((v*t2)**2)-4*((math.sqrt(3)*(x+r/float(2))/float(2)+(y+r/(2*math.sqrt(3)))/float(2))**2)/float(4*(r**2)-((v*t2)**2))),1)

    result_0 = solve([eq_0,eq_1])
    result_1 = solve([eq_1,eq_2])
    result_2 = solve([eq_0,eq_2])

    result = result_0+result_1+result_2

    print('result / len: '+str(len(result)))
    print(result)

    val = []

    for r in result:
        a = r[x]
        b = r[y]
        a = str(a)
        b = str(b)
        if ' ' in a:
            a = a[0:a.index(' ')]
        if ' ' in b:
            b = b[0:b.index(' ')]
        val.append({'x':float(a),'y':float(b)})

    print(len(val))
    print(val)

    # To get the intersections which is in the area that has possibility
    result = []
    for dic in val:
        a = dic['x']
        b = dic['y']
        

        if a<0 and b>-a/math.sqrt(3) and b>a/math.sqrt(3): #area 1 : t0 < t1 < t2
            if (area==1):
                result.append({'x':a,'y':b})
        elif a>0 and b>-a/math.sqrt(3) and b>a/math.sqrt(3): #area 2 : t1 < t0 < t2
            if (area==2):
                result.append({'x':a,'y':b})
        elif a>0 and b>-a/math.sqrt(3) and b<a/math.sqrt(3): #area 3 : t1 < t2 < t0
            if (area==3):
                result.append({'x':a,'y':b})
        elif a>0 and b<-a/math.sqrt(3) and b<a/math.sqrt(3): #area 4 : t1 < t2 < t0
            if (area==4):
                result.append({'x':a,'y':b})
        elif a<0 and b<-a/math.sqrt(3) and b<a/math.sqrt(3): #area 5 : t1 < t2 < t0 
            if (area==5):
                result.append({'x':a,'y':b})
        elif a<0 and b<-a/math.sqrt(3) and b>a/math.sqrt(3): #area 6 : t1 < t2 < t0 
            if (area==6):
                result.append({'x':a,'y':b})
        else:
            print('NO')

    # Middle of Intersections
    sum_x = 0.0
    sum_y = 0.0
    
    # Find the intersection result
    if len(result)!=0:
        print('result2 / len: '+str(len(result)))
        print(result)
        for r in result:
            sum_x += r['x']
            sum_y += r['y']
        output_x = sum_x/float(len(result))
        output_y = sum_y/float(len(result))
    
        print('output_x : ',output_x)
        print('output_y : ',output_y)
        
        result_x = output_x*math.cos(theta) - output_y*math.sin(theta)
        result_x = n+0.0000000902*result_x #Lng 
        result_y = output_x*math.sin(theta) + output_y*math.cos(theta)
        result_y = m+0.0000000902*result_y #Lat

        return (result_y, result_x)
    
    # No the intersection result 
    else:
        print('================ No Intersection ================')
        return (0.0, 0.0)


while True:
    # getting the value from the things network
    sub = subscribe.simple(topics=['#'], keepalive=5 ,hostname="nam1.cloud.thethings.network", port=1883, auth={'username':"esp32-sound",'password':"NNSXS.7ZNIO2YWWQ4IOZYXW75QSFRFATNRUXARKVAOCLQ.GSQBD2I3S2AFTDHBUDYFXENGJJSA7DFEOPR4BN3JKG4DCLH25WLA"}, msg_count=3)
    for element in sub:
        print(get_coordinate(element))
    
    # if the datas successfully get from three sensors 
    if "sound1" in dictData and "sound2" in dictData and "sound3" in dictData:
        print('========== Receive Done ==========')

        time0_obj = dictData.get('sound3')
        time1_obj = dictData.get('sound1')
        time2_obj = dictData.get('sound2')

        td0 = abs(time1_obj-time0_obj)
        td1 = abs(time1_obj-time2_obj)
        td2 = abs(time2_obj-time0_obj)

        print('td0')
        print(td0)
        print('td1')
        print(td1)
        print('td2')
        print(td2)
        
        # time difference 
        td0 = td0.total_seconds()  *10  
        td1 = td1.total_seconds()  *10
        td2 = td2.total_seconds()  *10

        print('diff_td0')
        print(td0)
        print('diff_td1')
        print(td1)
        print('diff_td2')
        print(td2)

        # if it get the right value of the right condition of hyperbola 
        if(td0<50 and td1<50 and td2<50):
            area = get_area(time0_obj,time1_obj,time2_obj) # get the area range 
            print('area is -> ',area)

            # input
            r = 152.4 # cm
            theta = 8 # Angle (radian) between origin coordinate plane and the experiment setting coordinate plane
            m = 40.42622175517373
            n = -86.90966878841449
            result = localization(r,m,n,td0,td1,td2,area,theta) #localization code returns (Lat, Lng)
            print(result)
            print(str(result[0])+","+str(result[1])) #Lat, Lng
            print("success")
            
            ws.send(str(result[0])+","+str(result[1])) # Sending Lat, Lng via web socket
        
    dictData.clear()
    sub.clear() 
    print("Over 1 Cycle")

ws. close()
