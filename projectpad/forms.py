from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    """
    Flask form for user registration.

    Attributes:
        username (StringField): A field for the user's desired username.
        email (StringField): A field for the user's email address.
        password (PasswordField): A field for the user's desired password.
        confirm_password (PasswordField): A field for the user to confirm their desired password.
        submit (SubmitField): A field for submitting the form.
    """
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    """
    Flask form for user login.

    Attributes:
        email (StringField): A field for the user's email address.
        password (PasswordField): A field for the user's password.
        remember (BooleanField): A field for the user to indicate whether they want to be remembered.
        submit (SubmitField): A field for submitting the form.
    """
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')