import sqlite3
import os 
print(os.path.abspath("students.db"))
conn = sqlite3.connect("students.db")
cursor= conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER,
               grade REAL
)
""")

conn.commit()
conn.close()
print("Database created!")