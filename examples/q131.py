class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Bird:
    pass

print(issubclass(Dog, Animal))  # Output: True, Dog is a subclass of Animal
print(issubclass(Cat, Animal))  # Output: True, Cat is a subclass of Animal
print(issubclass(Bird, Animal)) # Output: False, Bird is not a subclass of Animal

# Multiple inheritance: Checking if Dog is a subclass of both Animal and Bird
print(issubclass(Dog, (Animal, Bird)))
