from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def introduction():
    title = "Flask Introduction"
    name = "Richard"
    age = 19
    message = "I am excited to learn Flask!"
    return render_template('home.html', title = title, name = name, age = age, message = message)