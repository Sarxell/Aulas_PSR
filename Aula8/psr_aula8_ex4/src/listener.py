#!/usr/bin/env python3

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
import argparse
from psr_aula8_ex4.msg import Dog

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + 'Received a dog %s ', msg.name + 'wich is ' + str(msg.age))

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    parser = argparse.ArgumentParser(description='PSR argparse example')
    parser.add_argument('--topic', type=str, required=True, default='chatter')
    parser.add_argument('--topic2', type=str)
    parser.add_argument('--sub', type=str, required=True, default='sub')
    args = vars(parser.parse_args())

    rospy.init_node(args['sub'], anonymous=True)
    rospy.Subscriber(args['topic'], Dog , callback)
    if args['topic2']:
        rospy.Subscriber(args['topic2'], String, callback)


    # ----------------------------
    # execution
    # ---------------------------
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
