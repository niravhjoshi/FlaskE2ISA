from flask_sqlalchemy  import SQLAlchemy
from app import db,ma
from datetime import datetime
from app.utils.exceptions import ValidationError
from flask import url_for, current_app
from marshmallow import Schema, fields, pre_load, validate

class InvType(db.Model):
    __tablename__ = 'InvType'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('Users.id'),nullable=False)  # This is foreign key to users table so that id will be identify unique.
    InvType_name = db.Column(db.String(64), index=True)
    InvType_cdate = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self,InvType_name,u_id):
        self.InvType_name= InvType_name,
        self.u_id= u_id

class InvestTypeSchema(ma.Schema):
    class Meta:
        model = InvType
    id = fields.Integer(dump_only=True)
    u_id = fields.Integer(dump_only=True)
    InvType_name = fields.String(required=True)
