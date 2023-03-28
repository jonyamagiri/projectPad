from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


"""starts a flask web application"""
app = Flask(__name__)


"""configures the flask application"""
app.config['SECRET_KEY'] = '2b709ee3c5f6efa2f8e64048e04f230c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)


class User(db.Model):
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


# dummy data for testing
articles = [
    {
        'author': 'Kara Danvers',
        'title': 'Article 1',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias illo, eveniet odio quasi eaque sed voluptatum ducimus earum molestiae voluptates',
        'date_created': 'Jan 20, 2023'
    },
    {
        'author': 'James Olsen',
        'title': 'Article 2',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti doloribus dolorum quia. Ea esse excepturi blanditiis quas ullam, quae sed temporibus, ab a, magni deleniti.',
        'date_created': 'Feb 14, 2023'
    }
]

@app.route("/", strict_slashes=False)
@app.route("/home")
def home():
    """Returns the home page"""
    return render_template('home.html', articles=articles)

@app.route("/project_log", strict_slashes=False)
def project_log():
    """Returns the project_log page"""
    return render_template('project_log.html', title='Project Logs', articles=articles)

@app.route("/about", strict_slashes=False)
def about():
    """Returns the about page"""
    return render_template('about.html', title='About')

@app.route("/register", strict_slashes=False, methods=['GET', 'POST'])
def register():
    """Returns the register page"""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}".format(form.username.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", strict_slashes=False, methods=['GET', 'POST'])
def login():
    """Returns the login page"""
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'myself@example.com'and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('project_log'))
        else:
            flash('Login failed! Please check your username or password and try again', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == "__main__":
    app.run(debug=True)