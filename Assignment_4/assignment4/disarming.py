#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

class disarming(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['pass', 'fail'])

    def execute(self, userdata):
        rospy.loginfo('Preparing to disarm drone')
        num = randint(1, 10)
        rospy.loginfo('The number is: %s', num)
        if  (num > 1):
            rospy.loginfo('Drone disarmed')
            return 'pass'
        else:
            rospy.loginfo('Failure to disarm drone')
            return 'fail'