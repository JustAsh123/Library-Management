import sqlite3

reg = sqlite3.connect("register.db")
book = sqlite3.connect("books.db")

Rcur = reg.cursor()
Bcur = book.cursor()

try:
    Rcur.execute("CREATE TABLE register(date TEXT,access_code INT,s_id INT,s_name TEXT)")
    reg.commit()
except:
    pass

def register_issue(date,ac,s_id,s_name):
    data = [date,ac,s_id,s_name]
    #Rcur.execute("INSERT INTO register (date, access_code, s_id, s_name) VALUES (?, ?, ?, ?);", data)

    #reg.commit()
    Bcur.execute(f"SELECT * FROM books WHERE access_code = {ac}")
    data = Bcur.fetchall()
    print(data)
    qty = data[0][4]
    Bcur.execute(f"UPDATE books SET quantity = {qty-1} WHERE access_code = {ac}")
    book.commit()
