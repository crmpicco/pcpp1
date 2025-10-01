class Person():
    def display1(self):
        print("This is superclass")		
class Employee(Person):
    def display1(self):
        print("This is subclass")
		
p = Employee()
p.display1()
