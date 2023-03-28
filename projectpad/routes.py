from flask import render_template, url_for, flash, redirect, request
from projectpad import app, db
from projectpad.forms import RegistrationForm, LoginForm
from projectpad.models import User, Article
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You can now log in.", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", strict_slashes=False, methods=['GET', 'POST'])
def login():
    """Returns the login page"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('project_log'))
        else:
            flash('Login failed! Please check your email or password and try again', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    """Returns the logout page"""
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    """Returns the account page"""
    return render_template('account.html', title='Account')