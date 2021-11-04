#!/usr/bin/python3

import argparse
import cv2

def main():

    parser=argparse.ArgumentParser(description='OPenCV example')
    parser.add_argument('--image1',type=str,help='Path to image')
    args=vars(parser.parse_args())

    image_filename = '../../Aulas_PSR/Aula5/atlascar.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_filename2='../../Aulas_PSR/Aula5/atlascar2.png'
    image2 = cv2.imread(image_filename2, cv2.IMREAD_COLOR)  # Load an image

    while True:
        cv2.imshow('window', image)  # Display the image
        # image_bright=image+28
        # cv2.imshow('window2',image_bright)
        cv2.waitKey(3000) # wait for a key press before proceeding
        cv2.imshow('window', image2)  # Display the image


    print(type(image))


if __name__ == '__main__':
    main()