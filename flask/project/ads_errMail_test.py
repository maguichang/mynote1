# -*- coding: utf-8 -*-
# author:maguichang time:2018/9/14

from flask import Flask
from flask_script import Manager, Shell
from flask_mail import Mail, Message
from kafka import KafkaClient
from kafka import KafkaConsumer
import threading
import datetime
import time
import json
import os
import numpy as np
import pymysql
from Configlist import *
#
app = Flask(__name__)
# 导入配置文件信息
para = Config()
conn2 = pymysql.connect(
    # host = 'localhost',
    host = para.MYSQL_URI,
    port = para.MYSQL_PORT,
    user = para.MYSQL_USER,
    passwd = para.MYSQL_PWD,
    db = para.MYSQL_DB,
    charset = 'utf8'
)
cur = conn2.cursor()
app.config['MAIL_SERVER'] = para.MAIL_SERVER
app.config['MAIL_PORT'] = para.MAIL_PORT
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = para.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = para.MAIL_PASSWORD

mail = Mail(app)

msg = Message('errInfo', sender=para.MAIL_SENDER, recipients=[para.MAIL_RECIPIENTS])

consumer1=KafkaConsumer('ads-kafka-nmdb-1',group_id='consumer_errTest3',auto_offset_reset='latest',bootstrap_servers=['10.0.7.38:9092'])
consumer2=KafkaConsumer('ads-kafka-nmdb-2',group_id='consumer_errTest3',auto_offset_reset='latest',bootstrap_servers=['10.0.7.38:9092'])
consumer25=KafkaConsumer('ads-kafka-nmdb-25',group_id='consumer_errTest3',auto_offset_reset='latest',bootstrap_servers=['10.0.7.38:9092'])


def consumerFunc(consumer_id,fj_name):
    before_msg = "beforeinfo"
    for m in consumer_id:
        data = bytes.decode(m.value)
        start = data.find("main_task_system_date_time")
        end = start+53
        data2 = data[:start]+data[end:]
        data3 = data2.replace(":",'":').replace("{",'{"').replace(",",',"')
        data4 = json.loads(data3)
        t = data4["time"]
        # print(t)
        current_state = data4["current_state"]
        if current_state !=101 and current_state !=122:
            errTime = datetime.datetime.utcfromtimestamp(int(t) / 1000.0 + 28800).strftime('%Y-%m-%d %H:%M:%S.%f')
            list_dic ={"list1_id":data4["list1_id"],"list2_id":data4["list2_id"],"list3_id":data4["list3_id"],
             "list4_id":data4["list4_id"],"list5_id": data4["list5_id"],"list6_id":data4["list6_id"],
             "list7_id" :data4["list7_id"],"list8_id":data4["list8_id"],"list9_id":data4["list9_id"],
             "list10_id":data4["list10_id"],"list11_id":data4["list11_id"],"list12_id":data4["list12_id"],
             "list13_id":data4["list13_id"],"list14_id":data4["list14_id"],"list15_id":data4["list15_id"]}
            s = str(fj_name)
            # print(list_dic)
            # print(s)
            for k,v in list_dic.items():
                if v != 255:
                    sql = 'select id,errCode from listErr2 where id ='+str(v)
                    cur.execute(sql)
                    result1 = cur.fetchall()
                    result2 = np.array(result1)
                    s = s+'{"'+k+'" :'+str(result2[0])+"},"
                else:
                    pass
            # print(s)
            if "list" in s:
                msg.body = s
                if before_msg != msg.body:
                    with app.app_context():
                        before_msg = msg.body
                        msg.body = msg.body+errTime
                        mail.send(msg)
