from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_ckeditor import CKEditorField
from projectpad.models import User


# defines a FlaskForm subclass called RegistrationForm
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

    def validate_username(self, username):
        """
        Validates the username field in a form to ensure that it is not already taken.

        Attributes:
            username: The `username` field of the form to be validated.

        Raises:
            ValidationError: Raised if a user with the specified username already exists in the database.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
        
    def validate_email(self, email):
        """
        Validates the email field in a form to ensure that it is not already taken.

        Attributes:
            email: The `email` field of the form to be validated.

        Raises:
            ValidationError: Raised if a user with the specified email already exists in the database.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


# defines a FlaskForm subclass called LoginForm
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


# defines a FlaskForm subclass called UpdateAccountForm
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update your profile picture', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField('Update')

    # validates the username
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    # validates the email address
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


# defines a FlaskForm subclass called ArticleForm
class ArticleForm(FlaskForm):
    """
    Defines form used to create and edit articles.

    Attributes:
        title: A `StringField` representing the title of the article.
        content: A `CKEditorField` representing the content of the article.
        submit: A `SubmitField` representing the submission button for the form.
    """
    title = StringField('Title', validators=[DataRequired()])
    #content = TextAreaField('Content', validators=[DataRequired()])
    content = CKEditorField('Content', validators=[DataRequired()]) 
    submit = SubmitField('Save')
