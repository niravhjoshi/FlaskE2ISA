from flask_sqlalchemy  import SQLAlchemy
from app import db,ma
from datetime import datetime
from app.utils.exceptions import ValidationError
from flask import url_for, current_app
from marshmallow import Schema, fields, pre_load, validate

class EarType(db.Model):
    __tablename__ = 'EarType'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('Users.id'),nullable=False)  # This is foreign key to users table so that id will be identify unique.
    EarType_name = db.Column(db.String(64), index=True)
    EarType_cdate = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self,EarType_name,u_id):
        self.EarType_name= EarType_name,
        self.u_id= u_id

class EarTypeSchema(ma.Schema):
    class Meta:
        model = EarType
    id = fields.Integer(dump_only=True)
    u_id = fields.Integer(dump_only=True)
    EarType_name = fields.String(required=True)
