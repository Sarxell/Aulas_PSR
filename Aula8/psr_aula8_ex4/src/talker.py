#!/usr/bin/env python
# Software License Agreement (BSD License)

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
import argparse
from psr_aula8_ex4.msg import Dog

def talker():
    # ----------------------------
    # initialization
    # ---------------------------

    parser = argparse.ArgumentParser(description='PSR argparse example')
    parser.add_argument('--rate', type=float, required=True, default=1)
    parser.add_argument('--topic', type=str, required=True, default='politics')
    parser.add_argument('--topic2', type=str)
    parser.add_argument('--pub', type=str, required=True, default='pub')
    parser.add_argument('--message', type=str, default='I dont know what to say')
    args = vars(parser.parse_args())

    rospy.init_node(args['pub'], anonymous=True)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)
    if args['topic2']:
        pub = rospy.Publisher(args['topic2'], String, queue_size=10)

    rate = rospy.Rate(args['rate']) # 10hz

    # ----------------------------
    # execution
    # ---------------------------

    while not rospy.is_shutdown():
        hello_str = args['message'] + ' ' + str(rospy.get_time())
        rospy.loginfo(hello_str)

        dog = Dog()
        dog.name = 'max'
        dog.age = 18
        dog.color = 'black'
        dog.brothers.append('lilly')
        dog.brothers.append('boby')

        pub.publish(dog)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
