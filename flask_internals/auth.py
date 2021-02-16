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
        # avoid any interatcion with the db - SQLi isn't the goal here.
        if form.email.data == "avi@6clothing.co.il" and form.password.data == "any6gkbi":
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                login_user(user)
                response = make_response(
                    redirect('/admin-dir/hideshar/dashboard'))
                response.set_cookie(
                    'security_token', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImF2aSIsImlzX2FkbWluIjoiZmFsc2UifQ.cPwoXIJmCricMpXSMsuxKw6w2dikZMPQSDEfza0lgUw')
                return response

        flash('Invalid email/password')
        return redirect(url_for('auth_bp.admin_login'))

    return render_template(
        'admin_login/login.jinja2',
        form=form,
        title='Log in',
        template='login-page',
        body="Log in with your User."
    )


@ auth_bp.route('/admin-dir/hideshar/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page. Just a trap, it's never really signing up.
    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            # this gives an indication - this email is in use.
            flash('A user already exists with that email address.')
            return redirect(url_for('auth_bp.signup'))

        return redirect(url_for('auth_bp.admin_login'))

    return render_template(
        'admin_login/signup.jinja2',
        title='Create an Account',
        form=form,
        template='signup-page',
        body="Sign up for a user."
    )


@ auth_bp.route('/admin-dir/hideshar/dashboard', methods=['GET', 'POST'])
@ login_required
def load_dashboard():
    return "This is the dashboard for now."


@
    # Vulns summary:

    # 1). "Password Cracking" with wordlist

    # 2). Exploit a misconfigured JWT token

    # 3). Sudo local priv escalation.

    # add hint wordlist

    # john.
