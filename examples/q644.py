import logging

logging.basicConfig(format='%(asctime)s [%(levelname)s] [%(threadName)s] [PID:%(process)d] - %(message)s', level=logging.INFO)
logger = logging.getLogger()
logger.info('This is a log message with thread name and process ID')
