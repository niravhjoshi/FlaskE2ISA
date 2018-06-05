from flask_wtf import FlaskForm,Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,DateField,TextAreaField,FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models.Earning_model import Earnings
from app.models.Person_model import Persons
from app.models.Eartype_model import EarType
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import current_user, login_user,logout_user,login_required
from app import app,db
# This form will insert earnings into database

'''
def choice_pername():
    return Persons.query.filter_by(u_id=current_user.id)
    #return Persons.query.with_entities(Persons.per_name).filter_by(u_id=current_user.id)

def choice_eartype():
    return EarType.query.filter_by(u_id=current_user.id)
'''

class EarningEntryForm(FlaskForm):
    Ear_per_name=SelectField('PersonName', choices=[], coerce=int)
    Ear_type_name=SelectField('EarningType Name', choices=[], coerce=int)
    Ear_amt = FloatField('Earning Amount:-',validators=[DataRequired()])
    Ear_date = DateField('Earning Date:-',format = '%Y-%m-%d',validators=[DataRequired()])
    Ear_FileName = StringField('Earning FileName:-')
    Ear_img = FileField('Earning Proof File:-')
    Ear_comm = TextAreaField('Earning Comment:-',validators=[DataRequired()])
    submit = SubmitField('Save Earning')


class EarningEditForm(FlaskForm):
    Ear_per_name = SelectField('PersonName', choices=[], coerce=int)
    Ear_type_name = SelectField('EarningType Name', choices=[], coerce=int)
    Ear_amt = FloatField('Earning Amount:-', validators=[DataRequired()])
    Ear_date = DateField('Earning Date:-', format='%Y-%m-%d', validators=[DataRequired()])
    Ear_FileName = StringField('Earning FileName:-',validators=[DataRequired()])
    Ear_img = FileField('Earning Proof File:-')
    Ear_comm = TextAreaField('Earning Comment:-', validators=[DataRequired()])
    submit = SubmitField('Submit')
    Delete = SubmitField('Delete')

