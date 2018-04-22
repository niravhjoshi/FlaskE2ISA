from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models.Users_model import User


#THis form represent login forms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

#This forms represent New User Registration with their email id
class RegistrationForm(FlaskForm):
    nickname =StringField('Your Nick Name:-',validators = [DataRequired(),Length(min=1,max=56)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mob = StringField('Enter your mobile#:-',validators=[DataRequired(), Length(min=10, max=10, message='Mobile no is more than 10')])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, nickname):
        user = User.query.filter_by(nickname=nickname.data).first()
        if user is not None:
            raise ValidationError('Please use a different nickname.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

#This form represent edit profile for the user
class EditProfileForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    mob = StringField('mob', validators=[DataRequired(),Length(min=10, max=10)])
    submit = SubmitField('Submit')

    def __init__(self, original_mob,orig_nickname, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_mob = original_mob
        self.orig_nickname =orig_nickname

    def validate_mob(self, original_mob):
        if original_mob.data != self.original_mob:
            muser = User.query.filter_by(mob=self.mob.data).first()
            if muser is not None:
                raise ValidationError('Please use a different Mobile.')
    def validate_nickname(self,orig_nickname):
        if orig_nickname.data != self.orig_nickname:
            nuser = User.query.filter_by(nickname=self.nickname.data).first()
            if nuser is not None:
                raise ValidationError('Please use a different NickName.')