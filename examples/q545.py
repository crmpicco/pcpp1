import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'host': 'localhost', 'env': 'dev'}
config['mysql'] = {'host': 'localhost', 'env': 'prod'}
config['postgresql'] = {}
print(config['mysql']['env'])
print(config['postgresql']['env'])
