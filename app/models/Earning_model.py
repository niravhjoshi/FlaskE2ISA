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
    Ear_per_name = db.Column(db.String(64), index=True)
    Ear_type_name = db.Column(db.String(100),index=True)
    Ear_amt = db.Column(db.Float)
    Ear_date = db.Column(db.DateTime,index=True)
    Ear_img = db.Column(db.Binary)
    Ear_FileName = db.Column(db.String(300))
    Ear_comm = db.Column(db.String(200))

    def ear_get_url(self):
        return url_for('get_earnings', id=self.id, _external=True)

    def ear_export_data(self):
        return {
            'self_url': self.get_url(),
            'name': self.Ear_per_name
        }

    def ear_import_data(self, data):
        try:
            self.Ear_per_name = data['Ear_per_name'],
            self.Ear_type_name = data['Ear_type_name'],
            self.Ear_amt = data['Ear_amt'],
            self.Ear_date = data['Ear_date'],
            self.Exp_comm = data['Exp_comm'],
            self.Ear_img = data['Ear_img'],
            self.Ear_comm = data['Ear_comm']
        except KeyError as e:
            raise ValidationError('Invalid Investments Person Name: missing ' + e.args[0])
        return self

