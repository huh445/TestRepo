class Shape:
     def __init__(self, colour):
        self.colour = colour
     def get_area(self):
         raise NotImplementedError("Not implemented LMFAO")
     def get_info(self):
         print(f"Shape: {self.__class__.__name__} - Colour: {self.colour}")
     
class Circle(Shape):
     def __init__(self, colour, radius):
        super().__init__(colour)
        self.radius = radius
     def get_area(self):
         return 3.14 * self.radius**2
     def get_info(self):
         super().get_info()
         print(f"Radius: {self.radius}")

class Rectangle(Shape):
     def __init__(self, colour, width, length):
        super().__init__(colour)
        self.width = width
        self.length = length
     def get_area(self):
         self.area = self.width * self.length
         return self.area
     def get_info(self):
         super().get_info()
         print(f"Area: {self.get_area()}")
     def is_square(self):
         if self.width == self.length:
             return True
         else:
             return False

class Triangle(Shape):
     def __init__(self, colour)
john = Circle("Green", 12)
john.get_info()
print(f"John's area = {john.get_area()}")

steve = Rectangle("Brown", 4, 4)
steve.get_info()
print(f"Steve is a square, {steve.is_square()}")