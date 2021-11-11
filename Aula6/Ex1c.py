#!/usr/bin/python3

import cv2
import numpy as np
from functools import partial

drawing = False  # true if mouse is pressed
pt1_x, pt1_y = None, None


# mouse callback function
def line_drawing(img, color, event, x, y, flags, param):
    global pt1_x, pt1_y, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pt1_x, pt1_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img, (pt1_x, pt1_y), (x, y), color=color, thickness=3)
            pt1_x, pt1_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (pt1_x, pt1_y), (x, y), color=color, thickness=3)


def main():
    img = np.zeros((400, 600, 3), np.uint8)
    img.fill(255)
    cv2.namedWindow('Ex 1c')
    img = cv2.resize(img, (960, 540))
    color = (0, 0, 255)
    while 1:
        cv2.imshow('Ex 1c', img)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('r'):
            color = (0, 0, 255)
        if key & 0xFF == ord('b'):
            color = (255, 0, 0)
        if key & 0xFF == ord('g'):
            color = (0, 255, 0)

        cv2.setMouseCallback('Ex 1c', partial(line_drawing, img, color))

        if key & 0xFF == 27:
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()