# -*- coding: utf-8 -*-
import time
import sys
import os
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
