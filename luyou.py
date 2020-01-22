# -*- coding: utf-8 -*
from flask import Blueprint,render_template,redirect,url_for,make_response,session,jsonify
from werkzeug.routing import BaseConverter
from flask import request
#from mongo import *
from sql import *
import time
from datetime import timedelta
import sys
import os
# from blog_ajax import *

if(sys.version_info.major == 2):
    reload(sys)
    sys.setdefaultencoding('utf-8')

#db=Mongo(host='localhost',db_name='sk')
dbsql=Sqlite("./db/db.db")

# 自定义正则转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        # 将接受的第1个参数当作匹配规则进行保存
        self.regex = args[0]

b_shouye=Blueprint('b_luyou',__name__,url_prefix='/')
@b_shouye.route('/<re("(index.html){0,1}"):empty>',methods=['GET','POST'])
def index(empty):
    return render_template('index.html')

@b_shouye.route('/register',methods=['GET','POST'])
def register():
    if request.method=="POST":
        salt=None
        r_time=time.asctime( time.localtime(time.time()) )
        r_name=request.form['register_name']
        r_password=request.form['register_password']
        last_login=r_time
        check=dbsql.find_one("users","user_name",r_name)
        if check is not None:
            return render_template('register.html',errormessage="该用户已存在，请尝试另外的用户名！")
        else:
            dbsql.insert_one("users",'NULL,"{}","{}","{}","{}"'.format(r_name,r_password,r_time,last_login))
            session.permanent = True
            session['user_name']=r_name
            return redirect('/index.html')
    else:
    	return render_template('register.html')

@b_shouye.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        l_name=request.form['login_name']
        l_password=request.form['login_password']
        check=dbsql.find_one("users","user_name",l_name)
        if check is None:
        	return render_template('login.html',errormessage="用户名或密码输入错误，请检查！\n")
        if check[1]==l_name and check[2]==l_password:
            dbsql.update_one("users","last_login",time.ctime(),"user_name",l_name)
            session.permanent = True
            session['user_name']=l_name
            return redirect('/index.html')
        else:
            return render_template("login.html",errormessage="用户名或密码输入错误，请检查！")
    else:
    	return render_template('login.html')

@b_shouye.route('/logout',methods=['GET','POST'])
def logout():
    try:
        session.pop('user_name')
        return redirect(request.args.get("backurl"))
    except:
        return redirect(request.args.get("backurl"))

@b_shouye.route('/gallery',methods=['GET','POST'])
def gallery():
    return render_template("gallery.html")

@b_shouye.route('/swiper',methods=['GET','POST'])
def swiper():
    return render_template("swiper.html")
#blog ajax接口
blog_ajax=Blueprint('blog_ajax',__name__,url_prefix='/')

@blog_ajax.route('/ajax/lyb',methods=['GET','POST'])
def lyb():
    lyb=dbsql.find_all("lyb") 
    oynn=os.listdir("./static/img/oynn")
    if request.method=="POST":
        g_name=request.form['guest_name']
        g_message=request.form['guest_message']
        g_time=time.asctime( time.localtime(time.time()) )
        dbsql.insert_one("lyb","NULL,'{}','{}','{}'".format(g_name,g_message,g_time))
        return redirect('/#message')
    else:
        return jsonify(lyb)

@blog_ajax.route('/ajax/oynn',methods=['GET','POST'])
def oynn():
    oynn=os.listdir("./static/img/oynn")
    return jsonify(oynn)
##
if __name__=="__main__":
    print(url_for('gallery'))
