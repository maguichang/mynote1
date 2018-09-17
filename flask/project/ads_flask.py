# -*- coding: utf-8 -*-
# author:maguichang time:2018/9/14

import pymongo
import datetime
import time
from flask import Flask,render_template,request,url_for
from flask import jsonify #json 转换
import json
from pandas import DataFrame
import pandas as pd
import threading
from flask_script import Manager, Shell
from flask_mail import Mail, Message
from kafka import KafkaClient
from kafka import KafkaConsumer
import numpy as np
import pymysql

from ads_errMail_test import *
from Configlist import *


app = Flask(__name__)
# 引用配置类
# MONGO
app.config.from_object(Config)
# 数据库地址
DATABASE_URI = app.config.get('DATABASE_URI')
# 数据库名称
DATABASE_NAME = app.config.get('DATABASE_NAME')
# 数据库端口
DATABASE_PORT = app.config.get('DATABASE_PORT')
# 数据库用户名
DATABASE_USER = app.config.get('DATABASE_USER')
# 数据库密码
DATABASE_PASSWORD = app.config.get('DATABASE_PASSWORD')

conn = pymongo.MongoClient(DATABASE_URI, DATABASE_PORT)
db = conn[DATABASE_NAME]  # 连接kafkaads数据库，没有则自动创建
db.authenticate(DATABASE_USER, DATABASE_PASSWORD)

returnDataOne = {}
returnDataTwo = {}
returnDataThree = {}
returnDataFour = {}
returnDataFive = {}
returnDataSix = {}
returnDataSeven = {}
returnDataEight = {}
returnDataNine = {}
returnDataTen = {}

# 路由1，数据采集的可利用率
@app.route('/ads_analysis/<choose_table>/<b_time>/<e_time>/1',methods=['GET','POST'])
# @app.route('/1',methods=['GET'])
# def query_data1():
def query_data1(choose_table,b_time,e_time):
    # my_set = db["AdsAnalysis_25-1"]
    my_set = db[choose_table]
    query_data = my_set.find({'_id': {'$gte': str(b_time),'$lte': str(e_time)}}).sort('_id',1)
    # query_data = my_set.find({'_id': {'$gte': "2018-09-01",'$lte': "2018-09-09"}}).sort('_id',1)
    data = DataFrame(list(query_data))
    ads_date = list(data['_id'])
    ads_num = list(data['num'])
    if True:
        returnDataOne['status']=1
    else:
        returnDataOne['status']=0
    returnDataOne['datetime'] = ads_date
    returnDataOne['num'] = ads_num
#     # app.config['JSON_AS_ASCII'] = False
    return jsonify(returnDataOne)
    # return jsonify({"a":1})
    # print(returnDataOne)
@app.route('/ads_analysis/<choose_table>/<b_time>/<e_time>/show1')
def showOne(choose_table,b_time,e_time):
    return render_template('index_ads.html',choose_table=choose_table,b_time=b_time,e_time=e_time)
# 访问url  http://10.0.1.44:5004/ads_analysis/AdsAnalysis_25-1/2018-09-01/2018-09-09/show1

# 路由2，功率分布
@app.route('/ads_analysis/<choose_table>/<b_time>/<e_time>/2',methods=['GET','POST'])
def query_data2(choose_table,b_time,e_time):
    my_set = db[choose_table]
    field_dict2 = {'_id':0, 'time': 1, 'raw_wind_speed': 1, 'raw_active_power': 1}
    query_data = my_set.find({'time':{'$gt':int(b_time),'$lt':int(e_time)}}, field_dict2).sort('_id', -1)
    data = DataFrame(list(query_data))
    ads_wind_speed = list(data['raw_wind_speed'])
    ads_active_power = list(data['raw_active_power'])
    # 拟合数据
    power_normal = []
    speed_normal = [i / 10 for i in range(0, 200)]
    for i in speed_normal:
        if i <= 2:
            y_n = 0
            power_normal.append(y_n)
        elif 2 < i <= 14:
            y_n = -0.02127267 * i ** 3 + 1.41171128 * i ** 2 - 2.73958774 * i - 0.69314237
            power_normal.append(y_n)
        else:
            y_p = 200
            power_normal.append(y_p)
    if True:
        returnDataTwo['status'] = 1
    else:
        returnDataTwo['status'] = 0

    fitdata = [[i, j] for i, j in zip(speed_normal, power_normal)]
    active = [[i, j] for i, j in zip(ads_wind_speed, ads_active_power)]
    returnDataTwo['fit'] = fitdata
    returnDataTwo['active'] = active
    # app.config['JSON_AS_ASCII'] = False
    return jsonify(returnDataTwo)

@app.route('/ads_analysis/<choose_table>/<b_time>/<e_time>/show2')
def showTwo(choose_table,b_time,e_time):
    # return render_template('index_ads4_2.html',choose_table = choose_table,b_time = b_time,e_time = e_time)
    return render_template('index_ads2.html',choose_table = choose_table,b_time = b_time,e_time = e_time)
# 访问url http://10.0.1.44:5004/ads_analysis/ads-kafka-nmdb-2/1536740022289/1536740462289/show2

