from flask_sqlalchemy import SQLAlchemy
from app import db,ma
from datetime import datetime
from app.utils.exceptions import ValidationError
from flask import url_for, current_app,json
from datetime import datetime
from dateutil import parser as datetime_parser
from flask_login import current_user
from marshmallow import Schema, fields, pre_load, validate

class ExpType(db.Model):
    __tablename__ = 'ExpType'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('Users.id'),
                     nullable=False)  # This is foreign key to users table so that id will be identify unique.
    ExpType_name = db.Column(db.String(64), index=True)
    ExpType_cdate = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self,ExpType_name,u_id):
        self.ExpType_name= ExpType_name,
        self.u_id= u_id

class ExpTypeSchema(ma.Schema):
    class Meta:
        model = ExpType
    id = fields.Integer(dump_only=True)
    u_id = fields.Integer(dump_only=True)
    ExpType_name = fields.String(required=True)


'''
    def json(self):
        return {'ExpenseType':self.ExpType_name,'id':self.id,'U_id':self.u_id}

    @staticmethod
    def add_expense_type(_expType):
        new_expType = ExpType(u_id=current_user.id, ExpType_name=_expType)
        db.session.add(new_expType)
        db.session.commit()
        return "New Recordd Created"

    @staticmethod
    def get_all_exptypes():
        return[ExpType.json(exptype) for exptype in ExpType.query.filter_by(u_id=current_user.id)]

    @staticmethod
    def get_single_expType(_id):
        if ExpType.query.filter_by(u_id=current_user.id,id =_id).first() is None:
            return "Sorry No records found with this ID"
        else:
            return [ExpType.json(ExpType.query.filter_by(u_id=current_user.id,id =_id).first())]

    @staticmethod
    def delete_expType(_id):
        if ExpType.query.filter_by(u_id=current_user.id , id = _id) is None:
            return "Sorry No records found with this ID can not delete"
        else:
            ExpType.query.filter_by(u_id=current_user.id , id = _id).delete()
            db.session.commit()
            return "Record Deleted."

    @staticmethod
    def update_expType(id,exp_type):

        ExpName_toUpdate=ExpType.query.filter_by(u_id=current_user.id ,id = id).first()
        if ExpName_toUpdate is None:
            return "Sorry No records found with this ID can not update"
        else:
            ExpName_toUpdate.ExpType_name=exp_type
            db.session.commit()
            return "Record updated fine"


    def __repr__(self):
        exp_type_object={
            'ExpTypeName':self.ExpType_name,
            'ExpID':self.id,
            'UserID':self.u_id
        }
        return json.dumps(exp_type_object)
'''