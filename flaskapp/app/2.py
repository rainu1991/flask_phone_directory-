import sqlite3 as lite
import sys


con = lite.connect('tes.db')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM posts")

    rows = cur.fetchall()

    for row in rows:
        print row
