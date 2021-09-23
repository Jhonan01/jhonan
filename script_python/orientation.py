#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

rospy.init_node("speed_controller")
r = rospy.Rate(4)

def orientation(msg):

    global theta

    rot_q = msg.pose.pose.orientation
    (_, _, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    print(theta)


while not rospy.is_shutdown():

    sub = rospy.Subscriber("/odom", Odometry, orientation)
    r.sleep()
