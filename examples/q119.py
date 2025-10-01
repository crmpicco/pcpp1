class Person:
	def display(self):
		print("Person called")

class Father(Person):
	def display(self):
		print("Father called")

class Mother(Person):
	def display(self):
		print("Mother called")

class Child(Mother, Person):  # Mother should be before Person in inheritance
	pass

child_obj = Child()
child_obj.display()
