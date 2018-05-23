from flask_sqlalchemy  import SQLAlchemy
from app import db
from datetime import datetime
from flask import url_for, current_app
from app.utils.exceptions import ValidationError

#This is model defination for the Expnese Table and its api calls with get post put all covered in here.
class Investments(db.Model):
    __tablename__ = 'Investments'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    per_id = db.Column(db.Integer, db.ForeignKey('Persons.id'), nullable=False)
    Inv_per_name = db.Column(db.String(64), index=True)
    Inv_type_name = db.Column(db.String(100),index=True)
    Inv_init_amt = db.Column(db.Float)
    Inv_mat_amt = db.Column(db.Float)
    Inv_ROI_PerYear = db.Column(db.Float)
    Inv_date = db.Column(db.DateTime,index=True)
    Inv_mat_date = db.Column(db.DateTime,index=True)
    Inv_due_date = db.Column(db.DateTime,index=True)
    Inv_img = db.Column(db.LargeBinary)
    Inv_comm = db.Column(db.String(200))

    def inv_get_url(self):
        return url_for('get_investments', id=self.id, _external=True)

    def inv_export_data(self):
        return {
            'self_url': self.get_url(),
            'name': self.Inv_per_name
        }

    def inv_import_data(self, data):
        try:
            self.Inv_per_name = data['Inv_per_name'],
            self.Inv_type_name = data['Inv_type_name'],
            self.Inv_amt = data['Inv_amt'],
            self.Inv_date = data['Inv_date'],
            self.Inv_mat_date =data['Inv_mat_date'],
            self.Inv_due_date = data['Inv_due_date'],
            self.Inv_img = data['Inv_img'],
            self.Inv_comm = data['Inv_comm']
        except KeyError as e:
            raise ValidationError('Invalid Investments Person Name: missing ' + e.args[0])
        return self

