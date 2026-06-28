import sqlite3


connection = sqlite3.connect("student.db")

cursor = connection.cursor()




cursor.execute(
        "DELETE FROM students WHERE name=?",
        ("kumar",)
        )


connection.commit()
connection.close()

