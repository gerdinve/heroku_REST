import sqlite3
from db import db

# This userModel is an API, not a rest APIself
# it exposes two endpoints, 2 methods, and are an interface for other
# parts of our programme to interact with the user thing (writing and retrieving
# from database)

class UserModel(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # It isn't needed to specify the id because it is  automatically generated
        # by db.Integer, primkary_key + True
        self.username=username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
