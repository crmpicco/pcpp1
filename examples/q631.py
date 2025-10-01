from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyingBird(Animal):
    def __init__(self, species):
        self.species = species
    species="abc"
    def fly(self):
        return f"{self.species} is flying."
    def sound(self):
        return f"The sound of {self.species} is {self.sound}."

flying_bird = FlyingBird("Sparrow", "chirp")

print(flying_bird.fly())        
print(flying_bird.sound()) 
