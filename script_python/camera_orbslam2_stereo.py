#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image


pub_rgb = rospy.Publisher('/camera/left/image_raw', Image, queue_size=8)
pub_depth = rospy.Publisher('/camera/right/image_raw', Image, queue_size=8)

def callback1(data):
    pub_rgb.publish(data)
    #rospy.sleep(1)
    print "Message callback1"

def callback2(data):
    pub_depth.publish(data)
    #rospy.sleep(1)
    print "Message callback2"

def sub_rgbd():

    rospy.init_node('gazebo', anonymous=True)

    rospy.Subscriber('/multisense_sl/camera/left/image_raw', Image, callback1)
    rospy.Subscriber('/multisense_sl/camera/right/image_raw', Image, callback2)
    rospy.spin()

if __name__ == '__main__':
    print "Running"
    sub_rgbd()
