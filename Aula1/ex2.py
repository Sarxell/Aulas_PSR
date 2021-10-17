#!/usr/bin/python3

from colorama import Fore,Back, Style

maximum_number = 8

def isPrime(value):
    print('\n reference number ' + str(value))

    for i in range(2,value):
        remainder = value % i
        print(str(value) + '/' + str(i) + 'has remainder' + str(remainder))

        if remainder == 0:
            return False

    return True

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    counter=0
    for i in range(1, maximum_number):
        if isPrime(i):
            counter = counter + 1
            print(Fore.RED + Back.YELLOW + Style.DIM +'Number ' + str(i) + ' is prime' + Style.RESET_ALL)
        else:
            print('Number ' + str(i) + ' is not prime')

    print(Fore.Blue + 'Between 1 and ' + str(maximum_number) + ' we have ' + str(counter) + ' prime numbers' + Style.RESET_ALL)

if __name__ == "__main__":
    main()