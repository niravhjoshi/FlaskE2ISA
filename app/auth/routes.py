from app import app, db
from flask import session, make_response,current_app, render_template, flash, redirect, url_for, request, jsonify, g, current_app
from forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models.Users_model import User
from flask_login import login_user, logout_user, current_user, login_required, UserMixin
from requests_oauthlib import OAuth2Session
from requests.exceptions import HTTPError
import json
from flask_httpauth import HTTPBasicAuth
from app.auth import bp
import requests
from flask.json import jsonify
from time import time


# This decorator function witll implement login method
@bp.route('/login', methods=['GET', 'POST'])
def login():
    #If we don't have session token or email session token then user needs to sign in
    if session.get('oauth_token') is None:
        print session.get('oauth_token')
        session.permanent = True
        client_id = current_app.config['OAUTH_CREDENTIALS_GOOGLE_ID']
        scope = current_app.config['SCOPE']
        redirect_uri = current_app.config['REDIRECT_URI']
        authorization_base_url = current_app.config['AUTHORISATION_BASE_URL']
        google = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
        authorization_url, state = google.authorization_url(authorization_base_url, access_type="offline",
                                                            approval_prompt="force")
        session['oauth_state'] = state
        return redirect(authorization_url)
    #here if user has session token then we need to validate that session token with db stored token
    else:
        print session['oauth_state']
        print session['oauth_token']
        print session['email_id']
        AccesssToken = session['oauth_token']['access_token']
        RefreshToken = session['oauth_token']['refresh_token']
        print AccesssToken
        print RefreshToken
        user = User.query.filter_by(email=session['email_id']).first()
        if user:
            validate_url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?'
                            'access_token=%s' % user.auth_token)
            valid_user =requests.get(validate_url).json()
            #Now here if auth token is not valid which will return no result in calling that API. redirect to refresh token.
            if 'error' in valid_user:
                return redirect(url_for('auth.refresh_token'))

            #if token is valid then we will redirect user as logged in and then send them to main page.
            else:
                print valid_user
                print valid_user['email']
                print valid_user['expires_in']
                login_user(user, True)
                return redirect(url_for('main.index'))
        #If user does not exists in DB then we will send user to login page with google login.
        else:
            return redirect(url_for('auth.login'))


# This is callback URL
@bp.route('/callback')
def callback():
    client_id = current_app.config['OAUTH_CREDENTIALS_GOOGLE_ID']
    scope = current_app.config['SCOPE']
    redirect_uri = current_app.config['REDIRECT_URI']
    authorization_base_url = current_app.config['AUTHORISATION_BASE_URL']
    client_secret = current_app.config['OAUTH_CREDENTIALS_GOOGLE_SECRET']
    token_url = current_app.config['TOKEN_URL']

    google = OAuth2Session(client_id, redirect_uri=redirect_uri,state=session['oauth_state'])
    token = google.fetch_token(token_url, client_secret=client_secret,authorization_response=request.url)
    if token is None:
        return render_template('errors/404.html')
    print token
    session['oauth_token'] = token
    user_profile = google.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
    print user_profile
    user = User.query.filter_by(email=user_profile['email']).first()
    print "I am checking for user %s if it is in DB" %user_profile['email']
    session['email_id']=user_profile['email']
    print session['email_id']
    if user:
        return redirect(url_for('auth.validate_authToken'))

    else:
        user = User(nickname=user_profile['given_name'], email=user_profile['email'],
                    auth_token=token['access_token'], refresh_token=token['refresh_token'],
                    expires_in=token['expires_in'])
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered and Logged in!')
        login_user(user, True)
        return redirect(url_for('main.index'))


@bp.route('/validate_authToken', methods=['GET', 'POST'])
def validate_authToken():
    valid_token_session = session['oauth_token']
    print valid_token_session
    user = User.query.filter_by(email=session['email_id']).first()
    valid_token_db = user.auth_token
    ref_token = user.refresh_token
    #Condition to check token stored in DB and session are the same then check if it is valid.
    if valid_token_session['access_token'] == valid_token_db:
        validate_url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?' 'access_token=%s' % valid_token_session)
        validata = jsonify(requests.get(validate_url).json())
        if validata:
            login_user(user, True)
            return redirect(url_for('main.index'))
        #If token becomes invalid we need to refresh it using the below method
        else:
            return redirect(url_for('auth.refresh_token'))

    else:
        validate_data = requests.get('https://www.googleapis.com/oauth2/v1/tokeninfo?' 'access_token=%s' % valid_token_session)
        if validate_data:
            login_user(user, True)
            return redirect(url_for('main.index'))
        else:
            return redirect(url_for('auth.refresh_token'))



#This is decorator function will refresh token
@bp.route('/refresh_token',methods=['GET','POST'])
def refresh_token():
    token = session['oauth_token']
    refresh_url = current_app.config['TOKEN_URL']
    extra = {
        'client_id': current_app.config['OAUTH_CREDENTIALS_GOOGLE_ID'],
        'client_secret': current_app.config['OAUTH_CREDENTIALS_GOOGLE_SECRET'],
        'offline': True
    }
    def token_updater(token):
        session['oauth_token'] = token

    google = OAuth2Session(current_app.config['OAUTH_CREDENTIALS_GOOGLE_ID'],
                           token=token,
                           auto_refresh_kwargs=extra,
                           auto_refresh_url=refresh_url,
                           token_updater=token_updater)
    user_profile = google.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
    #If we get new token just update that token in db and not sure about session if it auto update we need to validate it.
    if user_profile:
        print user_profile
        print session['oauth_token']

        user = User.query.filter_by(email=user_profile['email']).first()
        user.refresh_token=session['oauth_token']['refresh_token'],
        user.auth_token = session['oauth_token']['access_token']
        db.session.commit()
        login_user(user, True)
        return redirect(url_for('main.index'))
    else:
        return redirect(url_for('auth.login'))






# This Decorator function is for creating user
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(nickname=form.nickname.data, email=form.email.data, mob=int(form.mob.data))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)


# This decorator function will be for logout
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

