import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.WARNING)
logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')
