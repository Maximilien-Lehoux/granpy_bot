from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/about')
def about():
    return "his is the about page"




