import sqlite3
con = sqlite3.connect("mydatabase.db")
cur = con.cursor()
cur.execute("create table if not exists students(name varchar(50),password varchar(50))")
cur.execute('insert into students values("rani","abc")')
cur.execute('insert into students values("raj","1234")')
cur.execute('insert into students values("ramesh","pqr")')
cur.execute('insert into students values("suresh","789")')
con.commit()
