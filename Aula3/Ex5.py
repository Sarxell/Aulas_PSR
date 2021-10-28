#!/usr/bin/python3

def add(x,y):
    real_x = x['r']
    imag_x = x['i']
    real_y = y['r']
    imag_y = y['i']

    real_part = real_x + real_y
    imag_part = imag_x + imag_y

    return {'r': real_part, 'i': imag_part}


def main():
    complex_dict={}

    complex_dict['c1']= {'r': 5, 'i': 3}
    complex_dict['c2'] = {'r': 2, 'i': -7}

    print(complex_dict)
    print(complex_dict['c1'])
    print(complex_dict['c2'])


if __name__ == '__main__':
    main()