from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,DateField,FileField,TextAreaField,FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models.Earning_model import Earnings

