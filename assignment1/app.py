from flask import Flask, render_template
from datetime import *
app = Flask(__name__)

@app.route('/')
def introduction():
    title = "Flask Introduction"
    name = "Richard"
    age = 19
    message = "I am excited to learn Flask!"
    date = datetime.today()
    return render_template('home.html', title = title, name = name, age = age, message = message, date = date)
