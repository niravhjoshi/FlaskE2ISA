from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from app.config import Config
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
login.login_view = 'login'


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

#Error loging to Error log file
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


from app import routes,errors
from models.Share_model import Shares
from models.Investment_model import Investments
from models.Users_model import User
from models.Earning_model import Earnings
from models.Expense_model import Expenses
from models.Eartype_model import EarType
from models.ExpType_model import ExpType
from models.Investtype_model import InvType
from models.Person_model import Persons

#Blueprint Import with all blueprint available
from app.investments import bp as investments
app.register_blueprint(investments)
from app.expenses import bp as expenses
app.register_blueprint(expenses)
from app.earnings import bp as earning
app.register_blueprint(earning)
from app.auth import bp as auth
app.register_blueprint(auth)
from app.error  import bp as error
app.register_blueprint(error)
from app.main import bp as main
app.register_blueprint(main)
from app.addEPES import bp as addEPES
app.register_blueprint(addEPES)
from app.addEarnType import bp as addEarnType
app.register_blueprint(addEarnType)
from app.addExpType import bp as addExpType
app.register_blueprint(addExpType)
from app.addInvType import bp as addInvType
app.register_blueprint(addInvType)
