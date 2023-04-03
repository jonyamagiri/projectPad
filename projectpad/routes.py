import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from projectpad import app, db
from projectpad.forms import RegistrationForm, LoginForm, UpdateAccountForm, ArticleForm
from projectpad.models import User, Article
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_ckeditor import CKEditor



@app.route("/", strict_slashes=False)
@app.route("/home")
def home():
    """Serves the home page"""
    return render_template('home.html')

@app.route("/about", strict_slashes=False)
def about():
    """Serves the about page"""
    return render_template('about.html', title='About')

@app.route("/register", strict_slashes=False, methods=['GET', 'POST'])
def register():
    """Serves the register page"""
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
    """Serves the login page"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login failed! Please check your email or password and try again', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout", strict_slashes=False)
def logout():
    """Serves the logout page"""
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    """ Saves and returns the picture uploaded via form """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", strict_slashes=False, methods=['GET', 'POST'])
@login_required
def account():
    """Serves the account page"""
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)



@app.route("/dashboard", strict_slashes=False)
@login_required
def dashboard():
    """Serves the dashboard page"""
    articles = Article.query.filter_by(author=current_user).order_by(Article.date_created.desc()).all()
    return render_template('dashboard.html', title='Dashboard', articles=articles)

@app.route("/article/new", strict_slashes=False, methods=['GET', 'POST'])
@login_required
def new_article():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(article)
        db.session.commit()
        flash('Your article has been created!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_article.html', title='New Article', form=form, legend='New Article')

@app.route("/article/<int:article_id>", strict_slashes=False)
def article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', title=article.title, article=article)


@app.route("/article/<int:article_id>/update", strict_slashes=False, methods=['GET', 'POST'])
@login_required
def update_article(article_id):
    article = Article.query.get_or_404(article_id)
    if article.author != current_user:
        abort(403)
    form = ArticleForm()
    if form.validate_on_submit():
        article.title = form.title.data
        article.content = form.content.data
        db.session.commit()
        flash('Your article has been updated!', 'success')
        return redirect(url_for('article', article_id=article.id))
    elif request.method == 'GET':
        form.title.data = article.title
        form.content.data = article.content
    return render_template('create_article.html', title='Update Article', form=form, legend='Update Article')


@app.route("/article/<int:article_id>/delete", strict_slashes=False, methods=['GET','POST'])
@login_required
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    if article.author!= current_user:
        abort(403)
    db.session.delete(article)
    db.session.commit()
    flash('Your article has been deleted!','success')
    return redirect(url_for('dashboard', article_id=article.id))
