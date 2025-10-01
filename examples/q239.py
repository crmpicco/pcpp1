import logging

# Define a custom handler by subclassing logging.Handler
class MyCustomHandler(logging.Handler):
    def emit(self, record):
        # Define how the log record should be handled
        msg = self.format(record)
        print("Custom Handler:", msg)

# Create a logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create an instance of your custom handler
custom_handler = MyCustomHandler()

# Set the handler's log level
custom_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
custom_handler.setFormatter(formatter)

# Add the custom handler to the logger
logger.addHandler(custom_handler)

# Log messages using the custom handler
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
