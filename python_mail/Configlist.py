# -*- coding: utf-8 -*-
# author:maguichang time:2018/9/10

"""
flask 引用的参数的配置的文件
config对象模块－－采用了 基于类继承的config结构，保存默认配置的Config类作为基类，其他类继承之。
"""

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = '10.0.7.37'
    DATABASE_NAME = 'ads_monitor'
    DATABASE_PORT = 3306
    DATABASE_USER = 'root'
    DATABASE_PASSWD = 'root'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USERNAME = 'mgc5320'
    MAIL_PASSWORD = 'mgc5320'
    MAIL_SENDER = 'mgc5320@163.com'
    MAIL_RECIPIENTS = 'juan.li@relectric.cn'



class ProductionConfig(Config):
    DATABASE_URI = '10.0.7.37'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    MAIL_RECIPIENTS = '1019233973@qq.com'
