from config import *
from Models.users import userModel
from sqlalchemy.exc import IntegrityError

blog_auth = Blueprint('blog_auth', __name__, url_prefix='/')


@blog_auth.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == "POST":
            salt = None
            r_time = time.asctime(time.localtime(time.time()))
            r_name = request.form['register_name']
            r_password = request.form['register_password']
            last_login = r_time
            # check=dbsql.find_one("users","user_name",r_name)
            # dbsql.insert_one("users",'NULL,"{}","{}","{}","{}"'.format(r_name,r_password,r_time,last_login))
            ormSqlite.session.add(userModel(
                user_name=r_name, user_password=r_password, register_time=r_time))
            ormSqlite.session.commit()
            session.permanent = True
            session['user_name'] = r_name
            return redirect('/index.html')
        else:
            return render_template('register.html')
    except IntegrityError as e:
        return render_template('register.html', errormessage="该用户已存在，请尝试另外的用户名！")
    except Exception as e:
        return f"500 error:{e}"


@blog_auth.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == "POST":
            l_name = request.form['login_name']
            l_password = request.form['login_password']
            # check=dbsql.find_one("users","user_name",l_name)
            check = userModel.query.filter_by(user_name=l_name).first()
            if check is None:
                return render_template('login.html', errormessage="用户名或密码输入错误，请检查！\n")
            # if check[1]==l_name and check[2]==l_password:
            if check.user_name == l_name and check.user_password == l_password:
                # dbsql.update_one("users","last_login",time.ctime(),"user_name",l_name)
                userModel.query.filter_by(
                    user_name=l_name).first().last_login = time.ctime()
                ormSqlite.session.commit()
                session.permanent = True
                session['user_name'] = l_name
                return redirect('/index.html')
            else:
                return render_template("login.html", errormessage="用户名或密码输入错误，请检查！")
        else:
            return render_template('login.html')
    except Exception as e:
        return f"500 error:{e}"


@blog_auth.route('/logout', methods=['GET', 'POST'])
def logout():
    try:
        session.pop('user_name')
        return redirect(request.args.get("backurl"))
    except:
        return redirect(request.args.get("backurl"))
