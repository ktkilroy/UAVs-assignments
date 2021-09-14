#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

class preflight(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['pass', 'fail'])

    def execute(self, userdata):
        rospy.loginfo('Preforming preflight checks')
        num = randint(1, 10)
        rospy.loginfo('The number is: %s', num)
        if  (num > 1):
            rospy.loginfo('Preflight checks sucessfully completed')
            return 'pass'
        else:
            rospy.loginfo('Preflight checks unsucessfully completed')
            return 'fail'