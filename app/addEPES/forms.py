from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,RadioField, SubmitField,SelectField,DateField,FileField,TextAreaField,FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models.Earning_model import Earnings
from wtforms.fields.html5 import DateField

# This form will insert persons for user into database
class PersonsAddEntryForm(FlaskForm):
    Person_Name = StringField('PersonName:-',validators = [DataRequired(),Length(min=1,max=56)])
    Per_Sex = RadioField('Person Sex:',choices=[('M', 'Male'),('F', "Female"),('O', "Other")],validators=[DataRequired(), ])
    Per_Bdate = DateField('Person BirthDate:-', format = '%Y-%m-%d',validators=[DataRequired()])
    submit = SubmitField('Save Person')


#This is form for edit person form for Perons table
class PersonEditForm(FlaskForm):
    Person_Name = StringField('PersonName:-', validators=[DataRequired(), Length(min=1, max=56)])
    Per_Sex = RadioField('Person Sex:', choices=[('M', 'Male'), ('F', "Female"), ('O', "Other")],validators=[DataRequired(), ])
    Per_Bdate = DateField('Person BirthDate:-', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')