#!/usr/bin/python3

from Ex4 import readAllUpTo
import readchar
from Ex4 import printAllCharsUpTo
from Ex4 import countNumbersUpTo

def main():
    '''
    reads the char
    :return: nothing
    '''

    c = readchar.readkey()
    printAllCharsUpTo(c)
    # readAllUpTo(c)
    countNumbersUpTo(c)


if __name__ == '__main__':
    main()