from . import app,db
from flask import render_template,flash, redirect, url_for, request
from auth.forms import LoginForm,RegistrationForm,EditProfileForm
from app.earnings.forms import EarningEntryForm
from flask_login import current_user, login_user,logout_user,login_required
from .models.Users_model import User
from .models.Person_model import Persons
from .models.Eartype_model import EarType
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime

'''


#This deocrator function will ensure that if page is served it must have authenticated users
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()



#This decorator function will implement index page
@app.route('/')
@app.route('/index')
def index():

    return render_template('welcome/index.html', title='Welcome to E2ISA Home')


#This decorator function witll implement login method
@app.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Login Name or Password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for('index'))
    return  render_template('auth/login.html',title='E2ISA Login Here',form=form)

#This decorator function will be for logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#This Decorator function is for creating user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(nickname=form.nickname.data, email=form.email.data,mob=int(form.mob.data))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form)


# This route decorator function will show user information and profile
@app.route('/user/<email>')
@login_required
def user(email):
    user = User.query.filter_by(email=email).first_or_404()
    return render_template('auth/user.html', user=user)


#This route decorator function will allow user to edit their profile
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.mob,current_user.nickname)
    if form.validate_on_submit():
        current_user.nickname = form.nickname.data
        current_user.mob = form.mob.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.nickname.data = current_user.nickname
        form.mob.data = current_user.mob
    return render_template('auth/editprofile.html',form=form)

@app.route('/earning/add_earn', methods=['GET', 'POST'])
@login_required
def earn_add():
    form = EarningEntryForm()
    form.Ear_per_name.choices = [(row.id,row.per_name) for row in Persons.query.all()]
    form .Ear_type_name.choices = [(row.id,row.EarType_name) for row in EarType.query.all()]
    return render_template('earning/earn_add.html',form=form)
'''