# from bs4 import BeautifulSoup
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
#   Secret key for changes on the DB
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
        if not product_name:
            flash('Product Name is required!')
        else:
            conn = get_db_connection()
            search_result = conn.execute(f"""
                SELECT  product_name, product_price 
                FROM products WHERE product_name LIKE '{product_name}%' """).fetchall()
 #------------------------------------------------------------------------------------------------------  
 #   Not found message
 #------------------------------------------------------------------------------------------------------         
            if search_result == []:
                product_not_finded_html = """ 
                <html>
                  <head>
                  </head>
                  <body style="background: #00CED1;">
                    <h1 style="color:#696969;
                    font-family:Impact; margin: 250px 150px 250px; border-style: solid;
                    ">
                        The product not found, sorry.
                    </h1>
                  </body>
                </html>
                """
                return product_not_finded_html
#------------------------------------------------------------------------------------------------------  
 #   Result message
#------------------------------------------------------------------------------------------------------            
            name = search_result[0][0]
            price = search_result[0][1] 
            
            result_message = f"This is your product: {name}  <br> Price: {price} ₪ "    
            
            conn.commit()
            conn.close()
            html_result = """
                <html>
                  <head>
                  </head>
                  <body style="background: #00CED1;">
                    <h1 style="color:#696969;
                    font-family:Impact; margin: 250px 150px 250px; border-style: solid;
                    "> 
                    {result_message}
                    </h1>
                    <h2 style="color:#696969;font-family:Impact;">Thank you! See you soon</h2>
                  </body>
                </html>
                """.format(name=name, price=price, result_message=result_message)
            return html_result
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
			conn.execute("""INSERT INTO products (product_name, product_price) 
                VALUES (?, ?)""",(product_name, product_price))
			conn.commit()
			conn.close()
			return redirect(url_for('search'))
	return render_template('add.html')


#------------------------------------------------------------------------------------------------------
#  Thank you, created by Andrey Gering
#------------------------------------------------------------------------------------------------------














