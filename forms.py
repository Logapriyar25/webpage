from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from market.model import User

class RegisterForm(FlaskForm):
    username = StringField(label="User Name:")
    email = StringField(label="Email Address:")
    password1 = PasswordField(label="Password:")
    password2 = PasswordField(label="confirm Password:")
    submit = SubmitField(label="Register")

class LoginForm(FlaskForm):
    username = StringField(label="User Name:")
    password = PasswordField(label="Password:")
    submit = SubmitField(label="Login")

class ResetRequestForm(FlaskForm):
    email = StringField(label="Email Address:")
    submit = SubmitField(label="Reset Password")
