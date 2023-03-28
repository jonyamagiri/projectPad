from flask import Flask
from flask_sqlalchemy import SQLAlchemy


"""starts a flask web application"""
app = Flask(__name__)


"""configures the flask application"""
app.config['SECRET_KEY'] = '2b709ee3c5f6efa2f8e64048e04f230c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)

from projectpad import routes