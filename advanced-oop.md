# Advanced Object-Oriented Programming

## Assorted methods
Magic methods - begin and end with double underscores. They are also known as dunder (**d**ouble **under**score) methods.

`__le__` - this method is used to implement less than or equal to comparisons. It should return `True` if the object is less than or equal to the other object, `False` otherwise.

`__repr()__` - used to return an information-rich string representation of the object. This is useful for debugging and logging purposes and is **developer-oriented**. The string returned by `__repr__()` should be a valid Python expression that can be used to recreate the object e.g.
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
`__str__` - used to return a human-readable string representation of the object. This is useful for displaying the object to the user and is **user-oriented**. The string returned by `__str__()` should be easy to read and understand e.g.
```python
class HouseShow:
    def __init__(self, name, attendance):
        self.name = name
        self.attendance = attendance

    def __str__(self):
        return f"{self.name} had a turnout of ${self.attendance})"

show = HouseShow("Insurrextion", 17000)
print(show) # Output: Insurrextion had a turnout of 17000
```
`__doc__` - this attribute contains the docstring of the class or function. It is used to provide documentation for the class or function
```python
"""
Comments can go in here but they will be ignored and they won't be returned by __doc__
"""
def greet(name):
    """Say hello to the given person"""
    return f"Hello, {name}!"

class Person:
    """Represents a person with a name"""    
    def __init__(self, name):
        """Initialise the person with their name"""
        self.name = name

print(greet.__doc__)  # Say hello to the given person
print(Person.__doc__)  # Represents a person with a name
print(Person.__init__.__doc__)  # Initialise the person with their name
```

`__eq__` - used to implement equality comparisons.

`is` - this operator is used to check if two objects are the same object in memory.

`__bases__` - this attribute is a tuple that contains the base classes of the class. It is useful for introspection and debugging purposes. You can use it to see the inheritance hierarchy of a class.

`type()` - this built-in function can return the type of an object. It can also be used to dynamically create a new class at runtime. For example:
```python
ProGolfer = type("ProGolfer", (GolfPlayer,), {"handicap": 0})
```

To override the accessors and mutators of a dictionary you need to use:

* `__getitem__()` - this method is used to get an item from the object using the `[]` operator. It should return the value associated with the key passed as an argument.
* `__setitem__()` - this method is used to set an item in the object using the `[]` operator. It should set the value associated with the key passed as an argument.

An example of overiding the accessors and mutators by using dictionary syntax would look like this:
```python
class Cache:
    def __init__(self):
        self.store = {}

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

cache = Cache()
cache['moodle_AU_host'] = 'hostname.com'  # uses __setitem__
print(cache['moodle_AU_host'])  # uses __getitem__
```
`__call__()` - this method is used to make an object callable like a function. It allows you to call an instance of a class as if it were a function. This is useful for creating objects that can be used as functions, e.g.
```python
class EventHandler:
    def __call__(self, event):
        print(f"Handling event: {event}")

handler = EventHandler()
handler("UserLogin")  # this works because __call__ is defined
```
`*args` - a tuple of all not explicitly expected positional arguments

`**kwargs` - a dictionary of all not explicitly expected keyword arguments.
```python
def greet(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

greet("Terry", "Jim", age=71, location="Stamford, CT")
# Positional arguments: ('Terry', 'Jim')
# Keyword arguments: {'age': 71, 'location': 'Stamford, CT'}
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

The "Pythonic" approach to retrieving a value from a dictionary if you are not sure if it will exist is using `dictionary.get('keyname')`

`from abc import ABC, abstractmethod` - the `abc` module provides the `ABC` class that can be used to create abstract base classes. Abstract base classes are classes that are designed to be inherited from, but not instantiated. Abstract methods are methods that must be implemented by any concrete subclasses.

`@abstractmethod` - this decorator is used to mark a method as abstract. Abstract methods must be implemented by any concrete subclasses. If you try to instantiate a subclass that does not implement all abstract methods then a `TypeError` will be raised, e.g.
```python
from abc import ABC, abstractmethod

class DocumentExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

class PDFExporter(DocumentExporter):
    def export(self, data):
        print(f"Exporting data to PDF: {data}")

class CSVExporter(DocumentExporter):
    pass

exporter = CSVExporter()
exporter.export("Sample Data")
```
### Magic methods
`__add__()` - this method is used to implement addition as Python doesn't know how to perform addition between objects by default. It should return the result of adding the two objects together.

`__sub__()` - used to implement subtraction
```python
class Budget:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Budget(self.amount + other.amount)

    def __sub__(self, other):
        return Budget(self.amount - other.amount)

    def __repr__(self):
        return f"Budget(${self.amount})"

january = Budget(1500)
february = Budget(1200)

