from flask import *
from .forms import LoginForm, GetEmailForm, SignupForm
from flask_login import current_user, login_user, login_required, logout_user
from . import login_manager
import os.path
import requests
from .models import db, User
import json


auth_bp = Blueprint('auth_bp',
                    __name__,
                    template_folder='templates',
                    static_folder='static')


@auth_bp.route('/admin-dir/hideshar/pollogin', methods=['GET', 'POST'])
def admin_login():
    """Log-in page for registered users.
    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard."""

    form = LoginForm()

    if form.validate_on_submit():
        # check for a specifc email & password - just for CTF purposes.
        # avoid any interatcion with the db - SQLi is not the goal here.
        requests
        if form.email.data == "avi@6clothing.co.il" and form.password.data == "any6gkbi":
            user = User.query.filter_by(email=form.email.data).first()

            login_user(user)
            return redirect(url_for('auth_bp.dashboard'))

        flash('Invalid email/password')
        return redirect(url_for('main_bp.load_admin_login'))

    return render_template(
        'admin_login/login.jinja2',
        form=form,
        title='Log in',
        template='login-page',
        body="Log in with your User."
    )


@auth_bp.route('/admin-dir/hideshar/signup', methods=['GET', 'POST'])
def signup():
    """User sign-up page. Just a trap!!!!
    GET requests serve sign-up page.
    POST requests validate form & user creation."""

    form = SignupForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            return redirect(url_for('main_bp.load_admin_login'))

        flash('A user already exists with that email address.')

    return render_template(
        'admin_login/signup.jinja2',
        title='Create an Account',
        form=form,
        template='signup-page',
        body="Sign up for a user."
    )


def _encode_auth_token(email):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'user': email,
            'iat': datetime.datetime.utcnow(),
            'is_admin': if email == 'eli
        }
        return jwt.encode(
            payload,
            auth_bp.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
