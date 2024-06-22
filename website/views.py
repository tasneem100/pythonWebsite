from flask import Blueprint, render_template

views= Blueprint('views',__name__)

@views.route('/')
def home(): #whenever go to rout it will call this func
    return render_template("home.html")

@views.route('/')
def login(): #whenever go to rout it will call this func
    return render_template("login.html")
