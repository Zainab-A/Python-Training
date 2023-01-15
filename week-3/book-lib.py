import sqlite3

booklib=sqlite3.connect("Booklib.db")
book=booklib.cursor()

x="y"
amount=0.00
while x=="y":
    t=(input("Book Title: "))

    book.execute('''SELECT * from books WHERE title==?''',(t,))
    mybook=book.fetchall()
    for bk in mybook:
        print(bk)
    book.execute('''SELECT price from books WHERE title==?''',(t,))
    myprice=book.fetchall()
    for prc in myprice:
        price=prc[0]
    cpy=int(input("Enter No. of Copies: "))
    amount=amount+(cpy*price)
    x=input("Add more books? (y/n) : ")

print("Total Cost: ",(amount))
booklib.close()