total = january + february
difference = january - february

print(total)       # Budget($2700)
print(difference)  # Budget($300)
```

`__slots__` - this is a special attribute that can be used to limit the attributes that can be added to an object. It is used to save memory by preventing the creation of a `__dict__` for each instance of the class. This is useful when you have a large number of instances of a class and you want to save memory. You can define `__slots__` as a tuple or list of attribute names, e.g.
```python
class Golfer:
    __slots__ = ('name', 'handicap')  # only these attributes can be added to the object

    def __init__(self, name, handicap):
        self.name = name
        self.handicap = handicap

golfer = Golfer("Ernie Els", 0)
golfer.age = 55  # :x: this raises an AttributeError
```
`__hash__` - used to define a custom hash function for instances of a class

`__delete__` - used in descriptors to define custom behaviour when an attribute is deleted

`__del__` - this method, also known as the destructor, is called when an object is about to be destroyed. It is useful for cleaning up resources, such as closing files or releasing locks. However, it is not guaranteed to be called immediately when an object goes out of scope, so it should not be relied upon for critical resource management.

`super()` - used to call a method from a superclass. Can be used with single and multiple inheritance. Follows the MRO (Method Resolution Order) which can skip the immediate parent if multiple inheritance is in play. **Importantly, it does not always mean "direct parent".**

In this example, when `super().__init__()` is called inside `B` it goes to `C` and not the superclass `A` because of the MRO defined in `D`.
```python
class B(A):
    def __init__(self):
        super().__init__()
        
class C(A):
    def __init__(self):
        super().__init__()
        
class D(B, C):
    def __init__(self):
        super().__init__()
```

### Properties

The old-style way for assigning a property to a class would be to use `property`:
```python
class Swagman:
    def __init__(self, weight_kg):
        self._weight_kg = weight_kg

    def get_weight(self):
        return self._weight_kg

    def set_weight(self, value):
        if value > 0:
            self._weight_kg = value
        else:
            raise ValueError("Weight must be a positive number.")

    weight = property(get_weight, set_weight)

bushwalker = Swagman(75)
bushwalker.weight = 112
```
The modern-style way to assign a property to a class would be to use the `@property` decorator:
```python
class Swagman:
    def __init__(self, weight_kg):
        self._weight_kg = weight_kg

    @property
    def weight(self):
        return self._weight_kg

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight_kg = value
        else:
            raise ValueError("Weight must be a positive number.")

bushwalker = Swagman(70)
bushwalker.weight = 78
```
### Decorators
Decorators are a way to modify or enhance the behaviour of functions or methods. This example adds authorisation logic without duplicating it in every function. The `@require_admin` decorator will intercept the function call and check the user role before continuing with the function execution.

Decorators allow you to create a read-only attribute

The `property` function (`@property` decorator) returns a descriptor object.

```python
def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin", False):
            print(f"Access denied for user {user['username']}: Admin privileges required.")
            return None
        print(f"Access granted for admin user {user['username']}.")
        return func(user, *args, **kwargs)
    return wrapper

@require_admin
def delete_course(user, course_id):
    print(f"Course {course_id} has been deleted.")
```
#### Order
| Concept           | Order                    | What happens                                                           |
|-------------------|--------------------------|------------------------------------------------------------------------|
| Decoration (load) | bottom :arrow_right: top | Wraps function objects, sets `my_function` to outermost wrapper        |
| Call (runtime)    | top :arrow_right: bottom | Outer wrapper runs first, calls inner wrappers, then original function |

This:
```python
@apply_handicap
@log_score
def record_score(player, score):
    print(f"{player} scored {score}")
```
is equivalent to this:
```python
result = apply_handicap(log_score(record_score))
```

`@classmethod` - used to define a class method. Class methods are methods that are bound to the class and not the instance. They can be called on the class itself, rather than on an instance of the class. Class methods take the class as the first argument, which is conventionally named `cls`.
```python
class Config:
    debug = False

    @classmethod
    def enable_debug(cls):
        cls.debug = True

print(Config.debug)  # False
Config.enable_debug()
print(Config.debug)  # True
```
`@staticmethod` - used to define a static method. Static methods are methods that do not take the instance or class as the first argument. They are similar to regular functions, but they are defined inside a class for organisational purposes. Static methods can be called on the class itself or on an instance of the class.

### Descriptors
Descriptors are objects that define how attributes are accessed and modified. They are used to create properties, methods, and other attributes that have custom behaviour. Descriptors are defined by implementing the `__get__()`, `__set__()`, and `__delete__()` methods.
```python
class WorldRanking:
    def __get__(self, instance, owner):
        print(f"Accessing world ranking for {instance.name}")
        return instance._ranking

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Ranking must be a positive integer")
        instance._ranking = value


