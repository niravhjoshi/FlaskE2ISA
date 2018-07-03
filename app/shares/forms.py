from flask_wtf import FlaskForm,Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,DateField,TextAreaField,FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import current_user, login_user,logout_user,login_required
from app import app,db

# This form will insert Expense into database
Trantype =[('buy','Buy'),('sell','Sell')]

class SharesEntryForm(FlaskForm):
    Share_per_name=SelectField('PersonName:-', choices=[], coerce=int)
    Share_tick_name=StringField('Share Ticker:-',validators=[DataRequired()])
    Share_Count = FloatField('Shares Count:-',validators=[DataRequired()])
    Share_tran_type = SelectField('Share Transaction Type:-',choices=Trantype, validators=[DataRequired()])
    Share_pershare_amt = FloatField('PerShare Amount:-', validators=[DataRequired()])
    Share_SellBuy_date = DateField('Share Sell or Buy Date:-',format = '%Y-%m-%d',validators=[DataRequired()])
    Share_FileName = StringField('FileName:-')
    Share_img = FileField('Share Proof File:-')
    Share_comm = TextAreaField('Share Comment:-',validators=[DataRequired()])
    submit = SubmitField('Save Shares')


class SharesEditForm(FlaskForm):
    Share_per_name = SelectField('PersonName:-', choices=[], coerce=int)
    Share_tick_name = StringField('Share Ticker:-', validators=[DataRequired()])
    Share_Count = FloatField('Shares Count:-', validators=[DataRequired()])
    Share_tran_type = SelectField('Share Transaction Type:-', choices=Trantype, validators=[DataRequired()])
    Share_pershare_amt = FloatField('PerShare Amount:-', validators=[DataRequired()])
    Share_SellBuy_date = DateField('Share Sell or Buy Date:-', format='%Y-%m-%d', validators=[DataRequired()])
    Share_FileName = StringField('FileName:-')
    Share_img = FileField('Share Proof File:-')
    Share_comm = TextAreaField('Share Comment:-', validators=[DataRequired()])
    submit = SubmitField('Submit')
    Delete = SubmitField('Delete')

