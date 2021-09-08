import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def move():
    # starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

def callback(data):
    rospy.loginfo("RECIEVED DATA: %s", data.data)
    rospy.Publisher('/turtle2/cmd_vel', turtle1_move, queue_size=10)


def listener():
    rospy.init_node("subscriber_node", anonymous = True)
    turtle1_move = rospy.Subscriber('/turtle1/cmd_vel', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
        move()
    except rospy.ROSInterruptException:
        pass
