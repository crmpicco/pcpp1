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

## Logging
The [logging](https://docs.python.org/3/library/logging.html) module is used to log messages from a program. It is useful for debugging and tracking the execution of a program. The logging module provides a way to configure different log levels, such as `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

`LogRecord` - an object that holds all the metadata about the logging event (level, filename, line number etc.)

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

logger.debug("Let's generate some fixtures for the new season!")

log_record = logging.LogRecord(
    name='crmpicco_logger',
    level=logging.DEBUG,
    pathname='generate_fixtures.py',
    lineno=10,
    msg='This is a custom log message',
    args=None,
    exc_info=None
)

# you can access the log message from the LogRecord using the msg attribute
log_message = log_record.msg
```
