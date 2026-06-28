import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()



cursor.execute(
        "SELECT * FROM students WHERE age > ?",
        (26,)
        )
print(cursor.fetchall())

connection.close()

