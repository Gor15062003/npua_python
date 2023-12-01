class Shape:
    def area(self):
        pass

    def volume(self):
        pass


class TwoDimensional(Shape):
    def area(self):
        pass


class ThreeDimensional(Shape):
    def area(self):
        pass

    def volume(self):
        pass


class Square(TwoDimensional):
    def init(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class Triangle(TwoDimensional):
    def init(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Cube(ThreeDimensional):
    def init(self, side_length):
        self.side_length = side_length

    def area(self):
        return 6 * self.side_length ** 2

    def volume(self):
        return self.side_length ** 3


class Cone(ThreeDimensional):
    def init(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        import math
        slant_height = math.sqrt(self.radius  2 + self.height  2)
        return math.pi * self.radius * (self.radius + slant_height)

    def volume(self):
        import math
        return (1/3) * math.pi * self.radius ** 2 * self.height


#daseri orinakner
square = Square(5)
triangle = Triangle(4, 3)
cube = Cube(3)
cone = Cone(2, 6)

print("Square Area:", square.area())  # Выводит площадь квадрата
print("Triangle Area:", triangle.area())  # Выводит площадь треугольника
print("Cube Area:", cube.area())  # Выводит площадь поверхности куба
print("Cube Volume:", cube.volume())  # Выводит объем куба
print("Cone Area:", cone.area())  # Выводит площадь поверхности конуса
print("Cone Volume:", cone.volume())  # Выводит объем конуса
