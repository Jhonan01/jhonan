import rospy
from geometry_msgs.msg import Twist

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
rospy.init_node('/teleop_twist_keyboard')
r = rospy.Rate(30) # 30hz

total_time = 10 #seconds
start_time = time.time()

while not rospy.is_shutdown() or (time.time() - start_time < total_time):

    msg = Twist()

    # here you should fill the msg fields
    # http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html
    # you can fill it randomly or with a direction in mind
    rostopic pub /cmd_vel geometry_msgs/Twist -r 10 -- '[0.3, 0.0, 0.0]' '[0.0, 0.0, -0.9]'

    pub.publish(msg)
    r.sleep()
