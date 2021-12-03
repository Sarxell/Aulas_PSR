#!/usr/bin/env python3.8
# Software License Agreement (BSD License)

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from colorama import Fore,Back,Style
from psr_aula8_ex4.msg import Dog
import argparse

def talker():
    # ----------------------------
    # initialization
    # ---------------------------
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)

    # ----------------------------
    # execution
    # ---------------------------


    while not rospy.is_shutdown():
        private_param = rospy.get_param('~rate', default=10)
        global_name = rospy.get_param("/highlight_text_color")
        rate = rospy.Rate(private_param)  # 10hz
        dog = Dog()

        dog.name = "max"
        dog.age = 18
        dog.color = 'black'
        dog.brothers.append('lilly')
        dog.brothers.append('boby')
        dog.header.stamp = rospy.Time.now()

        rospy.loginfo(getattr(Fore, str(global_name)) + 'my dog info is...' + Style.RESET_ALL)
        pub.publish(dog)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
