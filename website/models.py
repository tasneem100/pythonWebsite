#create db model for users
#setup database

from . import db #from this package import db
from flask_login import UserMixin #model help to login

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    studentname=db.Column(db.String(150))
    grade=db.Column(db.Integer)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))


#inheret user from db model and usermixin
class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email= db.Column(db.String(150),unique=True)
    passs = db.Column(db.String(150))
    fname=db.Column(db.String(150))
    students=db.relationship('Student')#list


