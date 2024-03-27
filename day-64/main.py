from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os
# loading dotenv file
load_dotenv('day-64/file.env')
TMDB = os.getenv('API_KEY')   # getting the api key
TMBD_BEARER = f'Bearer {os.getenv('TMBD_BEARER')}'
TMBD_URL = 'https://api.themoviedb.org/3/search/movie/'
TMDB_IMG_URL = 'https://image.tmdb.org/t/p/original/'
headers = {
        "accept": "application/json",
        "Authorization": TMBD_BEARER
        }

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id:     Mapped[int] = mapped_column(Integer, primary_key=True)
    title:  Mapped[str] = mapped_column(String, nullable=False, unique=True)
    year:   Mapped[str] = mapped_column(String,nullable=False)
    desc:   Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float,nullable=True)
    ranking:Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String, nullable=True)
    img_url:Mapped[str] = mapped_column(String, nullable=False)

with app.app_context():
    db.create_all()

# -----------------------------------------------------
# adding a new movie
# with app.app_context(): 
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         desc="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         desc="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(second_movie)
#     db.session.commit()
# -------------------------------------------------------

# rating edit form
class ratingForm(FlaskForm):
    rating = StringField('Your rating out of 10 eg. 7.6')
    review = StringField('Your review')
    submit = SubmitField('Submit')

# adding movie form
class addingForm(FlaskForm):
    title = StringField('Enter movie title')
    submit = SubmitField('Submit')

# home route
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars()
    return render_template("index.html",all_movies = all_movies)

# review edit route
@app.route("/edit",methods=["GET", "POST"])
def edit():
    form = ratingForm()
    id = request.args.get('id')
    movie = db.get_or_404(Movie,id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html",form=form,movie=movie)

# movie delete route
@app.route("/delete",methods=["GET", "POST"])
def delete():
    id = request.args.get('id')
    movie = db.get_or_404(Movie,id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

# movie add route
@app.route("/add",methods=["GET", "POST"])   #,dnsNameservers= '8.8.8.8'
def add():
    form = addingForm()
    if form.validate_on_submit():
        response = requests.get(url=TMBD_URL,params={'query':form.title.data},headers=headers)
        results = response.json()['results']
        return render_template('select.html', movies = results)
    return render_template("add.html",form=form)

# finding movie
@app.route("/find",methods=["GET", "POST"])
def find():
    id = request.args.get('id')
    url = TMBD_URL+f'{id}'
    response = requests.get(url=url,headers=headers)
    data = response.json()
    movie = Movie(
        id = id,
        title = data['title'],
        year = data['release_date'].split('-')[0],
        desc = data['overview'],
        img_url = f'{TMDB_IMG_URL}{data['poster_path']}'
    )
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('edit',id=id))

if __name__ == '__main__':
    app.run(debug=True)
