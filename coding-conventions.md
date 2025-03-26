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

## [Docstrings](https://peps.python.org/pep-0257/)
* For one-liner docstrings, the closing `"""` should be on the same line
* The `"""` that ends a multiline docstring should be on a line by itself
```python
def process_records(records, target):
    """Process the records for the target provided."""
    pass
```