class TennisPlayer:
    ranking = WorldRanking()

    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking

player = TennisPlayer("Andy Murray", 1)
print(player.ranking)   # 1

player.ranking = 2      # :ok:
# player.ranking = -5   # Would raise ValueError
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
```python
class User:
    pass

class Admin(User):
    pass

class Editor(User):
    pass

admin = Admin()

issubclass(Admin, User) 
# returns True
```

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

MRO (Method Resolution Order) - the order in which Python looks for a method or an attribute in a class hierarchy. You can view the MRO of a class using the `__mro__` attribute or the `mro()` method.

## Composition
A design principle where a class is made up of one or more objections from other classes. It has a "has-a" relationship rather than an "is-a" relationship. This is often preferred over inheritance as it allows for more flexibility and reusability of code. For example, a `Computer` class can be composed of `Storage`, `Memory`, and `CPU` classes.

## [itertools](https://docs.python.org/3/library/itertools.html)
The `itertools` module provides a set of fast, memory-efficient tools for working with iterators. It could be used to ensure instances of a class have a unique ID using a class-level counter, e.g.
```python
import itertools

class GrandPrixLap:
    _id_counter = itertools.count(1)  # class-level counter and start at 1

    def __init__(self):        
        self.id = next(self._id_counter)
```

## Exceptions
`__cause__` - when an exception is _explicitly chained_ using the `from` keyword, the original exception object is assigned to the `__cause__` attribute of the new exception.
```python
try:
    raise ValueError("You've just worked yourself into a shoot")
except ValueError as e:
    raise KeyError("This is a secondary error - key error occurred") from e
    # e.__cause__  # This will be the ValueError
```

Implicitly chained exceptions occur when an exception is raised inside another exception's `except` block. The new exception becomes the `__context__` of the original exception.

`__cause__` is always `None` for implicitly chained exceptions, while `__context__` is the original exception that caused the new exception to be raised.

`__cause__` is set to `None` by default unless you explicitly set it using the `from` keyword when raising the new exception.
```python
try:
    try:
        1872 / 0
    except ZeroDivisionError:
        raise ValueError("Oops. Ploblem.")
except Exception as e:
    print(f"__cause__: {e.__cause__}")   # None
    print(f"__context__: {type(e.__context__)}")   # <class 'ZeroDivisionError'>
```

`__context__` will be showing unless `__suppress_context__` is set to `True`

`finally` - always executed after `try` and `except` blocks.

:warning: **GOTCHA!** If a `finally` block contains a `return` it **overrides** any `return` from `try`, `except`, or `else`. 

Tracebacks can be accessed using the `__traceback__` attribute of an exception object. This attribute contains a traceback object that represents the call stack at the point where the exception was raised. You can use the `traceback` module to format and print the traceback information. It holds interesting information that is useful when you want to store exception details in other objects.

`traceback.print_tb()` - this function prints the traceback information to the console. It takes a traceback object as an argument and prints the call stack in a human-readable format.


## [pickle](https://docs.python.org/3/library/pickle.html)
The `pickle` module is used to serialise and deserialise Python objects. The `pickle` package is a good option for serialising single Python objects into a byte stream.

:no_entry_sign: Do not use `pickle` with data received from untrusted sources, as it can execute arbitrary code embedded in the pickle data during deserialisation.

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

## [shelve](https://docs.python.org/3/library/shelve.html)
Built on top of the `pickle` module, the `shelve` module provides a simple way to persistently store Python objects in a file. It allows you to store objects in a dictionary-like interface, where keys are strings and values are Python objects. This is useful for storing data that needs to be accessed later, such as application settings or user preferences.
```python
import shelve
books = shelve.open('books.shlv', flag='c')
```
### Flags
| Flag | Description                                                                   |
|------|-------------------------------------------------------------------------------|
| `c`  | Open for reading and writing, creating the file if it doesn't exist (default) |
| `r`  | Open for reading only                                                         |
| `w`  | Open for reading and writing                                                  |
| `n`  | Open for reading and writing, always creates a new empty database             |
It can also be used as a context manager using the `with` statement, which automatically handles closing the shelf when done.
```python
import shelve
with shelve.open('books.shlv') as books:
    books['1984'] = {'author': 'George Orwell', 'year': 1949}
    books['The Catcher in the Rye'] = {'author': 'J. D. Salinger', 'year': 1951}
```

