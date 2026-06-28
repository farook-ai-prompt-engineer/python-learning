import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

data = cursor.fetchall()

print(data)

connection.close()
