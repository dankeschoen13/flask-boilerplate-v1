from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, URL, Length, Optional, Email

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=250)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    name = StringField('Name', validators=[DataRequired(), Length(max=250)])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=250)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Sign in')