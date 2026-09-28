import sqlite3

con = sqlite3.connect('crud.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS CITY (id_city INTEGER PRIMARY KEY AUTOINCREMENT, name_city TEXT NOT NULL, population_city INTEGER, rating REAL NOT NULL)''')

users = [
    ('São Paulo', 12300000, 8.5),('Buenos Aires', 2890000, 7.8),('Santiago', 5740000, 8.0)
]
cur.executemany("INSERT OR IGNORE INTO CITY (name_city, population_city, rating) VALUES (?, ?, ?)", users)
con.commit()
con.close()