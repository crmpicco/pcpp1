# Advanced Object-Oriented Programming

## Assorted methods
Magic methods - begin and end with double underscores. They are also known as dunder (**d**ouble **under**score) methods.

`__le__` - this method is used to implement less than or equal to comparisons. It should return `True` if the object is less than or equal to the other object, `False` otherwise.

`__repr()__` - used to return an information-rich string representation of the object. This is useful for debugging and logging purposes. The string returned by `__repr__()` should be a valid Python expression that can be used to recreate the object e.g.
```python
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Player(name={self.name!r}, age={self.age!r})"

player = Player("James Tavernier", 33)
print(repr(player))  # Player(name='James Tavernier', age=33)
```
## Assorted attributes
`__dict__` - this attribute is a dictionary that contains the object's attributes and their values. It is useful for debugging and introspection purposes. You can use it to see all the attributes of an object and their values.
```python
class Performer:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

performer = Performer("John Cena", 251)

print(performer.__dict__)
# {'name': 'John Cena', 'weight': 251}
```
`from abc import ABC, abstractmethod` - the `abc` module provides the `ABC` class that can be used to create abstract base classes. Abstract base classes are classes that are designed to be inherited from, but not instantiated. Abstract methods are methods that must be implemented by any concrete subclasses.

`@abstractmethod` - this decorator is used to mark a method as abstract. Abstract methods must be implemented by any concrete subclasses.

`__add__()` - this method is used to implement addition as Python doesn't know how to perform addition between objects by default. It should return the result of adding the two objects together, e.g.
```python
class Match:
    def __init__(self, rating):
        self.rating = rating

    def __add__(self, other):
        return Match(self.rating + other.rating)

match1 = Match(4)
match2 = Match(5)
match3 = match1 + match2
print(match3.rating)
```

### :duck: Duck typing
This is a type of polymorphism (i.e. "many forms") and allows objects of different types to be used interchangeably as long as they implement the same methods. Duck typing relies heavily on **dynamic typing**. Duck typing focuses on an object's _behaviour_ rather than its class or explicit type. If two different classes have a `start_engine()` method then they can both be used as if they are "machines" because the calling code only cares that the `start_engine()` method exists.
```python
class Car:
    @staticmethod
    def start_engine():
        print("Car engine started")

class LawnMower:
    @staticmethod
    def start_engine():
        print("Lawn mower engine started")

def ignite(machine):
    machine.start_engine()  # this doesn't care what type 'machine' is

ignite(Car())
ignite(LawnMower())
```

`isinstance()` is used to check if an object is an instance of a specific class or its subclasses

`issubclass()` is used to check if a class is a subclass of another class. Works with classes **only**

#### Subclassing
By subclassing the built-ins in Python, you can modify only the parts that you intend to modify, while all remaining parts behave as good old built-ins.

## Encapsulation
One of the fundamental principles of OOP. This is the concept of restricting access to certain parts of an object. In Python, this is done using private and protected attributes. 
### Private attributes 
Prefixed with a double underscore `__` and are not accessible from outside the class. 
### Protected attributes 
Prefixed with a single underscore `_` and are intended to be used only within the class and its subclasses.

Class attributes are public by default

## Inheritance
Single inheritance - a class can inherit from only one parent class. This is the most common type of inheritance in Python.

Multiple inheritance - a class can inherit from multiple parent classes. This is less common and can lead to complex class hierarchies. This can also lead to MRO (Method Resolution Order) issues which Python solves using the C3 linearisation algorithm.

## Exceptions
`__cause__` - when an exception is _explicitly chained_ using the `from` keyword, the original exception object is assigned to the `__cause__` attribute of the new exception.

Implicitly chained exceptions occur when an exception is raised inside another exception's `except` block. The new exception becomes the `__context__` of the original exception.

## [pickle](https://docs.python.org/3/library/pickle.html)
The `pickle` module is used to serialise and deserialise Python objects. The `pickle` package is a good option for serialising single Python objects into a byte stream.
```python
import pickle

class Stadium:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def greet(self):
        return f"Welcome to {self.name}. I hold {self.capacity} spectators."

stadium = Stadium("Ibrox", 51000)

# serialise the object to a file
with open("ibrox.pkl", "wb") as file:
    pickle.dump(stadium, file)

# deserialise the object from the file we just created 
with open("ibrox.pkl", "rb") as file:
    loaded_stadium = pickle.load(file)

# use the deserialised object
print(loaded_stadium.greet())
```