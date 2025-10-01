import sqlite3

# Create a connection to the database
conn = sqlite3.connect("mydb.sqlite")

# Create a cursor
cursor = conn.cursor()

# SQL query for inserting data
insert_query = "INSERT INTO students (id, name, age) VALUES (?, ?, ?)"

# Data to be inserted
data = (1, "John Doe", 25)

# Execute the INSERT query with data
cursor.execute(insert_query, data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
