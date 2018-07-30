from flask_sqlalchemy  import SQLAlchemy
from app import db,ma
from datetime import datetime
from flask import url_for, current_app
from app.utils.exceptions import ValidationError
from sqlalchemy.dialects.mysql import LONGBLOB
from marshmallow import  fields, pre_load, validate
from app.models.Person_model import PersonSchema
from app.models.ExpType_model import ExpTypeSchema

#This is model defination for the Expnese Table and its api calls with get post put all covered in here.
class Expenses(db.Model):
    __tablename__ = 'Expesnes'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    per_id = db.Column(db.Integer, db.ForeignKey('Persons.id'), nullable=False)
    U_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False, index=True)
    Exp_per_name = db.Column(db.String(64), index=True)
    Exp_type_name = db.Column(db.String(100),index=True)
    Exp_amt = db.Column(db.Float)
    Exp_img = db.Column(db.LargeBinary)
    Exp_FileName = db.Column(db.String(300))
    Exp_date = db.Column(db.DateTime,index=True)
    Exp_comm = db.Column(db.String(200))

    def __init__(self,per_id,U_id,Exp_per_name,Exp_type_name,Exp_amt,Exp_img,Exp_FileName,Exp_date,Exp_comm):

        self.U_id = U_id
        self.per_id = per_id
        self.Exp_per_name = Exp_per_name,
        self.Exp_type_name = Exp_type_name,
        self.Exp_amt = Exp_amt,
        self.Exp_img = Exp_img,
        self.Exp_FileName = Exp_FileName,
        self.Exp_date = Exp_date,
        self.Exp_comm = Exp_comm
# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')

class ExpensesSchema(ma.Schema):
    class Meta:
        model = Expenses
    id = fields.Integer(dump_only=True)
    u_id = fields.Integer(dump_only=True)
    Exp_per_name = fields.Nested(PersonSchema, validate=must_not_be_blank)
    ExpType_name = fields.Nested(ExpTypeSchema,validate=must_not_be_blank)
    Exp_amt =fields.Float(required=True)
    Exp_img = fields.Raw()
    Exp_FileName = fields.Str(allow_none=None)
    Exp_comm = fields.Str(allow_none=None)



