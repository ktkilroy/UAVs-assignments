#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("RECIEVED DATA: %s", data.data)

def listener():
    rospy.init_node("subscriber_node", anonymous = True)
    rospy.Subscriber('robot_cleaner', String, callback)
    rospy.spin()
    velocity = Twist()
    velocity = data.data

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
