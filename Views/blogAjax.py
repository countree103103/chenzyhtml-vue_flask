from config import *
from flask import Blueprint
from Models.lyb import lybModel
from Models.users import userModel
from sqlalchemy.exc import IntegrityError

# blog ajax接口
blog_ajax = Blueprint('blog_ajax', __name__, url_prefix='/')


@blog_ajax.route('/ajax/lyb', methods=['GET', 'POST'])
def lyb():
    try:
        # lyb = dbsql.find_all("lyb")
        lyb = lybModel.query.all()
        if request.method == "POST":
            g_name = request.form['guest_name']
            g_message = request.form['guest_message']
            g_time = time.asctime(time.localtime(time.time()))
            # dbsql.insert_one("lyb", "NULL,'{}','{}','{}'".format(
            #     g_name, g_message, g_time))
            ormSqlite.session.add(
                lybModel(guest_name=g_name, guest_message=g_message, time=g_time))
            ormSqlite.session.commit()
            return redirect('/#message')
        else:
            json_lyb = []
            for i in lyb:
                json_lyb.append(
                    {'guest_name': i.guest_name, 'guest_message': i.guest_message, 'time': i.time})
            # return jsonify(lyb)
            return jsonify(json_lyb)
    except Exception as e:
        return f"500 error:{e}"


@blog_ajax.route('/ajax/oynn', methods=['GET', 'POST'])
def oynn():
    oynn = os.listdir("./static/img/oynn")
    return jsonify(oynn)
