import sqlite3

conn = sqlite3.connect('mydb.sqlite')
cursor = conn.cursor()

# Delete data
cursor.execute("DELETE FROM employees WHERE name = ?", ('Alice',))

conn.commit()
conn.close()
