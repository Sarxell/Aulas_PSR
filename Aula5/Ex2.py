#!/usr/bin/python3

import argparse
import cv2
import numpy as np

def main():

    parser = argparse.ArgumentParser(description='OPenCV example')
    parser.add_argument('--image1', required=True, type=str)
    args = vars(parser.parse_args())
    image_filename = '../../Aulas_PSR/Aula5/atlascar.png'

    image_original = cv2.imread(args['image1'], cv2.IMREAD_COLOR)
    image_gray = cv2.cvtColor(image_original, cv2.COLOR_RGB2GRAY)
    # SPLIT É PARA O 2C
    image_b, image_g, image_r = cv2.split(image_original)

   #  retval, image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    image_thresholded = image_gray > 128


    _, image_processed_b = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)
    _, image_processed_r = cv2.threshold(image_r, 100, 255, cv2.THRESH_BINARY)
    _, image_processed_g = cv2.threshold(image_g, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow('original', image_original) # Display the image
    cv2.imshow('threshold', image_thresholded.astype(np.uint8)*255)
    cv2.imshow('processed b', image_processed_b)  # Display the image
    cv2.imshow('processed r', image_processed_r)
    cv2.imshow('processed g', image_processed_g)



    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()