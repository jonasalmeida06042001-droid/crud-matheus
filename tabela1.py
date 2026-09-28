import sqlite3

con = sqlite3.connect('crud.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS COUNTRY (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, POPULATION INTEGER NOT NULL, AREA REAL NOT NULL)''')

users = [
    ('Brazil', 211000000, 8515767.0),
    ('Argentina', 44938712, 2780400.0),
    ('Chile', 18720000, 756102.0)
]

cur.executemany("INSERT OR IGNORE INTO COUNTRY (name, POPULATION, AREA) VALUES (?, ?, ?)", users)
con.commit()
con.close()