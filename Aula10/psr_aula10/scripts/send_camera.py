#!/usr/bin/env python3

## receives messages of type sensor_msgs/laserscan,
# converts the information in these messages to polar coordinates
# to cartesian coordinates, in a way to construct a message of type sensor_msgs/PointCloud2.


import rospy
from sensor_msgs.msg import *
from cv_bridge import CvBridge
import cv2
from imutils.video import VideoStream


def send_camera():

    # ----------------------------
    # initialization
    # ---------------------------
    rospy.init_node('send_camera')
    pc_pub = rospy.Publisher('msg_pub', Image, queue_size=1)
    capture = cv2.VideoCapture(0)

    # ----------------------------
    # execution
    # ---------------------------
    # spin() simply keeps python from exiting until this node is stopped

    while 1:
        # initial setup
        _, cv_image = capture.read()
        bridge = CvBridge()

        image_message = bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")

        if cv2.waitKey(1) & 0xFF == 27:  # add code to wait for a key press
            break

        # publish it
        pc_pub.publish(image_message)

    cv2.destroyAllWindows()

    rospy.spin()



if __name__ == '__main__':
    try:
        send_camera()
    except rospy.ROSInterruptException:
        pass
