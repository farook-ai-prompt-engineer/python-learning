import sqlite3

connection = sqlite3.connect("student_1.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

data = cursor.fetchall()

print("ID\tNAME\tAGE")
print("-" * 25)

for row in data:
    print(f"{row[0]}\t{row[1]}\t{row[2]}")

connection.close()
