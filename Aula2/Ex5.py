import colorama
import readchar
from colorama import Fore,Back, Style
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
    numbers = []
    inputs = []
    dictio = {}

    while True:
        print('Type something (''X'' to stop)')
        a = readchar.readkey()
        inputs.append(a)

        if a == 'X':
            break

    for index_input,input in enumerate(inputs):
        if input.isnumeric():
            total_numbers = total_numbers + 1
            numbers.append(input)
        else:
            total_others = total_others + 1
            dictio[index_input] = input

    #numbers = [x for x in inputs if str.isnumeric(x)]

    list_other=list(dictio.values())
    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')
    print('The numbers inserted were ' + str(numbers))
    print('The others inserted were ' + str(list_other))
    # caso seja preciso ordenar dicionarios por o value
    # print('The dictionary has' + str(dict(sorted(dictio.items(), key=lambda x: (x[1], x[0])))))

    numbers.sort()
    print('The sorted numbers inserted were ' + str(numbers))
    no_rep=list(set(numbers))
    no_rep.sort()
    print('The sorted numbers inserted with no repetition were ' + str(no_rep))
    colors = list(vars(colorama.Fore).values())
    print(colors)
    txt_colour=''

    for i in range(0,len(list_other)):
        txt_colour=txt_colour + colors[i] + Style.DIM + str(list_other[i]) + Style.RESET_ALL

    print(txt_colour)