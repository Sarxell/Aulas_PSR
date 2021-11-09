#!/usr/bin/env python
import cv2
from imutils.video import FPS


def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FPS, 15)
    fps = FPS().start()
    window_name = 'A5-Ex2'

    cv2.namedWindow(window_name,  cv2.WINDOW_AUTOSIZE)

    while 1:

        _, image = capture.read()   # get an image from the camera

        cv2.imshow(window_name, image)    # add code to show acquired image
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