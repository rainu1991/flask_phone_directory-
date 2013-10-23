import sqlite3 as lite
import sys
con=lite.connect("tes.db")       #connect to the tes.db database.connect() method returns a connection object
with con:
	cur=con.cursor()          
	cur.execute("DROP TABLE IF EXISTS posts")
	cur.execute("CREATE TABLE posts(id integer primary key autoincrement,title TEXT,text TEXT,phone INT)")

