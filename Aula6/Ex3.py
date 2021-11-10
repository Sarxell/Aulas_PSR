#!/usr/bin/env python
import cv2
from imutils.video import FPS
from imutils import face_utils
import numpy as np
import sys


def detection(gray,image, faceCascade, mouthCascade):
    m_start, m_end = face_utils.FACIAL_LANDMARKS_IDXS['mouth']

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30),
                                         flags=cv2.CASCADE_SCALE_IMAGE)

    mouth = mouthCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=20, minSize=(30, 30)
                                          , flags=cv2.CASCADE_SCALE_IMAGE)

    max_area = 0
    area = 0
    print(m_start, m_end)
    # Initialize black image of same dimensions for drawing the rectangles
    blk = np.zeros(image.shape, np.uint8)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        area = h * w
        if area > max_area:
            max_area = area
            cv2.rectangle(blk, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

    max_area_mouth = 0

    for (x, y, w, h) in mouth:
        area_mouth = h * w
        if area_mouth > max_area_mouth:
            max_area_mouth = area
            cv2.rectangle(blk, (x, y), (x + w, y + h), (0, 0, 255), cv2.FILLED)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)



    # Generate result by blending both images (opacity of rectangle image is 0.25 = 25 %)
    out = cv2.addWeighted(image, 1.0, blk, 0.25, 1)

    return out


def main():
    # initial setup
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    mouthCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FPS, 15)
    fps = FPS().start()
    window_name = 'A5-Ex2'

    cv2.namedWindow(window_name,  cv2.WINDOW_AUTOSIZE)

    while 1:

        _, image = capture.read()   # get an image from the camera

        image = cv2.resize(image, (960, 700))
        cv2.imshow(window_name, image)    # add code to show acquired image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        image_final = detection(gray, image, faceCascade, mouthCascade)
        cv2.imshow(window_name, image_final)

        fps.update()
        if cv2.waitKey(40) & 0xFF == 27:   # add code to wait for a key press
            break

    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()