#!/usr/bin/python3
from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])

class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        real = self.r + y.r
        imag = self.i + y.i
        result = Complex(r=real, i=imag)
        return result

    def multiply(self, y):
        result = Complex(r=(self.r * y.r), i=(self.i * y.i))
        return result

    def __str__(self):
        return '(%g, %g)' % (self.r, self.i)


def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    c1.add(c2)
    print(c1)  # uses the __str__ method in the class

    # test multiply
    print(c2)  # uses the __str__ method in the class
    c2.add(c1)
    print(c2)  # uses the __str__ method in the class


if __name__ == '__main__':
    main()