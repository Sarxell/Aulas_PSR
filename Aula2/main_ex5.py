#!/usr/bin/python3

from Ex5 import readAllUpTo
import readchar
from Ex5 import printAllCharsUpTo
from Ex5 import countNumbersUpTo

def main():
    '''
    reads the char
    :return: nothing
    '''

    print('give me a char... ')

    c = readchar.readkey()
    printAllCharsUpTo(c)
    # readAllUpTo(c)
    countNumbersUpTo(c)


if __name__ == '__main__':
    main()