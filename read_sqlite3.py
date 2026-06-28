import sqlite3

connection = sqlite3.connect("student_1.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

data = cursor.fetchall()

for row in data:
    print(row)



## print(data)

connection.close()
