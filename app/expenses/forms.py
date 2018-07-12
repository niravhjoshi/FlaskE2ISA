from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DateField, TextAreaField, \
    FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db


# This form will insert Expense into database


class ExpenseEntryForm(FlaskForm):
    Exp_per_name = SelectField('PersonName', choices=[], coerce=int)
    Exp_type_name = SelectField('ExpenseType Name', choices=[], coerce=int)
    Exp_amt = FloatField('Expense Amount:-', validators=[DataRequired()])
    Exp_date = DateField('Expense Date:-', format='%Y-%m-%d', validators=[DataRequired()])
    Exp_FileName = StringField('FileName:-')
    Exp_img = FileField('Expense Proof File:-', validators=[FileAllowed(['jpg','pdf','jpeg','png'],'Images and PDF only')])
    Exp_comm = TextAreaField('Expense Comment:-', validators=[DataRequired()])
    submit = SubmitField('Save Expense')


class ExpenseEditForm(FlaskForm):
    Exp_per_name = SelectField('PersonName', choices=[], coerce=int)
    Exp_type_name = SelectField('ExpenseType Name', choices=[], coerce=int)
    Exp_amt = FloatField('Expense Amount:-', validators=[DataRequired()])
    Exp_date = DateField('Expense Date:-', format='%Y-%m-%d', validators=[DataRequired()])
    Exp_FileName = StringField('FileName:-')
    Exp_img = FileField('Expense Proof File:-',validators=[FileAllowed(['jpg','pdf','jpeg','png'],'Images and PDF only')])
    Exp_comm = TextAreaField('Expense Comment:-', validators=[DataRequired()])
    submit = SubmitField('Submit')
    Delete = SubmitField('Delete')
