from flask_sqlalchemy  import SQLAlchemy
from app import db
from datetime import datetime
from flask import url_for, current_app
from app.utils.exceptions import ValidationError
from sqlalchemy.dialects.mysql import LONGBLOB

#This is model defination for the Expnese Table and its api calls with get post put all covered in here.
class Expenses(db.Model):
    __tablename__ = 'Expesnes'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    per_id = db.Column(db.Integer, db.ForeignKey('Persons.id'), nullable=False)
    Exp_per_name = db.Column(db.String(64), index=True)
    Exp_type_name = db.Column(db.String(100),index=True)
    Exp_amt = db.Column(db.Float)
    Exp_img = db.Column(db.LargeBinary)
    Exp_FileName = db.Column(db.String(300))
    Exp_date = db.Column(db.DateTime,index=True)
    Exp_comm = db.Column(db.String(200))

    def exp_get_url(self):
        return url_for('get_expense', id=self.id, _external=True)

    def exp_export_data(self):
        return {
            'self_url': self.exp_get_url(),
            'name': self.Exp_per_name,
            'type': self.Exp_type_name,
            'amt': self.Exp_amt,
            'date': self.Exp_date
        }

    def exp_import_data(self, data):
        try:
            self.Exp_per_name = data['Exp_per_name'],
            self.Exp_type_name =data['Exp_type_name'],
            self.Exp_amt = data['Exp_amt'],
            self.Exp_date = data['Exp_date'],
            self.Exp_comm = data['Exp_comm']

        except KeyError as e:
            raise ValidationError('Invalid Expense PersonName: missing ' + e.args[0])
        return self


