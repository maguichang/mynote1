# -*- coding: utf-8 -*-
# author:maguichang time:2018/5/24

# mqtt发布数据测试ok
import paho.mqtt.publish as publish
import time
import random

HOST = "10.0.1.60"
# HOST = "localhost"
PORT = 1883
# PORT = 61613
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode("utf-8"))

if __name__ == '__main__':
    client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    for i in range(1000):
        for j in range(6):
        # msg_dic = {"a_voltage": round(random.uniform(10, 20), 2), "a_current": round(random.uniform(10, 20), 2),
        #            "b_voltage": round(random.uniform(10, 20), 2),"b_current": round(random.uniform(10, 20), 2)}
        # msg='{"SUMWATT": 18.89, "SUMVAR": 10.81, "SUMVA": 14.15}'
            msg={"SUMWATT": round(random.uniform(10, 20), 2), "SUMVAR": round(random.uniform(10, 20), 2),
                 "SUMVA": round(random.uniform(10, 20), 2),"AVRMS":round(random.uniform(10, 20), 2),
                 "AIRMS":round(random.uniform(10, 20), 2),"BVRMS":round(random.uniform(10, 20), 2),
                 "BIRMS":round(random.uniform(10, 20), 2),"CVRMS":round(random.uniform(10, 20), 2),
                 "CIRMS": round(random.uniform(10, 20), 2),"cosA":round(random.uniform(0, 1), 2),
                 "cosB": round(random.uniform(0, 1), 2),"cosC":round(random.uniform(0, 1), 2),
                 "f": round(random.uniform(0, 1), 2),"sequence":round(random.uniform(0, 1), 2),
                 "AVHR3": round(random.uniform(0,1 ), 2), "AVHR5": round(random.uniform(0, 1), 2),
                 "AVHR7": round(random.uniform(0, 1), 2), "AVHR9": round(random.uniform(0, 1), 2),
                 "AVHR11": round(random.uniform(0, 1), 2), "AVHR13": round(random.uniform(0, 1), 2),
                 "AVHR15": round(random.uniform(0, 1), 2),"AVUIh": round(random.uniform(0, 5), 2),
                 "BVHR3": round(random.uniform(0, 1), 2), "BVHR5": round(random.uniform(0, 1), 2),
                 "BVHR7": round(random.uniform(0, 1), 2), "BVHR9": round(random.uniform(0, 1), 2),
                 "BVHR11": round(random.uniform(0, 1), 2), "BVHR13": round(random.uniform(0, 1), 2),
                 "BVHR15": round(random.uniform(0, 1), 2), "BVUIh": round(random.uniform(0, 5), 2),
                 "CVHR3": round(random.uniform(0, 1), 2), "CVHR5": round(random.uniform(0, 1), 2),
                 "CVHR7": round(random.uniform(0, 1), 2), "CVHR9": round(random.uniform(0, 1), 2),
                 "CVHR11": round(random.uniform(0, 1), 2), "CVHR13": round(random.uniform(0, 1), 2),
                 "CVHR15": round(random.uniform(0, 1), 2), "CVUIh": round(random.uniform(0, 5), 2),
                 "AIHR3": round(random.uniform(0, 1), 2), "AIHR5": round(random.uniform(0, 1), 2),
                 "AIHR7": round(random.uniform(0, 1), 2), "AIHR9": round(random.uniform(0, 1), 2),
                 "AIHR11": round(random.uniform(0, 1), 2), "AIHR13": round(random.uniform(0, 1), 2),
                 "AIHR15": round(random.uniform(0, 1), 2), "AIUIh": round(random.uniform(0, 5), 2),
                 "BIHR3": round(random.uniform(0, 1), 2), "BIHR5": round(random.uniform(0, 1), 2),
                 "BIHR7": round(random.uniform(0, 1), 2), "BIHR9": round(random.uniform(0, 1), 2),
                 "BIHR11": round(random.uniform(0, 1), 2), "BIHR13": round(random.uniform(0, 1), 2),
                 "BIHR15": round(random.uniform(0, 1), 2), "BIUIh": round(random.uniform(0, 5), 2),
                 "CIHR3": round(random.uniform(0, 1), 2), "CIHR5": round(random.uniform(0, 1), 2),
                 "CIHR7": round(random.uniform(0, 1), 2), "CIHR9": round(random.uniform(0, 1), 2),
                 "CIHR11": round(random.uniform(0, 1), 2), "CIHR13": round(random.uniform(0, 1), 2),
                 "CIHR15": round(random.uniform(0, 1), 2), "CIUIh": round(random.uniform(0, 5), 2),
                 "AVTHD": round(random.uniform(0, 1), 2), "BVTHD": round(random.uniform(0, 1), 2),
                 "CVTHD": round(random.uniform(0, 1), 2), "AITHD": round(random.uniform(0, 1), 2),
                 "BITHD": round(random.uniform(0, 1), 2), "CITHD": round(random.uniform(0, 1), 2)
                 }
            msg['AVUIh']=j
            mymsg = str(msg)
            data = mymsg.replace("'", '"')
            # data = "'"+data+"'"
            #
            time.sleep(1)
            print(data)
            publish.single("home/garden/fountain", data, qos = 1,hostname=HOST,port=PORT, client_id=client_id)
            # publish.single("test/fj", data, qos = 1,hostname=HOST,port=PORT, client_id=client_id,auth = {'username':"admin", 'password':"password"})
            # publish.single("test/fj1", data, qos = 1,hostname=HOST,port=PORT, client_id=client_id,auth = {'username':"admin", 'password':"password"})
            # publish.single("test/fj2", data, qos = 1,hostname=HOST,port=PORT, client_id=client_id,auth = {'username':"admin", 'password':"password"})
        # publish.single("test", str(msg_dic), qos = 1,hostname=HOST,port=PORT, client_id=client_id,auth = {'username':"admin", 'password':"password"})
    # publish.single("test2", "你好 MQTT2", qos = 1,hostname=HOST,port=PORT, client_id=client_id,auth = {'username':"admin", 'password':"password"})