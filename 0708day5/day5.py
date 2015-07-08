import math

class Shape:

    perimeter = 0
    area = 0

    def calcArea(self):
        pass

    def calcPerimeter(self):
        pass

    def printInfo(self):
        print "Area : {0}, Perimeter : {1}".format(self.area, self.perimeter)
        pass


    def __init__(self, perimeter = 0, area = 0):
        self.perimeter = perimeter
        self.area = area
        print "?"


shape1 = Shape()
#shape1.printInfo()

class Rectangle(Shape):
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
rect.printInfo()

class Triangle(Shape):
    x = 0
    def __init__(self, x):
        self.x = x
        #self.height = height
    def calcArea(self):
        self.area = math.sqrt(3) * pow(self.x, 2) / 4
    def calcPerimeter(self):
        self.perimeter = 3 * self.x

tri = Triangle(3)
tri.calcArea()
tri.calcPerimeter()
tri.printInfo()

class Circle(Shape):
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
cir.printInfo()

class Person:
    name = ""
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return "{0} and {1} became friends".format(self.name, other.name)

per1 = Person("JH")
per2 = Person("SW")

print per1 + per2
