from flask import *
from .forms import LoginForm, GetEmailForm, SignupForm
from flask_login import current_user, login_user, login_required, logout_user
from . import login_manager
import os.path
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
        # check for a specifc email and password
        # in order to avoid SQL injection etc..
        if form.email.data == "admin@eatery.co.il" and form.password.data == "Password1":
            user = User.query.filter_by(email=form.email.data).first()
            login_user(user)
            return redirect(url_for('main_bp.dashboard'))

        flash('Invalid email/password')
        return redirect(url_for('main_bp.load_admin_login'))

    return render_template(
        'admin_login/login.jinja2',
        form=form,
        title='Log in - Eatery Cafe',
        template='login-page',
        body="Log in with your User account."
    )


@auth_bp.route('/admin-dir/hideshar/signup', methods=['GET', 'POST'])
def signup():
    """User sign-up page.
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
        body="Sign up for a user account."
    )
