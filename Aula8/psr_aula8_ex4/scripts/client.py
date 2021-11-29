#!/usr/bin/env python

from __future__ import print_function

import sys
from std_msgs.msg import String
from psr_aula8_ex4.msg import Dog
import argparse
import rospy
from psr_aula8_ex4.srv import *

name = 'max'

def callback(msg):
    print('%s' % msg.data)


def SetDogName_client(dog):
    global name

    parser = argparse.ArgumentParser(description='PSR argparse example')
    parser.add_argument('--rate', type=float, required=True, default=1)
    parser.add_argument('--topic_pub', type=str, required=True, default='Name')
    parser.add_argument('--topic_sub', type=str, required=True, default='Animals')
    parser.add_argument('--pub', type=str, required=True, default='pub')
    parser.add_argument('--message', type=str, required=True,default='au au')

    args = vars(parser.parse_args())

    rospy.init_node(args['pub'], anonymous=True)
    rospy.Subscriber(args['topic_sub'], String, callback)

    dog = args['message']

    if args['topic_pub'] == 'set_dog_name':
        rospy.wait_for_service(args['topic_pub'])
    else:
        pub = rospy.Publisher(args['topic_pub'], Dog, queue_size=10)

    rate = rospy.Rate(args['rate'])

    try:
        Dog_name = rospy.ServiceProxy('set_dog_name', SetDogName)
        resp = Dog_name(dog)
        return resp
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

    while not rospy.is_shutdown():
        hello_str = args['message'] + ' ' + str(rospy.get_time())
        rospy.loginfo(hello_str)

        doggy = Dog()
        doggy.name = dog
        doggy.age = 18
        doggy.color = 'black'
        doggy.brothers.append('lilly')
        doggy.brothers.append('boby')

        pub.publish(doggy)
        rate.sleep()
    rospy.spin()



def usage():
    return "%s "%sys.argv[0]


if __name__ == "__main__":
    dog = name
    try:
        SetDogName_client(dog)
    except rospy.ROSInterruptException:
        pass

