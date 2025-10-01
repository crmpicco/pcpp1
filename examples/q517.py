class Dog:
    def __init__(self, name):
        self.name = name
Dog = type('Dog', (), {'name': 'Rex'})

# Equivalent:
# Dog = type('Dog', (), {'name': 'Rex'})
