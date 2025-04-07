# Advanced Object-Oriented Programming

`__le__` - this method is used to implement less than or equal to comparisons. It should return `True` if the object is less than or equal to the other object, `False` otherwise.

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

:duck: Duck typing - this is a type of polymorphism (i.e. "many forms") and allows objects of different types to be used interchangeably as long as they implement the same methods. Duck typing relies heavily on **dynamic typing**.
```python
class Car:
    def start_engine(self):
        print("Car engine started")

class LawnMower:
    def start_engine(self):
        print("Lawn mower engine started")

def ignite(machine):
    machine.start_engine()  # this doesn't care what type 'machine' is

ignite(Car())
ignite(LawnMower())
```