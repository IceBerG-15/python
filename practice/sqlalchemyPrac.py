from sqlalchemy import Integer, String, FLOAT
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

app = Flask(__name__)
## create database
class base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'
#create extension
db = SQLAlchemy(model_class=base)
# intialize the app with extension
db.init_app(app)

## create table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(FLOAT, nullable=False)
    
    # def __repr__(self):
    #     return f"<Book {self.title}>"

with app.app_context():
    db.create_all()
# new record entry
with app.app_context():
    new_book = Book(id=1,title='One Piece',author='ODA',rating=9.9)
    db.session.add(new_book)
    db.session.commit()
# reading records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
# updating record
with app.app_context():
    record = db.session.execute(db.select(Book).where(Book.id==1)).scalar()
    record.title='Attack On Titan'
    db.session.commit()
# record deletion
with app.app_context():
    record = db.session.execute(db.select(Book).where(Book.id==1)).scalar()
    db.session.delete(record)
    db.session.commit()