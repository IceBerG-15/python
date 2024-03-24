from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# flask app
app = Flask(__name__)
# db base class
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# table creation
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    print(all_books)
    return render_template('index.html',all_books = all_books)


@app.route("/add",methods=['POST','GET'])
def add():
    if request.method == 'POST':
        new_book = Book(title = request.form['title'],author=request.form['author'],rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<id>",methods=['POST','GET'])
def edit(id):
    selected_book = db.get_or_404(Book,id)
    if request.method == 'POST':
        selected_book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',book=selected_book)

@app.route("/delete/<id>")
def delete(id):
    selected_book = db.get_or_404(Book,id)
    db.session.delete(selected_book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

