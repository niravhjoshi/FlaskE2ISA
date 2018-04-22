from flask_sqlalchemy  import SQLAlchemy
from app import db
from datetime import datetime
from app.utils.exceptions import ValidationError
from flask import url_for, current_app

class ExpType(db.Model):
    __tablename__ = 'ExpType'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('Users.id'),nullable=False)  # This is foreign key to users table so that id will be identify unique.
    ExpType_name = db.Column(db.String(64), index=True)
    ExpType_cdate = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<ExpType_name {}>'.format(self.ExpType_name)
