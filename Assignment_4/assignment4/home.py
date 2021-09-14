#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

class home(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['pass', 'fail'])

    def execute(self, userdata):
        rospy.loginfo('Returning home')
        num = randint(1, 10)
        rospy.loginfo('The number is: %s', num)
        if  (num > 1):
            rospy.loginfo('Sucessfully returned home')
            return 'pass'
        else:
            rospy.loginfo('failed to return home')
            return 'fail'