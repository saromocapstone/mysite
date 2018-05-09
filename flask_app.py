import constants

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/class_schedule')
def class_schedule():
    return render_template('class_schedule.html',
                            courses = constants.COURSES)

@app.route('/demonstration')
def demonstration():
    return app.send_static_file('demonstration.html')
