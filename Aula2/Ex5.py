
import readchar
import sys


def printAllCharsUpTo(stop_char):
    '''
    prints all the chars in ascii till the stop char
    :param stop_char: the char where the program stops sending chars
    :return: nothing
    '''

    inicial_number = ord(' ')
    stop_number = ord(stop_char)

    while inicial_number != stop_number:
        print(chr(inicial_number))
        inicial_number = inicial_number+1


def readAllUpTo(stop_char):
    """
    reads the chars
    :param stop_char: the function stops when it arrives to this char
    :return:nothing
    """
    # não consigo perceber muito bem o que se quer dizer com a questão 4.b)

    a = readchar.readkey()

    while a != stop_char:
        a = readchar.readkey()


def countNumbersUpTo(stop_char):
    total_numbers = 0
    total_others = 0
    inputs = []
    while True:
        a = readchar.readkey()
        inputs.append(a)

        if a == stop_char:
            break

    for input in inputs:
        if input.isnumeric():
            total_numbers = total_numbers + 1

        if input.isascii():
            total_others = total_others + 1

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')


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