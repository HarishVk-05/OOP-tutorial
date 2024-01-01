class Fraction:

    # parameterized constructor (we give inputs to the constructor)
    def __init__(self, x, y):
        self.numerator = x
        self.denominator = y

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)
    
    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return "{}/{}".format(new_numerator, new_denominator)
    

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return "{}/{}".format(new_numerator, new_denominator)
    

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return "{}/{}".format(new_numerator, new_denominator)
    

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return "{}/{}".format(new_numerator, new_denominator)
    

    def convert_frac_to_decimal(self):
        return self.numerator / self.denominator


fr1 = Fraction(6, 8)
fr2 = Fraction(5, 7)
print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
print(fr1.convert_frac_to_decimal())
