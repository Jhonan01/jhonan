#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
#from nav_msgs.msg    import Odometry


pub_rgb = rospy.Publisher('/camera/rgb/image_rect_color', Image, queue_size=1)
pub_depth = rospy.Publisher('/camera/depth_registered/image_raw', Image, queue_size=1)
pub_inf = rospy.Publisher('/camera/rgb/camera_info', CameraInfo, queue_size=1)
#pub_odom = rospy.Publisher('/rtabmap/odom', Odometry, queue_size=8)

def callback1(data):
    pub_rgb.publish(data)
    #rospy.sleep(1)
    print "Message callback1"

def callback2(data):
    pub_depth.publish(data)
    #rospy.sleep(1)
    print "Message callback2"

def callback3(data):
    pub_inf.publish(data)
    #rospy.sleep(1)
    print "Message callback3"

#def callback4(data):
    #pub_odom.publish(data)
    #rospy.sleep(0.2)
    #print "Message callback4"

def sub_rgbd():

    rospy.init_node('gazebo', anonymous=True)

    rospy.Subscriber('/camera/color/image_raw', Image, callback1)
    rospy.Subscriber('/camera/depth/image_raw', Image, callback2)
    rospy.Subscriber('/camera/color/camera_info', CameraInfo, callback3)
    #rospy.Subscriber('/odom', Odometry, callback4)
    rospy.spin()

if __name__ == '__main__':
    print "Running"
    sub_rgbd()
