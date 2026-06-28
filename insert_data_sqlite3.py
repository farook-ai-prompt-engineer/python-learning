import sqlite3

connection = sqlite3.connect("student_1.db")
cursor = connection.cursor()




cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        ("Farook",25)
        )


connection.commit()
connection.close()

