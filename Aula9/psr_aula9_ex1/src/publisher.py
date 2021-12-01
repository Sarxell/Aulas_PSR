#!/usr/bin/env python3.8
# Software License Agreement (BSD License)

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from colorama import Fore,Back,Style
import argparse

def talker():
    # ----------------------------
    # initialization
    # ---------------------------
    rospy.init_node('publisher', anonymous=True)
    private_param = rospy.get_param('~rate')
    global_name = rospy.get_param("/highlight_text_color")
    print(private_param)
    pub = rospy.Publisher('chatter', String, queue_size=10)

    rate = rospy.Rate(private_param) # 10hz

    # ----------------------------
    # execution
    # ---------------------------


    while not rospy.is_shutdown():
        hello_str = getattr(Fore, str(global_name)) + 'Hello my basic program ' + str(rospy.get_time()) + Style.RESET_ALL + ''
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
