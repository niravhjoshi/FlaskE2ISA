from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,DateField,FileField,TextAreaField,FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models.Earning_model import Earnings

# This form will insert earnings into database
class EarningEntryForm(FlaskForm):
    Ear_per_name = SelectField('Earning PersonName:-',
                         #       default=(0, "Nirav"),
                          #     choices=[(0, "Nirav"), (1, "Arsh"), (2, "Pareen")],
                               id='select_pername')
    Ear_type_name = SelectField('Earning Type:-',
                           #     default=(0, "Salary"),
                            #    choices=[(0, "Salary"), (1, "Consulting"), (2, "Share")],
                                id='select_eartype')
    Ear_amt = FloatField('Earning Amount:-',validators=[DataRequired()])
    Ear_date = DateField('Earning Date:-',validators=[DataRequired()])
    Ear_img = FileField('Earning Proof File:-')
    Ear_comm = TextAreaField('Earning Comment:-',validators=[DataRequired()])
    submit = SubmitField('Save Earning')
