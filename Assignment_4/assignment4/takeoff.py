#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

class takeoff(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['pass', 'fail'])

    def execute(self, userdata):
        rospy.loginfo('Beginning takeoff sequence')
        num = randint(1, 10)
        rospy.loginfo('The number is: %s', num)
        if  (num > 1):
            rospy.loginfo('Successfully completed takeoff')
            return 'pass'
        else:
            rospy.loginfo('Failure during takeoff')
            return 'fail'