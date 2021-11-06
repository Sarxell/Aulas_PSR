#!/usr/bin/python3
#exte exercicio é o 2d
import argparse
import cv2
import numpy as np
import copy

def main():
    parser = argparse.ArgumentParser(description='OPenCV example')
    parser.add_argument('--image1',required=True,type=str)
    args = vars(parser.parse_args())
    image_filename = '../../Aulas_PSR/Aula5/atlascar.png'

    image_original = cv2.imread(args['image1'], cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image_original, cv2.COLOR_BGR2HSV)
    image_b, image_g, image_r = cv2.split(image)

    ranges = {'b': {'min': 0, 'max': 50},
              'g': {'min': 80, 'max': 150},
              'r':{'min': 0, 'max': 50}}


    mins=np.array([ranges['b']['min'],ranges['g']['min'],ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(image_original, mins, maxs)

    mask=mask.astype(np.bool)
    image_processed = copy.deepcopy(image_original)
    #image_processed[mask] = (image_processed[mask]*0.4).astype(np.uint8)

    # para pintar de vermelho
    image_processed[mask] = (0, 0, 255)
    print(image_original.dtype)
    print(mask.dtype)

    cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('original', image_original)  # Display the image
    cv2.imshow('mask', mask.astype(np.uint8)*255)  # Display the image
    cv2.imshow('processed', image_processed)
    cv2.waitKey(0)  # wait for a key press before proceeding


if __name__ == '__main__':
    main()