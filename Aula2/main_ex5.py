
from Ex5 import readAllUpTo
import readchar
from Ex5 import printAllCharsUpTo
from Ex5 import countNumbersUpTo

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