# -*- coding: utf-8 -*-
from flask import Flask
from config import *
# from luyou import *
import Views


autoEncoding()

# app初始化
app = Flask(__name__, static_url_path='')
app.config.from_object(appConfig)
app.url_map.converters['re'] = RegexConverter
autoRegisterBlueprint(app, Views, "Views")


if __name__ == "__main__":
    ormSqlite.init_app(app)
    app.run(host="0.0.0.0", port=5000)
    # print(url_for('static',filename='css/bootstrap.css'))
