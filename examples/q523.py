class Example:

	def __init__(self, val):
		self.val = val
		
	def __add__(self, val2):
		return Example(self.val + val2.val)

obj1 = Example(1)
obj2 = Example(2)
obj3 = obj1 + obj2
print(obj3.val)
