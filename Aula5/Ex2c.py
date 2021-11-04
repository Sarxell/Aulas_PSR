#!/usr/bin/python3

import argparse
import cv2
import numpy as np


def main():
    parser = argparse.ArgumentParser(description='OPenCV example')
    parser.add_argument('--image1',required=True,type=str)
    args = vars(parser.parse_args())
    image_filename = '../../Aulas_PSR/Aula5/atlascar.png'

    image_original = cv2.imread(args['image1'], cv2.IMREAD_COLOR)
    # image_gray=cv2.cvtColor(image_original)
    image_b, image_g, image_r = cv2.split(image_original)

    ranges={'b':{'min':20,'max':150},
            'g':{'min':20,'max':150},
            'r':{'min':20,'max':150}}


    mins=np.array([ranges['b']['min'],ranges['g']['min'],ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    image_processed=cv2.inRange(image_original, mins,maxs)

    cv2.imshow('original', image_original)  # Display the image
    cv2.imshow('processed', image_processed)  # Display the image

    cv2.waitKey(0)  # wait for a key press before proceeding


if __name__ == '__main__':
    main()