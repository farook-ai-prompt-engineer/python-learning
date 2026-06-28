import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE students (
                    name TEXT,
                    age INTEGER
                )
                """)

connection.commit()
connection.close()

