#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('gazebo', anonymous=True)

time_start = time.time()
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

r = rospy.Rate(10)

while not rospy.is_shutdown():
    msg = Twist()

    while(time.time() - time_start < 9.40):
        msg.angular.z = 0.5
        pub.publish(msg)
        r.sleep()

    msg.angular.z = 0.0
    while(time.time() - time_start < 20.0):
        msg.linear.x = 0.5
        pub.publish(msg)
        r.sleep()

    while(time.time() - time_start < 31.0):
        msg.angular.z = -0.5
        pub.publish(msg)
        r.sleep()
    
    msg.angular.z = 0.0

    while(time.time() - time_start < 50.0):
        msg.linear.z = -0.5
        pub.publish(msg)
        r.sleep()




    





