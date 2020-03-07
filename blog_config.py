# -*- coding: utf-8 -*
from flask import Blueprint,render_template,redirect,url_for,make_response,session,jsonify,Flask,request
from werkzeug.routing import BaseConverter
# from flask import request
#from mongo import *
from sql import *
import time
from datetime import timedelta
import sys
import os

if(sys.version_info.major == 2):
    reload(sys)
    sys.setdefaultencoding('utf-8')

dbsql=Sqlite("./db/db.db")
#db=Mongo(host='localhost',db_name='sk')
# dbsql=Sqlite("./db/db.db")

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        # 将接受的第1个参数当作匹配规则进行保存
        self.regex = args[0]
