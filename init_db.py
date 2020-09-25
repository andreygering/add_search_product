import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO products (product_name, product_price) VALUES (?, ?)",
            ('AirPods 2', 1230)
            )

cur.execute("INSERT INTO products (product_name, product_price) VALUES (?, ?)",
            ('Samsung Galaxy 10', 4350)
            )

connection.commit()
connection.close()