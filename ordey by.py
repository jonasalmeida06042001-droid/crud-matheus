import sqlite3

con = sqlite3.connect('crud.db')
cur = con.cursor()
cur.execute("SELECT name_city FROM CITY ORDER BY RATING ASC")

cities = cur.fetchall()
for city in cities:
    print(city)

con.close()
