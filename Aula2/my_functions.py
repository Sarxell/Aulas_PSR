#py file with various functions

import math

def isPrime(value):
    """
    sees if a number is prime or not
    :param value: the number to test
    :return: True or false
    """

    print('\n reference number ' + str(value))

    for i in range(2,int(math.sqrt(value))):
        remainder = value % i
        print(str(value) + '/' + str(i) + 'has remainder' + str(remainder))


        if remainder == 0:
            return False

    return True

