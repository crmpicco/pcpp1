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

## [Coding Conventions, Best Practices, and Standardisation](https://github.com/crmpicco/pcpp1/blob/main/coding-conventions.md)

## [Advanced Object-Oriented Programming](https://github.com/crmpicco/pcpp1/blob/main/advanced-oop.md)

## [Network Programming](https://github.com/crmpicco/pcpp1/blob/main/network-programming.md)