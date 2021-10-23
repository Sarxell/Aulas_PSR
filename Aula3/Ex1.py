#!/usr/bin/python3
from colorama import Fore,Back,Style
from time import time, ctime
import math
ctime()
numbers = []

t = time()
# for x in range(1, 50000000):
#     numbers.append(math.sqrt(x))

numbers=[math.sqrt(x) for x in range(1, 50000000)]

elapsed = time()-t
print('this is ' + Fore.RED + 'Ex1 ' + Style.RESET_ALL + 'and the current date is ' + Back.YELLOW + Fore.BLUE + ctime() + Style.RESET_ALL)
print('Elapsed time is ' + str(elapsed) + ' seconds')
