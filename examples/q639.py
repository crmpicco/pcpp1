import configparser


config = configparser.ConfigParser()

config['DEFAULT'] = {'website': 'example.com', 'port': '80'}
config['development'] = {'port': '8080'}
config['production'] = {'port': '443', 'ssl': 'True'}

print(config['development']['website'])   
print(config['production']['website'])    
print(config['development']['port'])      
print(config['production']['port'])    
