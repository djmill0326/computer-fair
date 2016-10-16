from messenger import app
from messenger import lm
from messenger import testdb as db
from messenger.models import User
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user
from passlib.hash import sha256_crypt

from messenger.forms import LoginForm, RegisterForm


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'dop'}
    return render_template('index.html', user=user, title='Main Page', header=True)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = db['users'].find_one({"username": form.username.data})
        if user and User.validate_login(user['hash'], form.password.data):
            user_obj = User(user['username'])
            login_user(user_obj)
            flash("Login successful")
            return redirect(url_for('index'))
        flash("Wrong username or password")
    return render_template('login.html', form=form, title="Login")


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        hash = sha256_crypt.encrypt(password)
        db['users'].insert_one(
            {
                'real_name': firstname + " " + lastname,
                'email': email,
                'username': username,
                'hash': hash
            }
        )
        return redirect(url_for('login'))
    flash("Please fill out form correctly")
    return render_template('register.html', form=form, title="Register")


@app.route('/logout')
def logout():
    return "logout"

@lm.user_loader
def load_user(username):
    u = db['users'].find_one({"username": username})
    print(u)
    if not u:
        return None
    return User(u["username"])
