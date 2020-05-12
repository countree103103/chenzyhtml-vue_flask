from config import ormSqlite


class userModel(ormSqlite.Model):
    __tablename__ = "users"
    id = ormSqlite.Column(
        ormSqlite.Integer, primary_key=True, autoincrement=True)
    user_name = ormSqlite.Column(ormSqlite.String(16), unique=True)
    user_password = ormSqlite.Column(ormSqlite.String(16))
    register_time = ormSqlite.Column(ormSqlite.String(30))
    last_login = ormSqlite.Column(ormSqlite.String(30))

    def __init__(self, user_name, user_password, register_time):
        self.user_name = user_name
        self.user_password = user_password
        self.register_time = register_time
        self.last_login = None

    def __repr__(self):
        return "<users {} {} {} {} {}>".format(self.id, self.user_name, self.user_password, self.register_time, self.last_login)
