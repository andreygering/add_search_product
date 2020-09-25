from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort
#------------------------------------------------------------------------------------------------------
#   Connection to DB (sqlite3)
#------------------------------------------------------------------------------------------------------
def get_db_connection():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    return conn
#------------------------------------------------------------------------------------------------------
#   Secret eky for changes on the DB
#------------------------------------------------------------------------------------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = "SwCm6J'm$kTKCSE6"

#------------------------------------------------------------------------------------------------------
#   Function for search product on the DB redirect from page search to result (render the page, connect 
#   to DBb and search/select  row on the DB by user input )
#------------------------------------------------------------------------------------------------------
@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        product_name = request.form['product_name']
        product_price = request.form['product_price']
        if not product_name:
            flash('Product Name is required!')
        else:
            conn = get_db_connection()
            search_result = conn.execute('SELECT * FROM products WHERE product_name IS (?) OR product_price IS (?)',(product_name, product_price)).fetchall()
            finish_search = ", ".join( repr(e) for e in search_result)
            conn.commit()
            conn.close()
            return finish_search
    return render_template('search.html')

#------------------------------------------------------------------------------------------------------
#   Function for add new product to DB ( render the page, connect to DB and create new row on the DB )
#------------------------------------------------------------------------------------------------------

@app.route('/', methods=('GET', 'POST'))
def add():
	if request.method == 'POST':
		product_name = request.form['product_name']
		product_price = request.form['product_price']
		if not product_name:
			flash('Product Name is required!')
		else:
			conn = get_db_connection()
			conn.execute('INSERT INTO products (product_name, product_price) VALUES (?, ?)',(product_name, product_price))
			conn.commit()
			conn.close()
			return redirect(url_for('search'))
	return render_template('add.html')

















