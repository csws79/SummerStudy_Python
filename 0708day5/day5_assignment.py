class Fraction:
    numerator1 = 0
    denominator1 = 0

    def __init__(self, numerator1, denominator1):
        self.numerator1 = numerator1
        self.denominator1 = denominator1

    def prt(self, numerator1):
        print str(self.numerator1) + "/" + str(self.denominator1)
    def __add__(self, other):
        return "+ answer: " + str(self.numerator1 * other.denominator1 + self.denominator1 * other.numerator1) + "/" + str(self.denominator1 * other.denominator1)
    def __sub__(self, other):
        return "- answer: " + str(self.numerator1 * other.denominator1 - self.denominator1 * other.numerator1) + "/" + str(self.denominator1 * other.denominator1)
    def __mul__(self, other):
        return "* answer: " + str(self.numerator1 * other.numerator1) + "/" + str(self.denominator1 * other.denominator1)
    def __div__(self, other):
        return "/ answer: " + str(self.numerator1 * other.denominator1) + "/" + str(self.denominator1 * other.numerator1)

test = Fraction(2, 3)
test.prt(test)

print "Input the first fraction."

frac1 = Fraction(input(), input())
frac1.prt(frac1)

print "Input the second fraction."

frac2 = Fraction(input(), input())
frac2.prt(frac2)

print frac1 + frac2
print frac1 - frac2
print frac1 * frac2
print frac1 / frac2