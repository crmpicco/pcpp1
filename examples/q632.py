class MyClass:
    """
    docstrings1
    """

    def __init__(self, name):
        self.name = name

    def greet(self):
        """
        docstrings2
        """
        print(f"Hello, {self.name}!")
obj = MyClass("Alice")
print(obj.greet.__doc__)
