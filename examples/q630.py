from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Color(ABC):
    @abstractmethod
    def color_info(self):
        pass
class ColoredShape(Shape, Color):
    def __init__(self, color,area):
        self.color = color

    def area(self):
        return 0  

    def color_info(self):
        return f"This shape is {self.color} in color."


colored_shape = ColoredShape("red",5)

print(colored_shape.area())        
print(colored_shape.color_info())   
