#!/usr/bin/python3
#main function of the primos work

from my_functions import isPrime
from colorama import Fore,Back, Style
import argparse, sys

def main():
    """
    shows what number is prime and what number isn't
    :return: nothing
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("--max_number", help="chooses the maximum number to use",
                        type=int)
    args = parser.parse_args()
    # usar vars para colocar o argumento entre chavetas

    if args.max_number < 1 or args.max_number > 1000:
        print("invalid range, it needs to be between 1 and 1000")
        sys.exit(1)

    maximum_number = args.max_number
    # com vars para se colocar o numero seria args['max_number']

    print("Starting to compute prime numbers up to " + str(maximum_number))

    counter=0
    for i in range(1, maximum_number):
        if isPrime(i):
            counter = counter + 1
            print(Fore.RED + Back.YELLOW + Style.DIM +'Number ' + str(i) + ' is prime' + Style.RESET_ALL)
        else:
            print('Number ' + str(i) + ' is not prime')

    print(Fore.BLUE + 'Between 1 and ' + str(maximum_number) + ' we have ' + str(counter) + ' prime numbers' + Style.RESET_ALL)

if __name__ == "__main__":
    main()