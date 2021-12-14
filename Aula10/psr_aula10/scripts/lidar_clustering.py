#!/usr/bin/env python3

import random
import sensor_msgs.point_cloud2 as pc2
import rospy
import std_msgs.msg
from sensor_msgs import point_cloud2
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan, PointCloud2, PointField
import laser_geometry.laser_geometry as lg
from geometry_msgs.msg import Point
import math
from visualization_msgs.msg import Marker, MarkerArray

pub = rospy.Publisher("marker_array", MarkerArray, queue_size=1)


def createMarker(id):
    marker = Marker()
    marker.id = id
    marker.header.frame_id = "left_laser"
    marker.type = marker.CUBE_LIST
    marker.action = marker.ADD
    marker.scale.x = 0.2
    marker.scale.y = 0.2
    marker.scale.z = 0.2
    marker.color.r = random.random()
    marker.color.g = random.random()
    marker.color.b = random.random()
    marker.color.a = 1.0
    marker.pose.orientation.w = 1.0
    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    return marker

def callback(msg):

    rospy.loginfo('LaserScan message received')
    thresh = 0.8
    marker_array = MarkerArray()
    marker = createMarker(0)
    marker_array.markers.append(marker)

    for idx, (range1, range2) in enumerate(zip(msg.ranges[:-1], msg.ranges[1:])):
        if range1 < 0.1 or range2 < 0.1:
            continue

        diff = abs(range2 - range1)
        if diff > thresh:
            marker = createMarker(idx + 1)
            marker_array.markers.append(marker)

        theta = msg.angle_min + idx * msg.angle_increment
        x = range1 * math.cos(theta)
        y = range1 * math.sin(theta)

        point = Point(x=x, y=y, z=0)

        last_marker = marker_array.markers[-1]
        last_marker.points.append(point)

    pub.publish(marker_array)


def lidar_subscriber():
    #------------------------------------------------
    #Initialization
    # ------------------------------------------------

    rospy.init_node('PolarToCartesian', anonymous=True)
    rospy.Subscriber('/left_laser/laserscan', LaserScan, callback, queue_size=1)

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    rospy.spin()


if __name__ == '__main__':
    try:
        lidar_subscriber()
    except rospy.ROSInterruptException:
        pass