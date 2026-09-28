import sqlite3

con = sqlite3.connect('crud.db')
cur = con.cursor()
cur.execute("SELECT id_city, name_city FROM CITY")

cities = cur.fetchall()
for city in cities:
    print(city) 

con.close()