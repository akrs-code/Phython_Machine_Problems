class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def calculate_area(self):
        return self.length * self.width
    
rectangle = Rectangle(2,3)
print(rectangle.calculate_area())

