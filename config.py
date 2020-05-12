# -*- coding: utf-8 -*-
import time
import sys
import os
import importlib
import pkgutil
from flask import Blueprint, render_template, redirect, url_for, make_response, session, jsonify, request
from werkzeug.routing import BaseConverter
#from mongo import *
from datetime import timedelta
from sql import Sqlite
from flask_sqlalchemy import SQLAlchemy

# 数据库初始化
# db=Mongo(host='localhost',db_name='sk')
# dbsql = Sqlite("./db/db.db")
ormSqlite = SQLAlchemy()

# 配置选项类


class appConfig():
    # app.jinja_env.auto_reload = True
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = "52013140"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    # DB的连接词
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/data.db'
    # 默认True，SQLAlchemy会记录下对象的变动，可以理解成写log
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 自定义正则转换器


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        # 将接受的第1个参数当作匹配规则进行保存
        self.regex = args[0]

# 自动判断python版本,解决兼容问题


def autoEncoding():
    if(sys.version_info.major == 2):
        reload(sys)
        sys.setdefaultencoding('utf-8')


def autoRegisterBlueprint(app, package, prefix=""):
    print("Starts auto registering Blueprints...")
    for _, name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module("." + name, package=prefix)
        for item in dir(module):
            item = getattr(module, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
                print(f"{name} registered..")
    print('-' * 20)
