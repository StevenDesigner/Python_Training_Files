# create_tables.py
import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')
conn.commit()
conn.close()

print("Table created successfully.")
