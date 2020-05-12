# -*- coding: utf-8 -*-
from flask import Flask
from config import *
from luyou import *

autoEncoding()

# app初始化
app = Flask(__name__, static_url_path='')
app.url_map.converters['re'] = RegexConverter
app.register_blueprint(blogMain.blog_main)
app.register_blueprint(blogAjax.blog_ajax)
app.register_blueprint(blogAuth.blog_auth)
app.register_blueprint(blogTest.blog_test)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "52013140"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
# DB的连接词
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/data.db'
# 默认True，SQLAlchemy会记录下对象的变动，可以理解成写log
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == "__main__":
    ormSqlite.init_app(app)
    app.run(host="0.0.0.0", port=5000)

# print(url_for('static',filename='css/bootstrap.css'))
