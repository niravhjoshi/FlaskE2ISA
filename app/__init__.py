from flask import  Flask, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_login import current_user, login_user, logout_user, login_required
from app.config import Config
from app.decorators import json, no_cache, rate_limit
import logging
from flask import Blueprint
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_restful import Api

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
loginMan = LoginManager(app)
loginMan.login_view = 'auth.login'
loginMan.login_message = ('Please log in to access this page.')
loginMan.session_protection = "strong"

# Mail configuration for Error loging
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='E2ISA Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    # Error loging to Error log file
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/E2ISA_log.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.DEBUG)
    app.logger.info('E2ISA App startup')

from models.Share_model import Shares
from models.Investment_model import Investments
from models.Users_model import User
from models.Earning_model import Earnings
from models.Expense_model import Expenses
from models.Eartype_model import EarType
from models.ExpType_model import ExpType
from models.Investtype_model import InvType
from models.Person_model import Persons

#Blue Prints imports
from app.resourcesapi import api_bp as apiV2
from app.shares import bp as shares
from app.investments import bp as investments
from app.expenses import bp as expenses
from app.earnings import bp as earning
from app.auth import bp as auth
from app.error import bp as error
from app.addEPES import bp as addEPES
from app.main import bp as main
from app.addEarnType import bp as addEarnType
from app.addExpType import bp as addExpType
from app.addInvType import bp as addInvType
from app.api_v1 import bp as apiV1


# Blueprint Import with all blueprint available
app.register_blueprint(shares)
app.register_blueprint(investments)
app.register_blueprint(expenses)
app.register_blueprint(earning)
app.register_blueprint(auth)
app.register_blueprint(error)
app.register_blueprint(main)
app.register_blueprint(addEPES)
app.register_blueprint(addEarnType)
app.register_blueprint(addExpType)
app.register_blueprint(addInvType)
app.register_blueprint(apiV1)
app.register_blueprint(apiV2,url_prefix='/apiV2')

#API Routes
