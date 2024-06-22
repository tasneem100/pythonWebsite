from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db= SQLAlchemy() #db object to add update on db
DB_name="database.db"

def create_app():
    app=Flask(__name__) #ini flask
    app.config['SECRET_KEY']='seckeyyyy' #secret key for cookie session

    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_name}'#where db located
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')


    from .models import User, Student
    
    create_db(app)


    return app


def create_db(app):
    #if not path.exists('website/' +DB_name):
        #db.create_all(app=app)

    if not path.exists('website/' + DB_name):
        with app.app_context():
            db.create_all()
            print('Created Database!')

