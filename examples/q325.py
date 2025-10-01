class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return f'Rectangle({self.height}, {self.width})'
   
    def __lt__(self, other):

        return self.height * self.width < other.height * other.width
        
    def __gt__(self, other):
        
        return self.height * self.width > other.height * other.width

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 8)
rect3 = Rectangle(5, 10)
print(rect1 == rect2)  
print(rect1 == rect3)  
print(rect1 < rect2)  
print(rect2 > rect3) 
