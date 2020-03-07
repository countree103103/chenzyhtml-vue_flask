# -*- coding: utf-8 -*
# from flask import Flask
#from blog_config import *
from blog_config import *
from luyou import *
# import sys

# if(sys.version_info.major == 2):
#     reload(sys)
#     sys.setdefaultencoding('utf-8')

app=Flask(__name__,static_url_path='')
app.url_map.converters['re']=RegexConverter
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key="16622877"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.register_blueprint(b_shouye)
app.register_blueprint(blog_ajax)
app.register_blueprint(blog_ht)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
# print(url_for('static',filename='css/bootstrap.css'))

