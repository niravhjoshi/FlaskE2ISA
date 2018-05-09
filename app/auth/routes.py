from app import app,db
from flask import render_template,flash, redirect, url_for, request
from forms import LoginForm,RegistrationForm,EditProfileForm
from app.earnings.forms import EarningEntryForm
from flask_login import current_user, login_user,logout_user,login_required
from app.models.Users_model import User
from app.models.Person_model import Persons
from app.models.Eartype_model import EarType
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from app.auth import bp

#This decorator function witll implement login method
@bp.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Login Name or Password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    return  render_template('auth/login.html',title='E2ISA Login Here',form=form)

#This decorator function will be for logout
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

#This Decorator function is for creating user
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(nickname=form.nickname.data,email=form.email.data,mob=int(form.mob.data))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)
