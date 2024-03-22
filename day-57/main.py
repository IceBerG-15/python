from flask import Flask, render_template
import random
from datetime import datetime
import requests 

app = Flask(__name__)

@app.route("/")
def hello_world():
    randNum = random.randint(20,100)
    year = datetime.now().year
    return render_template("index.html",num=randNum,year=year)

@app.route("/guess/<name>")
def guess(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    gender = response.json()['gender']
    response = requests.get(f'https://api.agify.io?name={name}')
    age = response.json()['age']
    return render_template("guess.html",name=name,gender=gender,age=age)

if __name__ == "__main__":
    app.run(debug=True)