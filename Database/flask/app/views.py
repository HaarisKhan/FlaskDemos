from app import app

from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return 'Welcome to BookFace!'

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		flash("Login requested for OPENID=%s, remember_me=%s" % (form.openid.data, str(form.remember_me.data)))

		return redirect('/index')

	return render_template('login.html', title = 'Sign In', form = form, providers = app.config['OPENID_PROVIDERS'])