#!/usr/bin/python3

import argparse
import cv2
import numpy as np
import copy

# Global variables
window_name = 'window - Ex3a'
image_gray = None

def onTrackbar(val):
    mask_black = cv2.inRange(image_gray, 0, val)
    mask_black= ~mask_black
    cv2.imshow('mask_black', mask_black)
    mask_black =mask_black.astype(np.bool)
    tmp = copy.copy(image_gray)
    tmp[mask_black] = 0
    cv2.imshow(window_name, tmp)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    cv2.createTrackbar('Red', window_name, 0, 255, onTrackbar)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()