from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


"""starts a flask web application"""
app = Flask(__name__)


"""configures the flask application"""
app.config['SECRET_KEY'] = '2b709ee3c5f6efa2f8e64048e04f230c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from projectpad import routes