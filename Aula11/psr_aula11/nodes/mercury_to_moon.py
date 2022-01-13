#!/usr/bin/env python3
import rospy

import math
import tf2_ros
from std_msgs.msg import String
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('planet_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    Mercury = rospy.get_param('planet_parent', 'Mercury')
    Moon = rospy.get_param('planet_child', 'Moon')
    pub = rospy.Publisher('planets/distance', geometry_msgs.msg.Twist, queue_size=1)
    rate = rospy.Rate(1.0)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform(Moon, 'Mercury', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        msg = geometry_msgs.msg.Twist()

        msg.angular.z = 0.0
        msg.linear.x = abs(math.sqrt(trans.transform.translation.x ** 2 + trans.transform.translation.y ** 2))

        pub.publish(msg)


        rate.sleep()
