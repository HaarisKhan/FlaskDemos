from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Haaris'}
	return render_template('index.html', title = 'Home', user = user, item = "memes")
	# render_template invokes Jinja2 templates that we learned before
	# Substitutes the {{ ... }} blocks in index.html with necessary info
	# Just pass them as variables