
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
    numbers=[]
    inputs = []
    dictio={}

    while True:
        a = readchar.readkey()
        inputs.append(a)

        if a == stop_char:
            break

    for input in inputs:
        if input.isnumeric():
            total_numbers = total_numbers + 1
            numbers.append(input)
        else:
            total_others = total_others + 1
            dictio[total_others] = input

    numbers.sort()
    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')
    print('The numbers inserted were ' + str(numbers))
    # caso seja preciso ordenar dicionarios por o value
    # print('The dictionary has' + str(dict(sorted(dictio.items(), key=lambda x: (x[1], x[0])))))
