import sqlite3

connection = sqlite3.connect("student_1.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

connection.commit()
connection.close()
