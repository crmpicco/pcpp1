# Network Programming

To parse a JSON string into a Python object, use the `json.loads()` method from the `json` module.
```python
import json
customer_info = '{"name": "Craig", "age": 41, "city": "Rockingham"}'
customer = json.loads(customer_info)
```

To convert Python data types into JSON data, use the `json.dumps()` method.
```python
import json
club = {"club": "Rangers", "year_founded": 1872, "city": "Glasgow"}
club_info = json.dumps(club)
```