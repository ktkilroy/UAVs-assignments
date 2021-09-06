#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Recieving the user's input
    print("Let's move your robot")
    speed = input("Input your speed:")
    distance = input("Type your distance:")
    isForward = input("Forward?:")#True or False



    #checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    #since we are movin just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        #setting the surrent time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

    #loop to move the turtle in a specific distance
    while (current_distance < distance):
        #publish the velocity
        velocity_publisher.publish(vel_msg)
        #takes the actual time to velocity calculus
        t1 = rospy.Time.now().to_sec()
        #calculate distancePoseStamped
        current_distance = speed*(t1-t0)
    #after the loop, stops the robot
    vel_msg.linear.x = 0
    #force the robot to stop
    velocity_publisher.publish(vel_msg)

if _name_ == '_main_':
    try:
        #testing our function
        move()
    except rospy.RosInterruptionException: pass


    