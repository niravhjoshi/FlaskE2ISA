from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,RadioField, SubmitField,SelectField,DateField,FileField,TextAreaField,FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models.ExpType_model import ExpType
from wtforms.fields.html5 import DateField

#This is entry form for Expense Type in UI
class EntryExpTypeForm(FlaskForm):
    Exp_Type = StringField('Expense Type:-',validators = [DataRequired(),Length(min=1,max=56)])
    submit = SubmitField('Save ExpenseType')

#This will be edit Expense Type form in UI may be delete entry.
class EditExpTypeForm(FlaskForm):
    Exp_Type = StringField('Expense Type:-', validators=[DataRequired(), Length(min=1, max=56)])
    submit = SubmitField('Save')
    Delete = SubmitField('Delete')


