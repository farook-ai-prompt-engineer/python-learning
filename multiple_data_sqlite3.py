import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()


students = [
        ("Farook", 19,),
         ("kumar", 28),
         ("rahman", 30)
        ]

cursor.executemany(
    "INSERT INTO students VALUES (?, ?)",
    students
    )


connection.commit()
connection.close()

