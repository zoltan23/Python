import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows


insert('water glass', 10, 8.00)


print(view())