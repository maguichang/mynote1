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
    DATABASE_URI = 'ip'
    DATABASE_NAME = 'kafkaTopic'
    DATABASE_PORT = 27017
    DATABASE_USER = 'admin'
    DATABASE_PASSWORD = 'admin'
    # mysql setup
    MYSQL_URI = 'ip'
    MYSQL_PORT = 3306
    MYSQL_USER = 'admin'
    MYSQL_PWD = 'admin'
    MYSQL_DB = 'ads_monitor'
    #mail setup
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USERNAME = '邮箱用户名'
    MAIL_PASSWORD = '邮箱密码'
    MAIL_SENDER = '发送邮箱'
    MAIL_RECIPIENTS = '接收邮箱'



class ProductionConfig(Config):
    DATABASE_URI = '10.0.7.37'
    DATABASE_NAME = 'mgc'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
