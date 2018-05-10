from app import app,db
from flask import render_template,flash, redirect, url_for, request
from app.auth.forms import LoginForm,RegistrationForm,EditProfileForm
from app.earnings.forms import EarningEntryForm
from flask_login import current_user, login_user,logout_user,login_required
from app.models.Users_model import User
from app.models.Person_model import Persons
from app.models.Eartype_model import EarType
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from app.main import bp


#This deocrator function will ensure that if page is served it must have authenticated users
@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()


#This decorator function will implement index page
@bp.route('/')
@bp.route('/index')
def index():
    return render_template('welcome/index.html', title='Welcome to E2ISA Home')

# This route decorator function will show user information and profile
@bp.route('/user/<email>')
@login_required
def user(email):
    user = User.query.filter_by(email=email).first_or_404()
    return render_template('auth/user.html', user=user)


#This route decorator function will allow user to edit their profile
@bp.route('/user/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.mob,current_user.nickname)
    if form.validate_on_submit():
        current_user.nickname = form.nickname.data
        current_user.mob = form.mob.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.nickname.data = current_user.nickname
        form.mob.data = current_user.mob
    return render_template('auth/editprofile.html',form=form)
