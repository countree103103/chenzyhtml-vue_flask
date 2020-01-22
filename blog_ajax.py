from flask import Blueprint,jsonify
import os

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
        return redirect('/')
    else:
        return jsonify(lyb)

@blog_ajax.route('/ajax/oynn',methods=['GET','POST'])
def oynn():
    oynn=os.listdir("./static/img/oynn")
    return jsonify(oynn)