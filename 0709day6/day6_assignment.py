import math
class Shape:
    area = 0
    def calcArea(self):
        pass

    def printArea(self):
        print "Area : {0}".format(self.area)
        pass

    def __init__(self, area = 0):
        self.area = area

class TwoDim(Shape):
    perimeter = 0
    def calcPerimeter(self):
        pass

    def printPerimeter(self):
        print "Perimeter : {0}".format(self.perimeter)
        pass

class ThreeDim(Shape):
    volume = 0
    def calcVolume(self):
        pass000

    def printVolume(self):
        print "Volume : {0}".format(self.volume)
        pass

class Rectangle(TwoDim):
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcArea(self):
        self.area = self.x * self.y

    def calcPerimeter(self):
        self.perimeter = 2 * (self.x + self.y)

rect = Rectangle(2, 4)
rect.calcArea()
rect.calcPerimeter()
print "Rectangle information"
rect.printArea()
rect.printPerimeter()

class Triangle(TwoDim):
    x = 0
    def __init__(self, x):
        self.x = x

    def calcArea(self):
        self.area = math.sqrt(3) * pow(self.x, 2) / 4

    def calcPerimeter(self):
        self.perimeter = 3 * self.x

tri = Triangle(3)
tri.calcArea()
tri.calcPerimeter()
print "Triangle information"
tri.printArea()
tri.printPerimeter()

class Circle(TwoDim):
    r = 0
    PI = 3.14
    def __init__(self, r, PI = 3.14):
        self.r = r
        self.PI = 3.14

    def calcArea(self):
        self.area = self.r * self.r * self.PI

    def calcPerimeter(self):
        self.perimeter = 2 * self.PI * self.r

cir = Circle(3)
cir.calcArea()
cir.calcPerimeter()
print "Circle information"
cir.printArea()
cir.printPerimeter()

class Cube(ThreeDim):
    a = 0
    def __init__(self, a):
        self.a = a

    def calcArea(self):
        self.area = pow(self.a, 2) * 6

    def calcVolume(self):
        self.volume = pow(self.a, 3)

cub = Cube(3)
cub.calcArea()
cub.calcVolume()
print "Cube information"
cub.printArea()
cub.printVolume()

class Sphere(ThreeDim):
    r = 0
    PI = 3.14
    def __init__(self, r, PI = 3.14):
        self.r = r
        self.PI = 3.14

    def calcArea(self):
        self.area = 4 * self.PI * pow(self.r, 2)

    def calcVolume(self):
        self.volume = (4.0 / 3) * self.PI * pow(self.r, 3)

sph = Sphere(3)
sph.calcArea()
sph.calcVolume()
print "Sphere information"
sph.printArea()
sph.printVolume()