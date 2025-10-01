import sqlite3

# Connect to a SQLite database (creates one if it doesn't exist)
conn = sqlite3.connect('my_database.db')

# Create a cursor
cursor = conn.cursor()

# SQL script containing multiple statements
sql_script = """
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

INSERT INTO students (name, age) VALUES ('Alice', 20);
INSERT INTO students (name, age) VALUES ('Bob', 22);
"""

# Execute the script
cursor.executescript(sql_script)

# Commit changes and close the connection
conn.commit()
conn.close()
