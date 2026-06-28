import sqlite3


connection = sqlite3.connect("student_1.db")

cursor = connection.cursor()




cursor.execute(
        "DELETE FROM students WHERE name=?",
        ("Farook",)
        )


connection.commit()
connection.close()

