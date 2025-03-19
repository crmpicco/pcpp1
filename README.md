# PCPP1™ – Certified Professional Python Programmer Level 1
 (Exam [PCPP-32-10x](https://pythoninstitute.org/pcpp1-exam-syllabus)) 

![PCPP1-Badge](https://images.credly.com/images/37e26478-d80c-43e8-80eb-ec492f3a26c1/image.png)

![pycodestyle](https://github.com/crmpicco/pcpp1_notes/actions/workflows/pycodestyle.yml/badge.svg)

Notes and small sample applications for the Python PCPP1 course and exam

## Tkinter
![Rangers tkinter app](https://github.com/crmpicco/pcpp1/blob/main/rfc-tkinter.gif?raw=true)

### Installation
`brew install python-tk@3.12` # Install Tkinter on macOS

### Widgets
- [x] **Label** - not clickable, no `command` attribute or callback functionality
- [x] **Button** - has a `command` attribute that is a callback function
- [x] **Entry**
- [x] ~~Text~~
- [x] **Frame** - not clickable, no `command` attribute or callback functionality
- [x] **Canvas**

### Geometry Managers
- [x] pack - simple "box" layout. Stacks widgets vertically or horizontally. Good for simple layouts. Uses `side='top'`, `side='bottom'` etc...
- [x] grid - uses rows and columns, like a table. Best for forms and structured layouts. Uses `row=x`, `column=y` etc...
- [x] place - places widgets at exact x and y coordinates. Not recommended for responsive UIs. Uses `.place(x=X, y=Y)`.

### Events
- [x] bind / event handlers
- [x] unbind 

### Other
- [x] StringVar / IntVar
- [x] Command binding
- [x] messagebox
- [x] PhotoImage
- [x] destroy
- [x] config method

### Resources

Data is retrieved from the free APIs at https://www.api-football.com/

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