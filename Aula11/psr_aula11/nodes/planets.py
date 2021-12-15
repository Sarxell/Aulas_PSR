#!/usr/bin/env python
import rospy
import tf2_ros
import geometry_msgs.msg
import math

if __name__ == '__main__':
    rospy.init_node('dynamic_tf2_broadcaster')

    planet_parent = rospy.get_param('~planet_parent')
    planet_child = rospy.get_param('~planet_child')
    distancex = rospy.get_param('~distancex')
    distancey = rospy.get_param('~distancey')
    velocity = rospy.get_param('~velocity')

    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.frame_id = planet_parent
    t.child_frame_id = planet_child

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        x = rospy.Time.now().to_sec() * velocity

        t.header.stamp = rospy.Time.now()
        t.transform.translation.x = distancex * math.sin(x)
        t.transform.translation.y = distancey * math.cos(x)
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        br.sendTransform(t)
        rate.sleep()