#!/usr/bin/env python

from __future__ import print_function

from psr_aula8_ex4.srv import SetDogName
from psr_aula8_ex4.msg import Dog
from std_msgs.msg import String
import argparse
import rospy

pub = None


def callback(msg):
    pub.publish(msg.name)


def caller1():
    global pub

    parser = argparse.ArgumentParser(description='Aula8_ex5')
    parser.add_argument('--topic_pub', type=str, required=True, default='Name')
    args = vars(parser.parse_args())

    rospy.init_node('caller1', anonymous=True)
    rospy.Subscriber('chatter2', Dog, callback)

    if args['topic_pub'] == 'set_dog_name':
        SetDogName_server()
        pub = rospy.Publisher(args['topic_pub'], String, queue_size=10)
    else:
        pub = rospy.Publisher(args['topic_pub'], String, queue_size=10)
    rospy.spin()


def handle_SetDogName(req):
    print("Returning ", req)
    return True


def SetDogName_server():
    s = rospy.Service('set_dog_name', SetDogName, handle_SetDogName)
    print("Ready to change name")


if __name__ == '__main__':
    try:
        caller1()
    except rospy.ROSInterruptException:
        pass
