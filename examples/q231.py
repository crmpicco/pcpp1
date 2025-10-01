class MyClass:
    def __init__(self):
        self.x = 42
        self.y = "hello"

obj = MyClass()

print(obj.z)       # Raises AttributeError
print(obj.__dict__)   # Output: {'x': 42, 'y': 'hello'}  
