# File Processing and Communicating with a Program's Environment

## sqllite3
The sqllite3 module provides a lightweight disk-based database that doesn't require a separate server process and allows access to the database using a nonstandard variant of the SQL query language. It is included in Python's standard library.

### Methods
`executescript()` - executes multiple SQL statements at once. It is useful for executing a batch of SQL commands in a single call.
```python
import sqlite3

# connect to a SQLite database (creates one if it doesn't exist)
conn = sqlite3.connect('prowrestling.db')
 
cursor = conn.cursor()
 
# SQL script containing multiple statements
sql_script = """
CREATE TABLE promoters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
 
INSERT INTO promoters (name, age) VALUES ('Vince K. McMahon', 73);
INSERT INTO promoters (name, age) VALUES ('Antonio Inoki', 68);
"""
 
cursor.executescript(sql_script)
 
# commit changes and close the connection
conn.commit()
conn.close()
```