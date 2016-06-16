from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'jane'},
            'body': 'It is a great day for sailing!'
        },
        {
            'author': {'nickname': 'roberto'},
            'body': 'No habla Español'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)