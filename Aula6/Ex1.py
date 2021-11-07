#!/usr/bin/python3

import argparse
import cv2
import numpy as np
import copy
from functools import partial


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())
    window_name = 'image'
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)
    cv2.circle(image, (200, 200), 50, (255, 0, 0), 2)

    cv2.imshow(window_name,image)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()