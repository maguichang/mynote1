# -*- coding: utf-8 -*-
# author:maguichang time:2018/8/7

# 多线程实现邮箱预警消息推送
from flask import Flask, request,jsonify,make_response
from flask_script import Manager, Shell
from flask_mail import Mail, Message
from kafka import KafkaClient
from kafka import KafkaConsumer
# from threading import Thread
import datetime
import time
import json
import os
import threading

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25 #网易邮箱端口
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'myname'# 邮箱用户名
app.config['MAIL_PASSWORD'] = 'mycode'# 邮箱授权码

mail = Mail(app)

msg = Message('标题', sender='xxxxxx@163.com', recipients=['xxxxxx@qq.com'])
# msg.body = 'raw_generator_speed error！' #发送消息内容
consumer=KafkaConsumer('ads-kafka-nmdb-2',group_id='consumer_errTest',auto_offset_reset='latest',bootstrap_servers=['ip:port'])
consumer2=KafkaConsumer('ads-kafka-nmdb-2',group_id='consumer_errTest',auto_offset_reset='latest',bootstrap_servers=['ip:port'])
def c1():
    # consumer = KafkaConsumer('ads-kafka-nmdb-2', group_id='consumer_errTest', auto_offset_reset='latest',
    #                          bootstrap_servers=['ip:port'])
    msg.body = 'raw_generator_speed error！'  # 发送消息内容
    for m in consumer:
        # returnData = {}
        data = bytes.decode(m.value)
        data_ = data.split(',')
        t = data_[0].split(':')[1]
        d = float(data_[10].split(':')[1])
        print(t, d,'c1')
        time.sleep(2)
        # 时间戳转换插差8个小时，加上28800为当前时间
        # returnData['time'] = datetime.datetime.utcfromtimestamp(int(t)/ 1000.0+28800).strftime('%Y-%m-%d %H:%M:%S.%f')
        errTime = datetime.datetime.utcfromtimestamp(int(t) / 1000.0 + 28800).strftime('%Y-%m-%d %H:%M:%S.%f')
        msg.body = msg.body + "time：" + errTime + ";" + "raw_generator_speed:" + str(d)
        if d > 37:
            with app.app_context():
                mail.send(msg)

def c2():
    # consumer2 = KafkaConsumer('ads-kafka-nmdb-2', group_id='consumer_errTest', auto_offset_reset='latest',
    #                           bootstrap_servers=['ip:port'])
    msg.body = 'raw_generator_speed error！'  # 发送消息内容
    for n in consumer2:
        # returnData = {}
        data = bytes.decode(n.value)
        data_ = data.split(',')
        t = data_[0].split(':')[1]
        d = float(data_[10].split(':')[1])
        print(t, d,'c2')
        # 时间戳转换插差8个小时，加上28800为当前时间
        # returnData['time'] = datetime.datetime.utcfromtimestamp(int(t)/ 1000.0+28800).strftime('%Y-%m-%d %H:%M:%S.%f')
        errTime = datetime.datetime.utcfromtimestamp(int(t) / 1000.0 + 28800).strftime('%Y-%m-%d %H:%M:%S.%f')
        msg.body = msg.body + "time：" + errTime + ";" + "raw_generator_speed:" + str(d)
        if d > 37:
            with app.app_context():
                mail.send(msg)

if __name__ == '__main__':
    # app.run()

    t1 = threading.Thread(target=c1)
    t2 = threading.Thread(target=c2)
    t2.start()
    t1.start()

    app.run()