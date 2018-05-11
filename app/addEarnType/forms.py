from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,RadioField, SubmitField,SelectField,DateField,FileField,TextAreaField,FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models.Eartype_model import EarType
from wtforms.fields.html5 import DateField

#This is entry form for Earning Type in UI
class EntryEarnTypeForm(FlaskForm):
    Earn_Type = StringField('Earning Type:-',validators = [DataRequired(),Length(min=1,max=56)])
    submit = SubmitField('Save EarningType')




#This will be edit Earning Type form in UI may be delete entry.
class EditEarnTypeForm(FlaskForm):
    Earn_Type = StringField('Earning Type:-', validators=[DataRequired(), Length(min=1, max=56)])
    submit = SubmitField('Save')
    Delete = SubmitField('Delete')


