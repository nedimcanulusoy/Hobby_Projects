import sqlite3


def show_all():
    con = sqlite3.connect('customer.db')
    c = con.cursor()

    c.execute('SELECT rowid, * FROM customers')
    items = c.fetchall()

    for item in items:
        print(item)

    con.commit()
    con.close()


def add_one(first, last, email):
    con = sqlite3.connect('customer.db')
    c = con.cursor()

    c.execute("INSERT INTO customers VALUES(?,?,?)", (first, last, email))

    con.commit()
    con.close()


def delete_one(row_id):
    con = sqlite3.connect('customer.db')
    c = con.cursor()

    c.execute("DELETE FROM customers WHERE rowid = (?)", row_id)

    con.commit()
    con.close()


def add_many(list):
    con = sqlite3.connect('customer.db')
    c = con.cursor()

    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    con.commit()
    con.close()


def find_email(email):
    con = sqlite3.connect('customer.db')
    c = con.cursor()

    c.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,))

    items = c.fetchall()

    for item in items:
        print(item)

    con.commit()
    con.close()
