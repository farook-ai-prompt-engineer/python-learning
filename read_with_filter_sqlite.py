import sqlite3

connection = sqlite3.connect("student_1.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

data = cursor.fetchall()

print(f"{'ID':<5}{'NAME':<15}{'AGE':<5}")
print("-" * 25)

for row in data:
    print(f"{row[0]:<5}{row[1]:<15}{row[2]:<5}")

connection.close()
