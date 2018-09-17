# -*- coding: utf-8 -*-
# author:maguichang time:2018/9/10

"""
flask 引用的参数的配置的文件
config对象模块－－采用了 基于类继承的config结构，保存默认配置的Config类作为基类，其他类继承之。
"""

class Config(object):
    DEBUG = False
    TESTING = False
    # mongo setup
    DATABASE_URI = '10.0.7.37'
    DATABASE_NAME = 'kafkaads'
    DATABASE_PORT = 27017
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = 'root'
    # mysql setup
    MYSQL_URI = '10.0.7.37'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PWD = 'root'
    MYSQL_DB = 'ads_monitor'
    #mail setup
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USERNAME = 'mgc5320'
    MAIL_PASSWORD = 'mgc5320'
    MAIL_SENDER = 'mgc5320@163.com'
    # MAIL_RECIPIENTS = 'juan.li@relectric.cn'
    MAIL_RECIPIENTS = '1019233973@qq.com'



class ProductionConfig(Config):
    DATABASE_URI = '10.0.7.37'
    DATABASE_NAME = 'mgc'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
