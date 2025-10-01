import shelve
with shelve.open('data') as db:
    db['name'] = 'John'
    db['age'] = 30
    db['city'] = 'New York'
print(db)
with shelve.open('data') as db:
    name = db['name']
    age = db['age']
    city = db['city']
print(db)
print(name, age, city)  
