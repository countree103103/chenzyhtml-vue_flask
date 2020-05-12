from config import *

blog_test = Blueprint('blog_test',__name__,url_prefix='/')

@blog_test.route('/test/create', methods=['GET', 'POST'])
def create():
    ormSqlite.drop_all()
    ormSqlite.create_all()

    return "creating..."


@blog_test.route('/test/set', methods=['GET', 'POST'])
def set():
    # admin = Test('admin', 'admin@example.com')
    # user = userModel("chenzy", "16622877", time.asctime(
    #     time.localtime(time.time())))
    # lyb_add = lybModel("guest", "hello world!", time.asctime(
    #     time.localtime(time.time())))
    # ormSqlite.session.add(admin)
    # ormSqlite.session.add(user)
    # ormSqlite.session.add(lyb_add)
    # guestes = [Test('guest1', 'guest1@example.com'),
    #            Test('guest2', 'guest2@example.com'),
    #            Test('guest3', 'guest3@example.com'),
    #            Test('guest4', 'guest4@example.com')]
    # ormSqlite.session.add_all(guestes)
    # ormSqlite.session.commit()
    try:
        user_add = userModel("chenzy", "16622877", time.asctime(
            time.localtime(time.time())))
        ormSqlite.session.add(user_add)
        ormSqlite.session.commit()
    except IntegrityError as e:
        return f"user exists...\n{e}"
    else:
        return "setting..."


@blog_test.route('/test/get/<search>', methods=['GET', 'POST'])
def get(search):
    result = Test.query.filter_by(name=search).first()
    result2 = userModel.query.filter_by(user_name=search).first()
    result3 = lybModel.query.filter_by(guest_name=search).first()
    if result3 is None or result2 is None or result is None:
        return "Not found."
    else:
        return "{},{}\n{}\n{}".format(result.name, result.email, result2.register_time, result3.guest_message)