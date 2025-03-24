# Network Programming

To parse a JSON string into a Python object, use the `json.loads()` method from the `json` module.
```python
import json
customer_info = '{"name": "Craig", "age": 41, "city": "Rockingham"}'
customer = json.loads(customer_info)
```