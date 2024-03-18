from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="color:red">Hello, World!</h1>'

@app.route("/<name>")
def greetings(name):
    return f'Hello {name}. Welcome to our number guess game. ' \
        f' To start the game, enter /game in the url bar.'

NUM = random.randint(1, 10) # random number generator

@app.route("/game/<int:num>")
def game(num):
    if num==NUM:
        return '<h1 style="color:red">Congrats u got the correct answer.</h1>'
    elif num>NUM:
        return '<h1 style="color:red">Your guess is too high.</h1>'
    else:
        return '<h1 style="color:red">Your guess is too low.</h1>'


if __name__ == '__main__':
    app.run(debug=True)
    