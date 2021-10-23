
def addComplex(x, y):
    """
    :param x: complex number 1
    :param y: complex number 2
    :return: addition
    """
    x1, x2 = x
    y1, y2 = y
    r = complex(x1,x2)+complex(y1,y2)
    return r

def multiplyComplex(x, y):
    """
    :param x: complex number 1
    :param y: complex number 2
    :return: multiplication
    """
    x1, x2 = x
    y1, y2 = y
    r = complex(x1,x2)*complex(y1,y2)
    return r

def printComplex(x):
    """
    :param x: the complex number to print
    :return: nothing
    """
    x = str(x)
    x = x.strip(')')
    x = x.strip('(')
    print(x)