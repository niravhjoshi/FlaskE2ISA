from flask_wtf import FlaskForm,Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,DateField,TextAreaField,FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField,FileAllowed
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import current_user, login_user,logout_user,login_required
from app import app,db

# This form will insert Expense into database


class InvestEntryForm(FlaskForm):
    Inv_per_name=SelectField('PersonName:-', choices=[], coerce=int)
    Inv_type_name=SelectField('Investment Type:-', choices=[], coerce=int)
    Inv_init_amt = FloatField('Investment Init Amount:-',validators=[DataRequired()])
    Inv_mat_amt = FloatField('Investment Mat Amount:-', validators=[DataRequired()])
    Inv_roiper_amt = FloatField('Investment ROI %:-', validators=[DataRequired()])
    Inv_date = DateField('Investment Date:-',format = '%Y-%m-%d',validators=[DataRequired()])
    Inv_Mat_date = DateField('Investment Mature Date:-', format='%Y-%m-%d', validators=[DataRequired()])
    Inv_due_date = DateField('Investment Due Date:-', format='%Y-%m-%d', validators=[DataRequired()])
    Inv_FileName = StringField('FileName:-')
    Inv_img = FileField('Investment Proof File:-',validators=[FileAllowed(['jpg','pdf','jpeg','png'],'Images and PDF only')])
    Inv_comm = TextAreaField('Investment Comment:-',validators=[DataRequired()])
    submit = SubmitField('Save Investment')


class InvestEditForm(FlaskForm):
    Inv_per_name = SelectField('PersonName:-', choices=[], coerce=int)
    Inv_type_name = SelectField('Investment Type:-', choices=[], coerce=int)
    Inv_init_amt = FloatField('Investment Init Amount:-', validators=[DataRequired()])
    Inv_mat_amt = FloatField('Investment Mat Amount:-', validators=[DataRequired()])
    Inv_roiper_amt = FloatField('Investment ROI %:-', validators=[DataRequired()])
    Inv_date = DateField('Investment Date:-', format='%Y-%m-%d', validators=[DataRequired()])
    Inv_Mat_date = DateField('Investment Mature Date:-', format='%Y-%m-%d', validators=[DataRequired()])
    Inv_due_date = DateField('Investment Due Date:-', format='%Y-%m-%d', validators=[DataRequired()])
    Inv_FileName = StringField('FileName:-',validators=[FileAllowed(['jpg','pdf','jpeg','png'],'Images and PDF only')])
    Inv_img = FileField('Investment Proof File:-')
    Inv_comm = TextAreaField('Investment Comment:-', validators=[DataRequired()])
    submit = SubmitField('Submit')
    Delete = SubmitField('Delete')

