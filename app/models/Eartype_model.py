from flask_sqlalchemy  import SQLAlchemy
from app import db
from datetime import datetime
from app.utils.exceptions import ValidationError
from flask import url_for, current_app

class EarType(db.Model):
    __tablename__ = 'EarType'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('Users.id'),nullable=False)  # This is foreign key to users table so that id will be identify unique.
    EarType_name = db.Column(db.String(64), index=True)
    EarType_cdate = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<EarType {}>'.format(self.EarType_name)
