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
from app.utils.oauth import OAuthSignIn
from app import LoginManager

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


lm =LoginManager(app)
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@bp.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('auth.user'))
    oauth= OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@bp.route('/callback/<provider>')
def oauth_callback(provider):
    if provider =='twitter':
        if not current_user.is_anonymous:
            return redirect(url_for('auth.user'))
        oauth = OAuthSignIn.get_provider(provider)
        social_id, username, email = oauth.callback()
        if social_id is None:
            flash('Authentication failed.')
            return redirect(url_for('/index'))
        user = User.query.filter_by(social_id=social_id).first()
        if not user:
            user = User(social_id=social_id, nickname=username, email=email)
            db.session.add(user)
            db.session.commit()
        login_user(user, True)
        return redirect(url_for('main.index'))
    else:
        if not current_user.is_anonymous:
            return redirect(url_for('auth.user'))
        oauth = OAuthSignIn.get_provider(provider)
        name, email = oauth.callback()
        if email is None:
            flash('Authentication failed.')
            return redirect(url_for('/index'))
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(nickname=name, email=email)
            db.session.add(user)
            db.session.commit()
        login_user(user, True)
        return redirect(url_for('main.index'))
