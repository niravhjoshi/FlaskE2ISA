from flask_sqlalchemy  import SQLAlchemy
from app import db
from datetime import datetime
from flask import url_for, current_app
from app.utils.exceptions import ValidationError

#This will be share market model db and it will store about your investment about share market.

class Shares(db.Model):
    __tablename__ = 'Shares'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    per_id = db.Column(db.Integer, db.ForeignKey('Persons.id'), nullable=False)
    Share_per_name = db.Column(db.String(64),index=True)
    Share_tick_name = db.Column(db.String(100),index=True)
    Share_Count = db.Column(db.Float)
    Share_tran_type = db.Column(db.String(50),index=True)
    Share_pershare_amt =db.Column(db.Float)
    Share_inv_sell_date = db.Column(db.DateTime,index=True)
    Share_img = db.Column(db.LargeBinary)
    Share_FileName = db.Column(db.String(300))
    Share_comm = db.Column(db.String(200))

    def share_get_url(self):
        return url_for('get_shares', id=self.id, _external=True)

    def shares_export_data(self):
        return {
            'self_url': self.get_url(),
            'name': self.Share_per_name
        }

    def shares_import_data(self, data):
        try:
            self.Share_per_name = data['Share_per_name'],
            self.Share_tick_name = data['Share_tick_name'],
            self.Share_Count = data['Share_Count'],
            self.Share_tran_type = data['Share_tran_type'],
            self.Share_pershare_amt = data['Share_pershare_amt'],
            self.Share_inv_sell_date = data['Share_inv_sell_date'],
            self.Share_img = data['Share_img'],
            self.Share_comm = data['Share_comm']

        except KeyError as e:
            raise ValidationError('Invalid Investments Person Name: missing ' + e.args[0])
        return self


