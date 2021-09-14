#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

class landing(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['pass', 'fail'])

    def execute(self, userdata):
        rospy.loginfo('Drone beginning landing sequence')
        num = randint(1, 10)
        rospy.loginfo('The number is: %s', num)
        if  (num > 1):
            rospy.loginfo('Drone has landed')
            return 'pass'
        else:
            rospy.loginfo('failure during landing')
            return 'fail'