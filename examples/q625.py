class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be a positive value.")
    radius = property(get_radius, set_radius) 
circle = Circle(5)
circle.radius = 10  
