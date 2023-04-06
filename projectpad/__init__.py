import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_mail import Mail


# creates a new Flask application and initializes the CKEditor extension
app = Flask(__name__)
ckeditor = CKEditor(app)


# configures the Flask application;  set-up secret key, database URI, and login manager
# set-up the SQLAlchemy database connection and the login manager for user authentication
app.config['SECRET_KEY'] = '2b709ee3c5f6efa2f8e64048e04f230c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# imports the routes module that defines the URL routes
from projectpad import routes