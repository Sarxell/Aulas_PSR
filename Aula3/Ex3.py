#!/usr/bin/python3
from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(x, y):
    """
    :param x: complex number 1
    :param y: complex number 2
    :return: addition
    """

    r = complex(x.r, x.i) + complex(y.r, y.i)
    return r


def multiplyComplex(x, y):
    """
    :param x: complex number 1
    :param y: complex number 2
    :return: multiplication
    """
    r = complex(x.r, x.i) * complex(y.r, y.i)
    return r

def printComplex(x):
    x=str(x)
    x = x.strip(')')
    x = x.strip('(')
    print(x)

def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    print('c1 = ' + str(c1)) # named tuple looks nice when printed

    # Test add
    c3=addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()