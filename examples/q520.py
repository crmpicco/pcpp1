class Parent1:
    pass
class Parent2:
    pass
class Child(Parent1,Parent2):
    pass

print("Child's base classes:", Child.__bases__)
