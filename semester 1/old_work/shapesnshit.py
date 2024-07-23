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
     def get_info(self):
         super().get_info()
         print(f"Radius: {self.radius}")
         print(f"Area: {GetInfo.get_area(self, self.radius, 0)}")

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
         print(f"Area: {GetInfo.get_area(self, self.width, self.length)}")

class Triangle(Shape):
    def __init__(self, colour, width, height):
        super().__init__(colour)
        self.width = width
        self.height = height
    def get_info(self):
        super().get_info()
        print(f"Area: {GetInfo.get_area(self, self.width, self.height)}")

class GetInfo(Shape):
    def get_area(self, width, height):
        if Triangle:
            self.area = width * height * 0.5
        elif Rectangle:
            self.area = width * height
        elif Circle:
            self.area = 3.14 * width**2
        return self.area

john = Circle("Green", 12)
john.get_info()

steve = Rectangle("Brown", 4, 4)
steve.get_info()

evan = Triangle("Steven", 12, 4)
evan.get_info()