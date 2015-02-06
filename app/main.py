import sys

from flask import Flask, render_template, redirect, url_for
from flask.ext.script import Manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd'
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    db.create_all()

    manager = Manager(app)
    manager.run()
