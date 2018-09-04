# -*- coding: utf-8 -*-
# author:maguichang time:2018/8/9

# python 操作mongodb数据库以及读取excel数据
# mongodb带用户名和密码
import pymongo
from pandas import DataFrame
import datetime
from itertools import groupby
import numpy as np
import matplotlib.pylab as plt
import math
import pandas as pd
field_dict = {"time":1,
              "wind_speed": 1,
              "active_power": 1,
              "wind_misalign":1,
              "_id":0}
# 连接数据库
conn = pymongo.MongoClient("myIP", 27017)
db_auth = conn.admin
db_auth.authenticate("root", "root")
db = conn['kafkaads']  # 连接kafkaads数据库，没有则自动创建
db.add_user('root','root')
my_set = db['ads-kafka-nmdb-2']
query_data = my_set.find({'wind_speed':{'$gte':3},"active_power":{'$gte':3}},field_dict)
returndata = DataFrame(list(query_data))
data = returndata.dropna()# 删除缺失值

wind_speed = np.array(data['wind_speed'])

active_power = np.array(data['active_power'])

# 读取标准功率数据
df = pd.read_excel('C:\\Users\\dell\\Desktop\\power.xlsx')
print(df)
print(df.columns)
w = np.array(df[u'wind '])
# p1 = np.array(df[u'power_0.985'])
p2 = map(lambda x : x/1000.0,np.array(df[u'power_1.225']))
plt.scatter(wind_speed,active_power,s=10)
# plt.plot(w,p1,'r-')
# plt.legend("power_0.985")
plt.plot(w,p2,'g-')
# plt.legend("power_1.225",)
plt.xlabel('wind_speed(m/s)')
plt.ylabel("power(kw)")
plt.title("windSpeed and Power Compare")
plt.show()
