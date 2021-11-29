#!/usr/bin/env python

from __future__ import print_function

from psr_aula8_ex4.srv import SetDogName
from psr_aula8_ex4.msg import Dog
from std_msgs.msg import String
import argparse
import rospy

pub = None


def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + 'Received a dog %s ', msg.name + ' which is ' + str(msg.age))


def handle_SetDogName(req):
    print("Returning ", req)
    return True


def SetDogName_server():
    global pub

    parser = argparse.ArgumentParser(description='Aula8_ex5')
    parser.add_argument('--topic_sub', type=str, required=True, default='Animals')
    parser.add_argument('--topic_pub', type=str, required=True, default='Name')
    parser.add_argument('--sub', type=str, required=True, default='sub')
    args = vars(parser.parse_args())

    rospy.init_node(args['sub'], anonymous=True)
    pub = rospy.Publisher(args['topic_sub'], String, queue_size=10)

    if args['topic_sub'] == 'set_dog_name':
        s = rospy.Service(args['topic_sub'], SetDogName, handle_SetDogName)
        print("Ready to change name")
    else:
        rospy.Subscriber(args['topic_sub'], Dog, callback)

    pub.publish('im trying to connect both')
    rospy.spin()


if __name__ == "__main__":
    try:
        SetDogName_server()
    except rospy.ROSInterruptException:
        pass