## Closures
A closure is a function that retains access to its lexical scope, even when the function is executed outside that scope. This means that the inner function can access variables from the outer function even after the outer function has finished executing. They also provide data hiding because the enclosed variables are accessible only through the closure's methods.
```python
def golf_score_tracker(player_name):
    score = { 'strokes': 0 }  # mutable object

    def add_strokes(strokes):
        score['strokes'] += strokes
        return f"{player_name} now has {score['strokes']} strokes"

    return add_strokes

tiger = golf_score_tracker("Tiger Woods")
print(tiger(4))  # Tiger Woods now has 4 strokes.
print(tiger(3))  # Tiger Woods now has 7 strokes.
```
`nonlocal` - this keyword is used to declare that a variable in a nested function refers to a variable in the nearest enclosing scope that is not global. It allows you to modify variables in the outer function from within the inner function.
```python
def ticket_dispenser():
    ticket_number = 0
    def next_ticket():
        nonlocal ticket_number
        ticket_number += 1
        return f"Your ticket number is {ticket_number}"
    return next_ticket

dispenser = ticket_dispenser()
print(dispenser())
print(dispenser())
# Your ticket number is 1
# Your ticket number is 2
```

## Metaclasses
Metaclasses are classes of classes. 
* defined by inheriting from the `type` class
* can replace or modify attributes of classes
* have the ability to control class creation by modifying or replacing it
* has similarites to superclasses, but you want to use a metaclass when modifying or enforcing structure at the **class definition level** whereas a superclass is used for sharing logic or data across instances
* the `__new__` method in a metaclass is a factory that is responsible for creating the actual class object. It runs before `__init__`.
* they are utilised by frameworks such as [Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/en/stable/)
```python
class ScottishMeta(type):
    def __new__(cls, name, bases, namespace):
        # add a standard attribute to all classes using this metaclass
        namespace['region'] = 'Scotland'
        return super().__new__(cls, name, bases, namespace)

# any class using ScottishMeta will have 'region' set to 'Scotland'
class University(metaclass=ScottishMeta):
    pass

print(University.region)  # Scotland
```

## [queue](https://docs.python.org/3/library/queue.html)
The `queue` module provides thread-safe data structures for exchanging information between threads. It offers:
* Thread safety - handling all locking and synronisation internally
* Block behaviour - built-in support for blocking or non-blocking operations
* Simple API

## copy
The `[:]` syntax (or `copy.copy()`) is used to create a shallow copy of a list. It creates a new list object that contains the same elements as the original list, but the elements themselves are not copied. This means that if the elements are mutable objects, changes to those objects will be reflected in both lists.
```python
strikers = ['Dessers', 'Igamane', 'Danilo']
shallow_copied_strikers = strikers[:]
shallow_copied_strikers[0] = 'Moore'
print(strikers)  # ['Dessers', 'Igamane', 'Danilo']
print(shallow_copied_strikers)   # ['Moore', 'Igamane', 'Danilo']

teams = [['Dulka Pumpherston', 'Weatherfield County'], ['Walford Wanderers', 'Harchester United']]
copy_teams = teams[:]
copy_teams[0][0] = 'Atletico Partick'

print(teams)       # [['Atletico Partick', 'Weatherfield County'], ['Walford Wanderers', 'Harchester United']]
print(copy_teams)  # [['Atletico Partick', 'Weatherfield County'], ['Walford Wanderers', 'Harchester United']]
```
`copy.deepcopy()` - creates a deep copy of an object, meaning that it recursively copies all nested objects. This is useful when you want to create a completely independent copy of an object and its nested objects.

## sets
A set is an unordered collection of unique elements. 
Sets:
* mutable
* useful for storing unique items and performing set operations such as union (`set1.update(set2)`), intersection, and difference
* ignore duplicates

## Generators
* can only be iterated over once
* once a generator has been exhaused, you can't iterate over it again unless you recreate it
* yields values lazily, meaning it produces each value only when requested and resumes execution from where it left off after each `yield`
* When the generator is exhausted, it raises a `StopIteration` exception to signal that there are no more values to `yield`
* If a generator function executes a `return` statement, it raises a `StopIteration` exception with the value specified in the `return` statement as its argument
* `send(value)` - resumes the generator and sends a value that replaces the result of the current `yield` expression
```python
def process_files():
    print("Opening file system")
    yield "config.txt"
    print("Reading application data")
    yield "data.json"
    print("Cleanup completed")
    return "All files processed successfully"

def handle_file_processing(file_processor):
    processor = file_processor()
    try:
        while True:
            filename = next(processor)
            print(f"Processing: {filename}")
    except StopIteration as e:
        print(f"Status: {e.value}")

handle_file_processing(process_files)
```

## [collections](https://docs.python.org/3/library/collections.html)
The `collections` module provides alternatives to built-in types that can be more efficient or provide additional functionality.
```python
import collections
counter = collections.Counter
count_piccos = counter('crmpicco')
print(count_piccos.most_common(1))
# [('c', 3)]
```