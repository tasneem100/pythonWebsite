from flask import Blueprint, render_template, request, flash, redirect, url_for

from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth= Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login(): #whenever go to rout it will call this func
    if request.method == 'POST':
        email=request.form.get('email')
        passs=request.form.get('pass')

        #search in db by email return first one
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.passs, passs):
                flash('Logged Successfully',category='success')
                return redirect(url_for('views.home'))
            
            else:
                flash('Incorrect Password',category='error')
        else:
            flash('Email desn\'nt exist',category='error')

    return render_template("login.html", booan=True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/signup', methods=['GET','POST'])
def signup():

    if request.method == 'POST':
        email= request.form.get('email')
        Firstname=request.form.get('Firstname')
        pass1=request.form.get('pass1')
        pass2=request.form.get('pass2')
        user=User.query.filter_by(email=email).first()
        if user:
            flash('email already exist', category='error')
        elif len(email)< 4:
            flash('Enter valid email', category='error')
        elif len(Firstname)<2:
            flash('Enter valid username', category='error')
        elif pass1 != pass2:
            flash('passwords don\'t match', category='error')
        elif len(pass1) <7:
            flash('password must be at least 7 characters', category='error')
        else:
            new_user= User(email=email, fname=Firstname, passs=generate_password_hash( pass1, method='pbkdf2:sha256'))
            db.session.add(new_user)#add new user to db
            db.session.commit()
            
            flash('Account Created Successfully', category='success')
            #redirect user to homepage 
            return redirect(url_for('views.login'))
        
    return render_template("signup.html")
