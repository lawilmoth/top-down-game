class Circle:
    def __init__(self,x, y, radius):
        self.x = x
        self.y = y 
        self.radius = radius

    def get_area(self):
        return 3.14*self.radius**2
    
class Rectangle:
    def __init__(self,x, y, length, width):
        self.x = x
        self.y = y 
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
    
circle = Circle(0, 0, 5)
rectangle = Rectangle(0, 0, 4, 5)
