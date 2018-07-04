from flask_login import UserMixin,LoginManager
from flask_sqlalchemy  import SQLAlchemy
from app import db,loginMan
from datetime import datetime
from hashlib import md5
from dateutil.tz import tzutc
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import url_for, current_app
from flask_login import UserMixin
from .Expense_model import Expenses
from .Earning_model import Earnings
from .Investment_model import Investments
from .Share_model import Shares

class User(UserMixin,db.Model):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=True, unique=True)
    pwd_hash = db.Column(db.String(512))
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    cdate = db.Column(db.DateTime, default=datetime.utcnow())
    ladate = db.Column(db.DateTime, default=datetime.utcnow())
    mob = db.Column(db.BigInteger, unique=True, nullable=True)
    confirmed = db.Column(db.Boolean, default=False)
    PersonName= db.relationship('Persons',backref='persor',lazy='dynamic')
    EarType = db.relationship('EarType',backref='eartypefk',lazy='dynamic')
    InvType = db.relationship('InvType',backref='invtypefk',lazy='dynamic')
    ExpType = db.relationship('ExpType',backref='exptypefk',lazy='dynamic')

    def set_password(self, password):
        self.pwd_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.pwd_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

# Load user function will load users details from DB to application memeory
@loginMan.user_loader
def load_user(id):
   return User.query.get(int(id))










'''
# This module may used in API frame work once we expose API

def generate_auth_token(self, expires_in=3600):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
    return s.dumps({'id': self.id}).decode('utf-8')

@staticmethod
def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return None
    return User.query.get(data['id'])

'''