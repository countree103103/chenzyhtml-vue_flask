# -*- coding: utf-8 -*-
from config import ormSqlite


class lybModel(ormSqlite.Model):
    __tablename__ = "lyb"
    id = ormSqlite.Column(
        ormSqlite.Integer, primary_key=True, autoincrement=True)
    guest_name = ormSqlite.Column(ormSqlite.Text)
    guest_message = ormSqlite.Column(ormSqlite.Text)
    time = ormSqlite.Column(ormSqlite.Text)

    def __init__(self, guest_name, guest_message, time):
        self.guest_name = guest_name
        self.guest_message = guest_message
        self.time = time

    def __repr__(self):
        return "<lyb {} {} {} {}>".format(self.id, self.guest_name, self.guest_message, self.time)
