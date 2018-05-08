from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Welcome to Jonathan's Capstone Demonstration!"

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/class_schedule')
def class_schedule():
    return app.send_static_file('class_schedule.html')