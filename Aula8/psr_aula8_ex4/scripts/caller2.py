#!/usr/bin/env python

from __future__ import print_function

import sys
from std_msgs.msg import String
from psr_aula8_ex4.msg import Dog
import argparse
import rospy
from psr_aula8_ex4.srv import *

def callback(msg):
    print('The name of the dog is ' + msg.data)


def SetDogName_client(dog):
    rospy.wait_for_service('set_dog_name')
    try:
        Dog_name = rospy.ServiceProxy('set_dog_name', SetDogName)
        resp = Dog_name(dog)
        return resp
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def caller2():

    parser = argparse.ArgumentParser(description='Aula8_ex5')
    parser.add_argument('--topic_sub', type=str, required=True, default='Animals')
    parser.add_argument('--name', type=str, default='max')
    args = vars(parser.parse_args())

    pub = rospy.Publisher('chatter2', Dog, queue_size=10)
    rospy.init_node('caller2', anonymous=True)
    rospy.Subscriber(args['topic_sub'], String, callback)
    rate = rospy.Rate(1) # 10hz

    while not rospy.is_shutdown():
        doggy = Dog()

        if args['topic_sub'] == 'set_dog_name':
            SetDogName_client(args['name'])
            doggy.name = args['name']
        else:
            doggy.name = "max"

        doggy.age = 18
        doggy.color = 'black'
        doggy.brothers.append('lilly')
        doggy.brothers.append('boby')

        pub.publish(doggy)
        rate.sleep()
    rospy.spin()


if __name__ == '__main__':
    try:
        caller2()
    except rospy.ROSInterruptException:
        pass
