import sqlite3

db = sqlite3.connect('books.db') #initialising the database and connecting it
cursor = db.cursor() #cursor for moving up and won the db
# cursor.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title VARCHAR(20) NOT NULL UNIQUE, author VARCHAR(20) NOT NULL , rating FLOAT NOT NULL)')
cursor.execute("INSERT INTO books (id, title, author, rating) VALUES(1,'One Piece','ODA',10)")
db.commit()