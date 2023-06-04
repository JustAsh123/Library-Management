import sqlite3

con = sqlite3.connect("books.db")

cur = con.cursor()
try:
    cur.execute("CREATE TABLE books (access_code INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, publication TEXT, quantity INTEGER);")
except:
    print("...")

def add_data(title,auth,publ,qty):
    book = (title, auth, publ, qty)

    cur.execute("INSERT INTO books (title, author, publication, quantity) VALUES (?, ?, ?, ?);", book)

    con.commit()

def give_data():
    cur.execute("SELECT * FROM books")
    return cur.fetchall()

def delete(ac):
    cur.execute(f"DELETE FROM books WHERE access_code=={ac}")
    con.commit()
