#!/usr/bin/env python3.8
import copy
import math

import rospy
import tf2_ros
from geometry_msgs.msg import Twist, PoseStamped
import tf2_geometry_msgs # Do not use geometry_msgs. Use this for PoseStamped (depois perguntar porque)


class Driver:

    def __init__(self):
        # Define the goal to which the robot should move
        self.goal = PoseStamped
        self.goal_active = False

        self.tf_buffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tf_buffer)
        self.publisher_command = rospy.Publisher('/p_spombinho/cmd_vel', Twist, queue_size=1)
        self.timer = rospy.Timer(rospy.Duration(0.1), self.sendCommandCallback)
        self.goal_subscriber = rospy.Subscriber('/move_base_simple/goal', PoseStamped, self.goalReceivedCallBack)

    def goalReceivedCallBack(self, goal_msg):

        self.goal = goal_msg # storing the goal inside the class
        self.goal_active = True

    def sendCommandCallback(self, msg):

        # Decision outputs a speed (linear velocity) and an angle (angular velocity)
        # input : goal
        # output : angle and speed

        # verify if the goal is achieved
        if self.goal_active:
            distance_to_goal = self.computeDistanceToGoal(self.goal)
            if distance_to_goal < 0.05:
                rospy.logwarn('I have achieved my goal!!!')
                self.goal_active = False

        # define driving behaviour according to the goal
        if self.goal_active:
            angle, speed = self.driveStraight(self.goal)
            if angle is None or speed is None: # can't transform target frame
                angle = 0
                speed = 0
        else:
            angle = 0
            speed = 0

        # Build the command message (Twist) and publish it
        command_msg = Twist()
        command_msg.linear.x = speed
        command_msg.angular.z = angle
        self.publisher_command.publish(command_msg)

    def computeDistanceToGoal(self, goal):

        goal_present_time = copy.deepcopy(goal)
        goal_present_time.header.stamp = rospy.Time.now()

        target_frame = 'p_spombinho/base_link'
        try:
            goal_in_base_link = self.tf_buffer.transform(goal_present_time, target_frame, rospy.Duration(1))
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.logerr(
                'Could not transform goal from ' + goal.header.frame_id + ' to ' + target_frame + '. Will ignore this goal')
            return None, None

        x = goal_in_base_link.pose.position.x
        y = goal_in_base_link.pose.position.y

        distance = math.sqrt(x**2 + y**2)
        return distance

    def driveStraight(self, goal, minimum_speed=0.1, maximum_speed=1.0):
        """
        :param goal:
        :param minimum_speed:
        :param maximum_speed:
        :return: the angle and speed to use as command
        """
        goal_present_time = copy.deepcopy(goal)
        goal_present_time.header.stamp = rospy.Time.now()

        target_frame = 'p_spombinho/base_link'
        try:
            goal_in_base_link = self.tf_buffer.transform(goal_present_time, target_frame, rospy.Duration(1))

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.logerr('Could not transform goal from ' + goal.header.frame_id + ' to ' + target_frame + '. Will ignore')
            return None, None

        x = goal_in_base_link.pose.position.x
        y = goal_in_base_link.pose.position.y

        angle = math.atan2(y,x) # compute the angle

        distance = math.sqrt(x**2 + y**2)
        speed = 0.5 * distance
        # saturates the speed to minimum and maximum values
        speed = min(speed, maximum_speed)
        speed = max(speed, minimum_speed)

        return angle, speed



def main():
    rospy.init_node('p_spombinho_driver', anonymous=False)
    driver = Driver()
    rospy.spin()


if __name__ == '__main__':
  main()