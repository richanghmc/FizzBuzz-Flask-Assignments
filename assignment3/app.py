from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def introduction():
    title = "Favorite foods"
    name = "Richard"
    age = 19
    message = "I am excited to learn Flask!"
    listOfFavoriteFoods = ["ice cream", "popcorn chicken", "sushi"]
    return render_template('home.html', title = title, name = name, age = age, message = message, foods = listOfFavoriteFoods)

@app.route('/drinks')
def introductionWithDrinks():
    title = "Favorite drinks"
    name = "Richard"
    age = 19
    message = "I am excited to learn Flask!"
    favoriteDrinks = ["green tea", "water", "milk tea"]
    return render_template('drinks.html', title = title, name = name, age = age, message = message, drinks = favoriteDrinks)