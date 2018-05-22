from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,RadioField, SubmitField,SelectField,DateField,FileField,TextAreaField,FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models.Investtype_model import InvType
from wtforms.fields.html5 import DateField

#This is entry form for Expense Type in UI
class EntryInvTypeForm(FlaskForm):
    Inv_Type = StringField('Investment Type:-',validators = [DataRequired(),Length(min=1,max=56)])
    submit = SubmitField('Save InvestmentType')

#This will be edit Expense Type form in UI may be delete entry.
class EditInvTypeForm(FlaskForm):
    Inv_Type = StringField('Investment Type:-', validators=[DataRequired(), Length(min=1, max=56)])
    submit = SubmitField('Save')
    Delete = SubmitField('Delete')


