import json
json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_object = json.loads(json_string)
print(python_object["name"])  
print(python_object["age"])   
print(python_object["city"]) 
