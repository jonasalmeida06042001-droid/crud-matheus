''' jonas Pinheiro de Almeida
    27/08/2026
    Banco de dados
'''

import sqlite3

con = sqlite3.connect('crud.db')
cur = con.cursor()
cur.execute("SELECT name_city as name_city FROM CITY")
cities = cur.fetchall()
for city in cities:
    print(city)
con.close()