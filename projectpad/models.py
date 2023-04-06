from datetime import datetime
from flask import app
from projectpad import db, login_manager
from flask_login import UserMixin


# defines function that loads a user from the database
@login_manager.user_loader
def load_user(user_id):
    """
    A function that loads a user from the database.

    Attributes:
        user_id (int): The unique identifier for the user.

    Returns:
        User: The user with the given ID.
    """
    return User.query.get(int(user_id))


# defines the User model
class User(db.Model, UserMixin):
    """
    A class representing a user.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The user's username.
        email (str): The user's email address.
        image_file (str): The filename of the user's profile image.
        password (str): The user's hashed password.
        articles (RelationshipProperty): A relationship to the user's articles, represented by the 'Article' class.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    articles = db.relationship('Article', backref='author', lazy=True)

    def __repr__(self):
        """ Returns a string representation of the user """
        return "User('{}', '{}', '{}')".format(self.username, self.email, self.image_file)


# defines the Article model
class Article(db.Model):
    """
    A class representing an article.

    Attributes:
        id (int): The unique identifier for the article.
        title (str): The title of the article.
        date_created (datetime): The date and time the article was created.
        content (str): The content of the article.
        user_id (int): The foreign key referring to the ID of the user who created the article from the 'User' class.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """ Returns a string representation of the article """
        return "Article('{}', '{}', '{}')".format(self.title, self.date_created)
