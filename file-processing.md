# File Processing and Communicating with a Program's Environment

## sqllite3
The sqllite3 module provides a lightweight disk-based database that doesn't require a separate server process and allows access to the database using a nonstandard variant of the SQL query language. It is included in Python's standard library.

### Methods
`executescript()` - executes multiple SQL statements at once. It is useful for executing a batch of SQL commands in a single call.
```python
import sqlite3

# connect to an SQLite database (creates one if it doesn't exist)
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
 
# save all changes made in the current transaction to the database
conn.commit()
# ...and close the connection
conn.close()
```

## Logging
The [logging](https://docs.python.org/3/library/logging.html) module is used to log messages from a program. It is useful for debugging and tracking the execution of a program. The logging module provides a way to configure different log levels, such as `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

`LogRecord` - an object that holds all the metadata about the logging event (level, filename, line number, etc.)

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

`basicConfig()` - used to configure the logging module. It sets the default log level and the format of the log messages. If you don't specify a level, then it will be set to `WARNING` by default.

```python
import logging
logging.basicConfig()

app_logger = logging.getLogger()
app_logger.critical('CRITICAL - fix urgently!')
# CRITICAL:root:CRITICAL - fix urgently!

app_logger.error('ERROR - fix this!')
# ERROR:root:ERROR - fix this!

app_logger.warning('WARNING - something is not right')
# WARNING:root:WARNING - something is not right

# the following log lines are not displayed because the default log level is WARNING
app_logger.info('INFO')
app_logger.debug('DEBUG')
```

A typical use of `LogRecord` when using threads:

```python
logging.basicConfig(format='%(asctime)s [%(levelname)s] [%(threadName)s] [PID:%(process)d] - %(message)s', level=logging.INFO)
```

## csv
The `csv` module provides functionality to read and write CSV (Comma-Separated Values) files. It is part of Python's standard library.

### Writing
`csv.writer()` - creates a writer object that can write data to a CSV file. If you do not explicitly define the quoting parameter the default is `quoting=csv.QUOTE_MINIMAL`, which means that only fields containing special characters (like commas or quotes) will be quoted.