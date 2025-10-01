class Vehicle:
    brand="Opel"
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f'Brand is {self.brand}.'

class Car(Vehicle):
    brand="BMW"
    def __init__(self, brand):
        super().__init__(brand)
    
    def display_info(self):
        print(f"This is a car of brand {self.brand} and model {self.model}.")


my_vehicle = Car('Toyota')
print(my_vehicle.brand)
print(Vehicle.brand)
print(Car.brand)
