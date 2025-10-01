import sqlite3

# Connect to a SQLite database
connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()

# Create the "employees" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        name TEXT,
        age INTEGER
    )
''')
connection.commit()

# Insert sample data into the "employees" table
sample_data = [
    ('Alice', 25),
    ('Bob', 30),
    ('Charlie', 28)
]
cursor.executemany('INSERT INTO employees (name, age) VALUES (?, ?)', sample_data)
connection.commit()

# Execute a SELECT query
cursor.execute('SELECT name, age FROM employees')

# Fetch all the rows of the query result
result = cursor.fetchall()

# Print the fetched data
for row in result:
    print(row)

# Close the cursor and the connection
cursor.close()
connection.close()
