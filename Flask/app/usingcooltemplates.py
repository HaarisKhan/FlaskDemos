from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Haaris'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Kevin'}, 
            'body': 'HackFam is a great team!' 
        },
        { 
            'author': {'nickname': 'Kars'}, 
            'body': 'Finals are killin me #sendhalp' 
        }
    ]
    return render_template("betterindex.html",
                           title='Home',
                           user=user,
                           posts=posts)
