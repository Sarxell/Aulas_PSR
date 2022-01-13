#!/usr/bin/env python
import rospy
import tf2_ros
import geometry_msgs.msg
import math

if __name__ == '__main__':
    rospy.init_node('dynamic_tf2_broadcaster')

    planet_parent = rospy.get_param('~planet_parent')
    planet_child = rospy.get_param('~planet_child')
    distance = rospy.get_param('~distance')
    velocity = rospy.get_param('~velocity')

    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.frame_id = planet_parent
    t.child_frame_id = planet_child

    rate = rospy.Rate(10.0)
    alpha = 0
    while not rospy.is_shutdown():
        alpha += (1/velocity)/100
        if alpha > 2*math.pi:
            alpha = 0

        t.header.stamp = rospy.Time.now()
        t.transform.translation.x = distance * math.sin(alpha)
        t.transform.translation.y = distance * math.cos(alpha)
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        br.sendTransform(t)
        rate.sleep()