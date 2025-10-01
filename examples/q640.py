import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    grade TEXT
                )''')
student_data = [
    ('Alice', 20, 'A'),
    ('Bob', 22, 'B'),
    ('Charlie', 19, 'C')
]
cursor.executemany('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', student_data)
cursor.executemany('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', student_data)
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()
