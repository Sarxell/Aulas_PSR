#!/usr/bin/env python

# import the necessary packages
import copy
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import dlib
import cv2
import numpy as np
from colorama import Fore,Back, Style


def is_speaking(prev_img, curr_img, threshold, width=400, height=400):
    """
    Args:
        prev_img:
        curr_img:
    Returns:
        Bool value if a person is speaking or not
    """
    prev_img = cv2.resize(prev_img, (width, height))
    curr_img = cv2.resize(curr_img, (width, height))

    diff = cv2.absdiff(prev_img, curr_img)
    norm = np.sum(diff) / (width * height) * 100

    return norm > threshold


def main():

    # --------------------------------
    # INITIALIZATION
    # ---------------------------------
    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # grab the indices of the facial landmarks for mouth
    m_start, m_end = face_utils.FACIAL_LANDMARKS_IDXS['mouth']

    # initialize the video stream and allow the cammera sensor to warmup
    print("[INFO] camera sensor warming up...")
    vs = VideoStream(0).start()
    time.sleep(2.0)

    prev_mouth_img = None
    i = 0
    margin = 10


    # --------------------------------
    # EXECUTION
    # ---------------------------------
    while True:
        # grab the frame from the threaded video stream, resize it to
        # have a maximum width of 400 pixels, and convert it to
        # grayscale
        frame = vs.read()
        frame = imutils.resize(frame, width=600)
        blk = np.zeros(frame.shape, np.uint8)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame1 = copy.deepcopy(frame)

        # edges
        edges = cv2.Canny(frame1, 100, 200)
        rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
        # step 2: now all edges are white (255,255,255). to make it red, multiply with another array:
        rgb *= np.array((0, 0, 1), np.uint8)  # set g and b to 0, leaves red :)

        mask = np.zeros(frame.shape, np.uint8)


        # detect faces in the grayscale frame
        rects = detector(gray, 0)
        area = 0
        max_area = 0
        area_mouth = 0
        max_area_mouth = 0


        # loop over the face detections
        for rect in rects:
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            x = rect.left()
            y = rect.top()  # could be face.bottom() - not sure
            w = rect.right() - rect.left()
            h = rect.bottom() - rect.top()

            area = h*w

            rgb[y:y+h, x:x+w] = frame1[y:y+h, x:x+w]
            # step 3: compose:
            edges = np.bitwise_or(frame1, rgb)
            frame1 = edges

            if area > max_area:
                max_area = area
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.rectangle(blk, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)

            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            mouth_shape = shape[m_start:m_end + 1]

            leftmost_x = min(x for x, y in mouth_shape) - margin
            bottom_y = min(y for x, y in mouth_shape) - margin
            rightmost_x = max(x for x, y in mouth_shape) + margin
            top_y = max(y for x, y in mouth_shape) + margin

            w1 = rightmost_x - leftmost_x
            h1 = top_y - bottom_y

            x = int(leftmost_x - 0.1 * w1)
            y = int(bottom_y - 0.1 * h1)

            # optional just to be bigger
            w1 = int(1.1 * w1)
            h1 = int(1.1 * h1)

            # get the mouth image, in this case using the gray
            mouth_img = gray[bottom_y:top_y, leftmost_x:rightmost_x]

            area_mouth = h1*w1

            if area_mouth > max_area_mouth:
                max_area_mouth = area_mouth
                cv2.rectangle(frame1, (x, y), (x + w1, y + h1), (0, 0, 255), 2)
                mask = cv2.rectangle(blk, (x, y), (x + w1, y + h1), (0, 0, 255), cv2.FILLED)


            frame1 = cv2.addWeighted(frame1, 1.0, blk, 0.25, 1)

            if prev_mouth_img is None:
                prev_mouth_img = mouth_img
            if is_speaking(prev_mouth_img, mouth_img, threshold=350):
                cv2.putText(frame1, "The person is speaking", (10, 50), cv2.FONT_HERSHEY_PLAIN, 1,
                            (0, 255, 0))
                print(Fore.GREEN + "The person is speaking" + Style.RESET_ALL , end='\r')
            else:
                cv2.putText(frame1, "The person is not speaking", (10, 50), cv2.FONT_HERSHEY_PLAIN, 1,
                            (0, 0, 255))
                print( Fore.RED + "The person is NOT speaking" + Style.RESET_ALL , end='\r')

            prev_mouth_img = mouth_img

            cv2.imshow('mouth', mouth_img)
        # show the frame
        cv2.imshow("edges", edges)
        cv2.imshow("mask face", mask)
        cv2.imshow("Frame", frame1)
        cv2.imshow("Original", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the Esc key was pressed, break from the loop
        if key == 27:
            break

    # do a bit of cleanup

    # -------
    # termination
    # ----------

    cv2.destroyAllWindows()
    vs.stop()

if __name__ == '__main__':
    main()