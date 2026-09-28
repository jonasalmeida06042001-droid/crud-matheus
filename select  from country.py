import sqlite3

con = sqlite3.connect('crud.db')
cur = con.cursor()
cur.execute("SELECT * FROM COUNTRY")

rows = cur.fetchall()
for row in rows:
    print(row)

con.close()