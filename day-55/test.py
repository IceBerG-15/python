from flask import Flask

app = Flask(__name__)

# custom decorators
def make_bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper

def make_italic(func):
    def wrapper():
        return f'<i>{func()}</i>'
    return wrapper

def make_underlined(func):
    def wrapper():
        return f'<u>{func()}</u>'
    return wrapper


@app.route("/")
@make_bold
@make_italic
@make_underlined
def hello_world():
    return '<h1 style="color:red">Hello, World!</h1>'

@app.route("/username/<name>/<int:age>")
def greet(name,age):
    return f'<h1 style="color:red">Hello {name}</h1>' \
            f'<h1 style="text-align:center">You are {age} years old.</h1>'

if __name__ == '__main__':
    app.run(debug=True)