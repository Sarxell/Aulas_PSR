#!/usr/bin/env python3

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from psr_aula8_ex4.msg import Dog
from std_msgs.msg import String
import argparse


def callback(msg):
    msg_stamp = msg.header.stamp
    stamp_now = rospy.Time.now()
    duration = (msg_stamp - stamp_now).to_sec()
    rospy.loginfo(rospy.get_caller_id() + 'I heard  %s',  + ' ' + str(duration))



def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('chatter', Dog, callback)

    # ----------------------------
    # execution
    # ---------------------------
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
