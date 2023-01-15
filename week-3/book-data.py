import sqlite3

booklib=sqlite3.connect("ass5\Booklib.db")
book=booklib.cursor()
z=0
z=int(input("Creating new database.....Press 1 if already created!"))
if z==0:
    book.execute('''CREATE TABLE books(
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    price REAL);''')
    z==1
x="y"
while x=="y":
    b_id=int(input("Enter Book ID: "))
    t=(input("Enter Title: "))
    a=(input("Enter Author: "))
    p=float(input("Enter Price: "))

    book.execute('''INSERT INTO books(book_id,title,author,price)VALUES(?,?,?,?);''',(b_id,t,a,p))
    x=input("Enter another book to library? (y/n) : ")
booklib.commit()

booklib.close()
