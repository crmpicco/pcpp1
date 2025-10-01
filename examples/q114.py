# This code will raise error
"""
import json
x = {"apple","banana","cherry"}
y = json.dumps(x)
print(y)
"""
# it will raise: TypeError: Object of type set is not JSON serializable

# This code will not raise error

import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(42))

#Output will be:

#{"name": "John", "age": 30}
#["apple", "bananas"]
#42