# 路由3，风速，偏航误差关系统计
@app.route('/ads_analysis/<choose_table>/<b_time>/<e_time>/3',methods=['GET','POST'])
def query_data3(choose_table,b_time,e_time):
# def query_data3():
    my_set = db[choose_table]
    filed_dic3 = [
                  # {"$limit": 1000},
                  {"$match":{"time":{"$gte":int(b_time),"$lte":int(e_time)}}},
                  # {"$match":{"time":{"$gte":int(1535424666083),"$lte":int(1535424796083)}}},
                  {"$group":
                      {
                          "_id": "$raw_wind_speed",
                          "raw_wind_misaligns": {"$push": "$raw_wind_misalign"}
                      }
                  },
                  {"$sort":{"_id":1}}
                  ]

    ori_data = my_set.aggregate(filed_dic3)
    data = DataFrame(list(ori_data))
    if True:
        returnDataThree['status'] = 1
    else:
        returnDataThree['status'] = 0
    returnDataThree["xdata"] = [round(i,1) for i in list(data["_id"])]
    returnDataThree["ydata"] = [sorted(i) for i in list(data["raw_wind_misaligns"])]#箱线图对数据列表排序
    # print(returnDataThree["xdata"])
    return jsonify(returnDataThree)

@app.route('/ads_analysis/<choose_table>/<b_time>/<e_time>/show3')
def showThree(choose_table,b_time,e_time):
    # return render_template('index_ads4_4.html',choose_table = choose_table,b_time = b_time,e_time = e_time)
    return render_template('index_ads3.html',choose_table = choose_table,b_time = b_time,e_time = e_time)
# 访问url http://10.0.1.44:5004/ads_analysis/ads-kafka-nmdb-2/1533806635555/1534906635555/show3

# 路由4，风速，风向关系统计
@app.route('/ads_analysis/<choose_table>/<b_time>/<e_time>/4',methods=['GET','POST'])
def query_data4(choose_table,b_time,e_time):
    my_set = db[choose_table]
    filed_dic4 = [
                  # {"$limit": 1000},
                  {"$match":{"time":{"$gte":int(b_time),"$lte":int(e_time)}}},
                  # {"$match":{"time":{"$gte":int(1535424666083),"$lte":int(1535424796083)}}},
                  {"$group":
                      {
                          "_id": "$raw_wind_speed",
                          "analog_input_wind_directions": {"$push": "$analog_input_wind_direction"}
                      }
                  },
                  {"$sort":{"_id":1}}
                  ]

    ori_data = my_set.aggregate(filed_dic4)
    data = DataFrame(list(ori_data))
    if True:
        returnDataFour['status'] = 1
    else:
        returnDataFour['status'] = 0
    returnDataFour["xdata"] = [round(i,1) for i in list(data["_id"])]
    returnDataFour["ydata"] = [sorted(i) for i in list(data["analog_input_wind_directions"])]#箱线图对数据列表排序
    # print(returnDataThree["xdata"])
    return jsonify(returnDataFour)

@app.route('/ads_analysis/<choose_table>/<b_time>/<e_time>/show4')
def showFour(choose_table,b_time,e_time):
    # return render_template('index_ads4_5.html',choose_table = choose_table,b_time = b_time,e_time = e_time)
    return render_template('index_ads4.html',choose_table = choose_table,b_time = b_time,e_time = e_time)
# 访问url http://10.0.1.44:5004/ads_analysis/ads-kafka-nmdb-2/1533806635555/1534906635555/show4


# 路由6，超速分析，统计每天n3超速的次数
@app.route('/ads_analysis/<choose_table>/<b_time>/<e_time>/6',methods=['GET','POST'])
def query_data6(choose_table,b_time,e_time):
    my_set = db[choose_table]
    query_data = my_set.find({'_id': {'$gte': str(b_time),'$lte': str(e_time)}}).sort('_id',1)
    data = DataFrame(list(query_data))
    ads_date = list(data['_id'])
    ads_num = list(data['num'])
    if True:
        returnDataSix['status']=1
    else:
        returnDataSix['status']=0
    returnDataSix["datetime"] = ads_date
    returnDataSix["num"] = ads_num
    # app.config['JSON_AS_ASCII'] = False
    return jsonify(returnDataSix)

@app.route('/ads_analysis/<choose_table>/<b_time>/<e_time>/show6')
def showSix(choose_table,b_time,e_time):
    return render_template('index_ads6.html',choose_table=choose_table,b_time=b_time,e_time=e_time)
# 访问 url http://10.0.1.44:5004/ads_analysis/AdsAnalysis_25-2/2018-09-01/2018-09-15/show6


if __name__ == '__main__':
    # excel.init_excel(app)
    t1 = threading.Thread(target=consumerFunc, args=(consumer1, "ads-kafka-nmdb-1"))
    t2 = threading.Thread(target=consumerFunc, args=(consumer2, "ads-kafka-nmdb-2"))
    t3 = threading.Thread(target=consumerFunc, args=(consumer25, "ads-kafka-nmdb-25"))
    t1.start()
    t2.start()
    t3.start()
    app.run(host='0.0.0.0',port=5004)