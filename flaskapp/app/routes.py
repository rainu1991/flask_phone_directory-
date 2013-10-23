import sqlite3
from functools import wraps
from flask import Flask, render_template, request, flash
from flask import *
from functools import wraps

DATABASE = 'tes.db'                                           #Database name

 
app = Flask(__name__)                                         #Create an instance of this class 

app.config.from_object(__name__)
 
app.secret_key = 'development key' 

def connect_db():                                             #Database connection 
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/')                                               # maps the URL / to a Python function home
def home():
  g.db=connect_db()	
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  g.db=connect_db()
  return render_template('contact.html')
 

@app.route('/post',methods=['POST'])                         #Function for posting data into database
def add_entry():
	g.db=connect_db()
	g.db.execute('insert into posts (title, text, phone) values (?, ?, ?)',[request.form['title'], request.form['text'],         		request.form['phone']])
	g.db.commit()
	g.db.close()
	return redirect(url_for('show_entries'))

@app.route('/post')                                           #Retrieve data from database
def show_entries():
	g.db=connect_db()
	cur = g.db.execute('select title, text, phone from posts order by id desc')
	posts = [dict(title=row[0], text=row[1], phone=row[2]) for row in cur.fetchall()]
	g.db.close()
	return render_template('post.html',posts=posts)

if __name__ == '__main__':
  app.run(debug=True)                                         #run() function to run our Server.
