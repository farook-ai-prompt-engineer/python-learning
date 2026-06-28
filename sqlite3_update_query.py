import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()



cursor.execute(
        "UPDATE students SET age=? WHERE name=?",
        (26, "Farook")
        )



connection.commit()
connection.close()

