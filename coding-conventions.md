## Coding Conventions, Best Practices, and Standardisation
[PEP-8 naming conventions](https://peps.python.org/pep-0008/#naming-conventions)

PEP-8 guidelines are a set of rules for formatting Python code to enhance readability and maintainability.

:wink: If you are starting a new project, it is recommended to use [PEP-8](https://peps.python.org/pep-0008/) as a guide for writing Python code.

* :x: Avoid using lowercase `l`, uppercase `O`, and uppercase `I` as variable names, since they can be confused with the digits `1` and `0`.
* Modules - Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability, e.g. `cron_locker`
* Packages - Package names should also have short all-lowercase, although underscores are discouraged.
* Classes - Class names should normally use the CapWords convention, e.g. `UserMetadata`
* Exceptions - exceptions should be classes, so should follow the class naming convention. Use the `Error` suffix on exception names, e.g. `UserNotFoundError`, `InvalidInputError`.
* Functions - Function names should be lowercase, with words separated by underscores as necessary to improve readability.
* Variables - Variable names follow the same convention as function names.
* Function and Method arguments - Always use `self` for the first argument to instance methods and `cls` for the first argument to class methods.
* Constants - Constants are usually defined on a module level and written in all capital letters with underscores separating words, e.g. `BUCKET_NAME` and `THRESHOLD`.

Avoid extraneous whitespace in the following situations:
* Immediately inside parentheses, brackets, or braces.
```python
# No extra spaces
letsgo(info[1], {level: 2})
# Extra spaces
letsgo( info[ 1 ], { level: 2 } )
```
* Immediately before the open parenthesis that starts and indexing or slicing.
```python
# No extra spaces
developer = {'name': 'crmpicco', 'language': 'Python'}
info = developer['name']
# Extra spaces
info = developer[ 'name' ]
```
* More than one space around an assignment (or other) operator to align it with another.
```python
# No extra spaces
aws = 1
gcp = 2
microsoft_azure = 3
# Extra spaces
aws             = 1
gcp             = 2
microsoft_azure = 3
```

### Maximum Line Length
* :seven::two: characters for docstrings and comments
* :seven::nine: characters for code

The restricted line length originates from the early days of computing when terminals were limited to 80 characters per line. This convention is still followed in Python to ensure code readability across different editors and environments.

### Trailing commas
Trailing commas are mandatory when making a tuple of one element, even although they appear redundant.
```python
towns = ('Mauchline',)
```
### Comparisons
Use `is` or `is not` when comparing to `None`. From a performance perspective, `is` is faster than `==` because it checks for object identity rather than value equality.
```python
crmpicco = None
if crmpicco is None:
    print("crmpicco is not here")

the_champ = "cnation"
if the_champ is not None:
    print("the champ is here")
``` 

### Types
#### Informational
Informational PEPs describe a Python design issue, or provide general guidelines or information to the Python community. Some examples of informational PEPs are [PEP-20](https://peps.python.org/pep-0020/) (The Zen of Python), and [PEP-257](https://peps.python.org/pep-0257/) (Docstring conventions).

:information_source: You can view the PEP-20 aphorisms by running the following command from the REPL:
```python
Python 3.13.4 (main, Jun  3 2025, 15:34:24) [Clang 17.0.0 (clang-1700.0.13.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
#### Standards Track
Standards Track PEPs describes a new feature or implementation in Python. They include a specification and a rationale for the change. An examples of Standards Track PEPs is [PEP-621](https://peps.python.org/pep-0621/).

### [Sections](https://peps.python.org/pep-0001/#what-belongs-in-a-successful-pep)
#### Abstract
A short summary and description of the technical issue being addressed.
#### Preamble
[RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822.html) headers, including the title, author, metadata and status of the PEP.
#### Open Issues
Ideas related to the PEP that are not yet resolved. This section is optional.

## Comments
* Comments should be written in English
* Comments that contradict the code are worse than no comments at all
* Inline comments should start with a `#` and a single space and should be written on the same line as your statements

## [Docstrings](https://peps.python.org/pep-0257/)
* String literals that occur as the first statement in a module, function, class or method definition.
* For one-liner docstrings, the closing `"""` should be on the same line
* The `"""` that ends a multiline docstring should be on a line by itself. For consistency, always use triple double quotes around docstrings.
```python
def process_records(records, target):
    """Process the records for the target provided."""
    pass
```

Strings - single-quoted strings and double-quoted strings are the same in Python. When a string contains single or double quote characters, use the other one to avoid backslashes in the string.
```python
name = "Stéphane Guivarc'h"  # :white_check_mark: No need for backslash
comment = 'He said, "Hello Hello!"'  # :white_check_mark: No need for backslash
```

### Type variables
Type variables, from the [typing](https://docs.python.org/3/library/typing.html) module, are used to define generic types in Python.
* :no_entry_sign: Do **not** exist at runtime and are implicitly established by [PEP-484](https://peps.python.org/pep-0484/). 
* Type annotations provide optional metadata used for static type checking and help IDEs with autocompletion. 
* They allow you to create functions and classes that can work with different types while maintaining type safety. 
* Type variable names should typically use CamelCase (CapWords), for example:
#### Single-letter type variable
```python
from typing import TypeVar
T = TypeVar('T')  # a type variable that can be any type

def identity(value: T) -> T:
    """Return the value unchanged."""
    return value
```
#### Descriptive CamelCase type variable
```python
from typing import TypeVar
UserId = TypeVar('UserId')

def get_user(user_id: UserId):
    """Retrieve a user by their ID."""
    pass
```
### Context Managers
`with` statements - used to wrap the execution of a block with methods defined by a context manager. It ensures that resources are properly managed, such as closing files or releasing locks.

To make a class usable with a `with` statement, you need to implement the `__enter__()` and `__exit__()` methods. 

* `__enter__()` - called when the block is entered
* `__exit__()` - called when the block is exited. Always called even if an exception occurs inside the `with` block. This allows context managers to clean up resources.

```python
class APIConnection:
    def __enter__(self):
        print("Connection opened")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Connection closed")

with APIConnection() as connection:
    print("Using connection")
```

`self` - refers to the instance of the class within the context manager. It allows you to access instance variables and methods.
It is **not** a keyword and is only a naming convention.

If you return `True` from `__exit__()`, it suppresses the exception, meaning it won't be propagated outside the `with` block. This can be useful if you want to handle exceptions within the context manager itself.

:warning: **GOTCHA!** Never use mutable objects like lists or dicts as default arguments. The alternative is to use `None` and handle it inside the function. Default arguments are evaluated only once at the time the function is defined, not every time it is called.

:x: `def add_item(lst=[]):`

:white_check_mark: `def add_item(lst=None):`