import sqlite3

con = sqlite3.connect('crud.db')
cur = con.cursor()
cur.execute("SELECT  co.name, ci.name_city FROM CITY AS ci JOIN COUNTRY AS co ON ci.id_city = co.id")
cities = cur.fetchall()
for city in cities:
    print(city)
con.close()