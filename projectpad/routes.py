from flask import render_template, url_for, flash, redirect
from projectpad import app
from projectpad.forms import RegistrationForm, LoginForm
from projectpad.models import User, Article


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
