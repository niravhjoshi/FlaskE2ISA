from flask_sqlalchemy  import SQLAlchemy
from app import db
from datetime import datetime
from app.utils.exceptions import ValidationError
from flask import url_for, current_app

#This will delcare model class for earnings and its relevant model will be display over here .

class Earnings(db.Model):
    __tablename__ = 'Earnings'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    Per_id = db.Column(db.Integer, db.ForeignKey('Persons.id'),nullable=False)  # This is foreign key to Persons table so that id will be identify unique.
    U_id = db.Column(db.Integer,db.ForeignKey('Users.id'),nullable=False,index=True)
    Ear_per_name = db.Column(db.String(64), index=True)
    Ear_type_name = db.Column(db.String(100),index=True)
    Ear_amt = db.Column(db.Float)
    Ear_date = db.Column(db.DateTime,index=True)
    Ear_img = db.Column(db.LargeBinary)
    Ear_FileName = db.Column(db.String(300))
    Ear_comm = db.Column(db.String(200))


