from flask_sqlalchemy  import SQLAlchemy
from app import db,ma
from datetime import datetime
from flask_table import Table,Col
from app.utils.exceptions import ValidationError
from flask import url_for, current_app
from marshmallow import Schema, fields, pre_load, validate

class Persons(db.Model):
    __tablename__ = 'Persons'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('Users.id'),
                     nullable=False)  # This is foreign key to users table so that id will be identify unique.
    per_name = db.Column(db.String(64), index=True)
    per_sex = db.Column(db.String(1), index=True)
    per_bdate = db.Column(db.DATE)
    per_cdate = db.Column(db.DateTime, default=datetime.utcnow())
    Sharesor = db.relationship('Shares', backref='sharesor', lazy='dynamic')
    Investor = db.relationship('Investments', backref='investor', lazy='dynamic')
    Expensor = db.relationship('Expenses', backref='expensor', lazy='dynamic')
    Earner = db.relationship('Earnings', backref='earner', lazy='dynamic')


    def __init__(self, _per_name, _per_sex,_per_bdate):
        self.per_name = _per_name
        self.per_sex = _per_sex
        self.per_bdate =_per_bdate


class PersonSchema(ma.Schema):
    class Meta:
        model = Persons
    id = fields.Integer(dump_only=True)
    per_name = fields.String(required=True)
    per_sex = fields.String(required=True, validate=validate.Length(1))
    per_bdate = fields.DateTime()


'''
    def json(self):
        return {'per_name': self.per_name,
                'per_sex': self.per_sex,
                'per_bdate': self.per_bdate,
                'id': self.id,
                'U_id': self.u_id}
    @staticmethod
    def add_per_name(_perName, _persex, _perbdate):
        new_person = Persons(u_id=current_user.id, per_name=_perName, per_sex=_persex, per_bdate=_perbdate)
        db.session.add(new_person)
        db.session.commit()
        return "New Record Created"

    @staticmethod
    def get_all_persons():
        return {'persons': [marshal(person, person_fields) for person in Persons.query.filter_by(u_id=current_user.id)]}
        #return [Persons.json(persons) for persons in Persons.query.filter_by(u_id=current_user.id)]

    @staticmethod
    def get_single_person(_id):
        if Persons.query.filter_by(u_id=current_user.id, id=_id).first() is None:
            return "Sorry No records found with this ID"
        else:
            return {'persons': [marshal(person, person_fields) for person in Persons.query.filter_by(u_id=current_user.id, id=_id).first()]}

    @staticmethod
    def delete_person(_id):
        if Persons.query.filter_by(u_id=current_user.id, id=_id) is None:
            return "Sorry No records found with this ID can not delete"
        else:
            Persons.query.filter_by(u_id=current_user.id, id=_id).delete()
            db.session.commit()
            return "Record Deleted."

    @staticmethod
    def update_persons(id, _per_name, _per_sex, _per_bdate):
        PerName_res = Persons.query.filter_by(u_id=current_user.id, id=id).first()
        if PerName_res is None:
            return "Sorry No records found with this ID can not update"
        else:
            PerName_res.per_name = _per_name
            PerName_res.per_sex = _per_sex
            PerName_res.per_bdate = _per_bdate
            db.session.commit()
            return "Record updated fine"

    def __repr__(self):
        per_type_object = {'per_name': self.per_name,
                           'per_sex': self.per_sex,
                           'per_bdate': self.per_bdate,
                           'id': self.id,
                           'U_id': self.u_id
                           }
        return json.dumps(per_type_object)
'''
