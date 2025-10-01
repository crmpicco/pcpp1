class Animal:
    def __init__(self, animal_type):
        if animal_type == 'dog':
            self.sound = 'Woof!'
        elif animal_type == 'cat':
            self.sound = 'Meow'
        else:
            self.info = f"Unknown animal: {animal_type}"

animals = [
    Animal('dog'),
    Animal('cat'),
    Animal('bird'),
    Animal('elephant'),
]

for animal in animals:
    print(hasattr(animal, 'sound'))
