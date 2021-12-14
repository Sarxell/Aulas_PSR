#!/usr/bin/env python

from visualization_msgs.msg import Marker, MarkerArray
import rospy
import math


def send_shapes():
    topic = 'visualization_marker_array'
    publisher = rospy.Publisher(topic, Marker, queue_size=10)

    rospy.init_node('register')

    while not rospy.is_shutdown():
        marker_array = MarkerArray()

        marker = Marker()
        marker.header.frame_id = "map"
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.scale.x = 1
        marker.scale.y = 1
        marker.scale.z = 1

        marker.color.a = 0.5
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = 0.0
        marker.pose.position.y = 0.0
        marker.pose.position.z = 0.0
        marker.id = 0

        marker1 = Marker()
        marker1.header.frame_id = "map"
        marker1.type = marker1.CUBE
        marker1.action = marker1.ADD
        marker1.scale.x = 1
        marker1.scale.y = 1
        marker1.scale.z = 1

        marker1.color.a = 1.0
        marker1.color.r = 1.0
        marker1.color.g = 0.0
        marker1.color.b = 0.0
        marker1.pose.orientation.w = 1.0
        marker1.pose.position.x = 1.0
        marker1.pose.position.y = 1.0
        marker1.pose.position.z = 1.0
        marker1.id = 1

        marker2 = Marker()
        marker2.header.frame_id = "map"
        marker2.type = marker2.TEXT_VIEW_FACING
        marker2.action = marker2.ADD
        marker2.scale.x = 0.2
        marker2.scale.y = 0.2
        marker2.scale.z = 0.2

        marker2.color.a = 1.0
        marker2.color.r = 1.0
        marker2.color.g = 1.0
        marker2.color.b = 1.0
        marker2.pose.orientation.w = 0.0
        marker2.pose.position.x = 1.0
        marker2.pose.position.y = 0.0
        marker2.pose.position.z = 0.0
        marker2.id = 2
        marker2.text ="the radius is 1"


        # Publish the MarkerArray
        publisher.publish(marker)
        publisher.publish(marker1)
        publisher.publish(marker2)

        rospy.sleep(0.1)


if __name__ == '__main__':
    try:
        send_shapes()
    except rospy.ROSInterruptException:
        pass
