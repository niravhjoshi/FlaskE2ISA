from app import app,db
from flask import render_template,flash, redirect, url_for, request
from app.earnings.forms import EarningEntryForm
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime

#This deocrator function will ensure that if page is served it must have authenticated users
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()
