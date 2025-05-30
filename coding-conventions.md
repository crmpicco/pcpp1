## Coding Conventions, Best Practices, and Standardisation
[PEP-8 naming conventions](https://peps.python.org/pep-0008/#naming-conventions)
* :x: Avoid using lowercase `l`, uppercase `O`, and uppercase `I` as variable names, since they can be confused with the digits `1` and `0`.
* Modules - Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability.
* Packages - Package names should also have short all-lowercase, although underscores are discouraged.
* Classes - Class names should normally use the CapWords convention, e.g. `UserMetadata`
* Exceptions - exceptions should be classes, so should follow the class naming convention. Use the `Error` suffix on exception names.
* Functions - Function names should be lowercase, with words separated by underscores as necessary to improve readability.
* Variables - Variable names follow the same convention as function names.
* Function and Method arguments - Always use `self` for the first argument to instance methods and `cls` for the first argument to class methods.
* Constants - Constants are usually defined on a module level and written in all capital letters with underscores separating words, e.g. `BUCKET_NAME` and `THRESHOLD`.

### Maximum Line Length
* :seven::two: characters for docstrings and comments
* :seven::nine: characters for code

The restricted line length originates from the early days of computing when terminals were limited to 80 characters per line. This convention is still followed in Python to ensure code readability across different editors and environments.

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
#### Standards Track
Standards Track PEPs describes a new feature or implementation in Python. They include a specification and a rationale for the change. An examples of Standards Track PEPs is [PEP-621](https://peps.python.org/pep-0621/).

### [Sections](https://peps.python.org/pep-0001/#what-belongs-in-a-successful-pep)
#### Abstract
A short summary and description of the technical issue being addressed.
#### Preamble
[RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822.html) headers, including the title, author, metadata and status of the PEP.
#### Open Issues
Ideas related to the PEP that are not yet resolved. This section is optional.

## [Docstrings](https://peps.python.org/pep-0257/)
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
Type variables, from the [typing](https://docs.python.org/3/library/typing.html) module, are used to define generic types in Python. They do not exist at runtime and are implicitly established by [PEP-484](https://peps.python.org/pep-0484/). They allow you to create functions and classes that can work with different types while maintaining type safety. Type variable names should typically use CamelCase (CapWords), for example:
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
