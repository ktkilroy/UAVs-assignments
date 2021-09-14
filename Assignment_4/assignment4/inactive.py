#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

class onground(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['pass', 'fail'])

    def execute(self, userdata):
        rospy.loginfo('Checking drone state')
        num = randint(1, 10)
        rospy.loginfo('The number is: %s', num)
        if  (num > 1):
            rospy.loginfo('The drone is inactive or on the ground')
            return 'pass'
        else:
            rospy.loginfo('The drone is in an active state')
            return 'fail'