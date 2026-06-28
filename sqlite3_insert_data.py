import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()




cursor.execute(
        "INSERT INTO students VALUES (?, ?)",
        ("Farook",25)
        )


connection.commit()
connection.close()

