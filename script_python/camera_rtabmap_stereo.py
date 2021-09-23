#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
#from nav_msgs.msg    import Odometry


pub_rgb = rospy.Publisher('/stereo_camera/left/image_rect_color', Image, queue_size=1)
pub_depth = rospy.Publisher('/stereo_camera/right/image_rect', Image, queue_size=1)
pub_inf_l = rospy.Publisher('/stereo_camera/left/camera_info', CameraInfo, queue_size=1)
pub_inf_r = rospy.Publisher('/stereo_camera/right/camera_info', CameraInfo, queue_size=1)

def callback1(data):
    pub_rgb.publish(data)
    #rospy.sleep(1)
    print "Message callback1"

def callback2(data):
    pub_depth.publish(data)
    #rospy.sleep(1)
    print "Message callback2"

def callback3(data):
    pub_inf_l.publish(data)
    #rospy.sleep(1)
    print "Message callback3"

def callback4(data):
    pub_inf_r.publish(data)
    #rospy.sleep(0.2)
    print "Message callback4"

def sub_rgbd():

    rospy.init_node('gazebo', anonymous=True)

    rospy.Subscriber('/multisense_sl/camera/left/image_raw', Image, callback1)
    rospy.Subscriber('/multisense_sl/camera/right/image_raw', Image, callback2)
    rospy.Subscriber('/multisense_sl/camera/left/camera_info', CameraInfo, callback3)
    rospy.Subscriber('/multisense_sl/camera/right/camera_info', CameraInfo, callback4)
    rospy.spin()

if __name__ == '__main__':
    print "Running"
    sub_rgbd()
