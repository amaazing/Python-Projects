'''
Author: Maaz
A number generator website, Guess the number!
'''

from flask import Flask
from random import randint

app = Flask(__name__)

number = randint(0,9)
    
    
@app.route('/')
def home():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"display: block; margin-left: auto; margin-right: auto; width: 50%>'

@app.route('/<int:number_chosen>')
def greet(number_chosen):
    if number_chosen > number:
        return f"<h1 style='color:red'>Too high!</h1>"
    
    elif number_chosen < number:
        return f"<h1 style='color:blue'>Too low!</h1>"
    
    else:
        return f"<h1 style='color:green'>Correct! The number was {number}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)