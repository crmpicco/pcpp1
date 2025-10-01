class ProgrammingLanguage:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I am a programming language called {self.name}."

class Python(ProgrammingLanguage):
    def __str__(self):
        return super().__str__() + " I am used for various purposes."

class Java(ProgrammingLanguage):
    def __str__(self):
        return super().__str__() + " I am known for my portability."

class JavaScript(ProgrammingLanguage):
    def __str__(self):
        return super().__str__() + " I am primarily used for web development."

python_lang = Python("Python")
java_lang = Java("Java")
js_lang = JavaScript("JavaScript")

print(issubclass(Python, ProgrammingLanguage), issubclass(Python, Java))
print(isinstance(python_lang, ProgrammingLanguage), isinstance(java_lang, ProgrammingLanguage))
