#!/usr/bin/python3

import argparse
import cv2
import numpy as np
import copy
from functools import partial
import json


def onTrackbar(segmented_window, image, limits, val):
    mins = np.array([limits['B']['min'], limits['G']['min'], limits['R']['min']])
    maxs = np.array([limits['B']['max'], limits['G']['max'], limits['R']['max']])
    # getting the values of the trackbars
    mins[0] = cv2.getTrackbarPos('min B/H', segmented_window)
    mins[1] = cv2.getTrackbarPos('min G/S', segmented_window)
    mins[2] = cv2.getTrackbarPos('min R/V', segmented_window)
    maxs[0] = cv2.getTrackbarPos('max B/H', segmented_window)
    maxs[1] = cv2.getTrackbarPos('max G/S', segmented_window)
    maxs[2] = cv2.getTrackbarPos('max R/V', segmented_window)

    [limits['B']['min'], limits['G']['min'], limits['R']['min']] = mins
    [limits['B']['max'], limits['G']['max'], limits['R']['max']] = maxs

    print(limits)
    file_name = 'limits.json'
    with open(file_name, 'w') as file_handle:
        print('writing dictionary d to file ' + file_name)
        json.dump(str(limits), file_handle)  # d is the dicionary

    mask = cv2.inRange(image, mins, maxs)
    # mask = ~mask
    cv2.imshow(segmented_window, mask)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())
    window_name = 'original'
    segmented_window = 'segmented'
    image_or = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image = cv2.cvtColor(image_or, cv2.COLOR_BGR2HSV)
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image_or)

    limits = {'B': {'max': 200, 'min': 100},
               'G': {'max': 200, 'min': 100},
               'R': {'max': 200, 'min': 100}}

    cv2.namedWindow(segmented_window)

    cv2.createTrackbar('min B/H', segmented_window, 0, 255, partial(onTrackbar, segmented_window, image, limits))
    cv2.createTrackbar('max B/H', segmented_window, 0, 255, partial(onTrackbar, segmented_window, image, limits))
    cv2.createTrackbar('min G/S', segmented_window, 0, 255, partial(onTrackbar, segmented_window, image, limits))
    cv2.createTrackbar('max G/S', segmented_window, 0, 255, partial(onTrackbar, segmented_window, image, limits))
    cv2.createTrackbar('min R/V', segmented_window, 0, 255, partial(onTrackbar, segmented_window, image, limits))
    cv2.createTrackbar('max R/V', segmented_window, 0, 255, partial(onTrackbar, segmented_window, image, limits))

    cv2.waitKey(0)

if __name__ == '__main__':
    main()