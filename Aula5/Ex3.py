#!/usr/bin/python3

import argparse
import cv2
import numpy as np
import copy
from functools import partial


def onTrackbar(window_name,image_gray,val):
    mask_black = cv2.inRange(image_gray, 0, val)
    mask_black = ~mask_black
    cv2.imshow('mask_black', mask_black)
    mask_black =mask_black.astype(np.bool)
    tmp = copy.copy(image_gray)
    tmp[mask_black] = 0
    cv2.imshow(window_name, tmp)
    cv2.setMouseCallback(window_name, partial(test, window_name, tmp))



def test(window_name, image, event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, str(x) + ',' + str(y), (x, y), font, 0.5, (255, 0, 0), 2)
        # Displaying the image
        cv2.imshow(window_name, image)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())
    window_name = 'window - Ex3a'
    image_gray = None
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    cv2.createTrackbar('Red', window_name, 0, 255, partial(onTrackbar, window_name, image_gray))

    cv2.waitKey(0)

if __name__ == '__main__':
    main()