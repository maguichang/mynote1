# -*- coding: utf-8 -*-
# author:maguichang time:2018/9/10

"""
flask 引用的参数的配置的文件
config对象模块－－采用了 基于类继承的config结构，保存默认配置的Config类作为基类，其他类继承之。
"""

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'xx.xx.xx.xx'
    DATABASE_NAME = 'db'
    DATABASE_PORT = xx
    DATABASE_USER = 'xx'
    DATABASE_PASSWD = 'xx'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USERNAME = 'xxx'
    MAIL_PASSWORD = 'xxx'
    MAIL_SENDER = 'xxx'
    MAIL_RECIPIENTS = 'xxx'



class ProductionConfig(Config):
    DATABASE_URI = 'xx.xx.xx.xx'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    MAIL_RECIPIENTS = 'xxx@qq.com'
