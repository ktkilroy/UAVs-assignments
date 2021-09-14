#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

class mission(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['pass', 'fail'])

    def execute(self, userdata):
        rospy.loginfo('Preforming Mission')
        num = randint(1, 10)
        rospy.loginfo('The number is: %s', num)
        if  (num > 1):
            rospy.loginfo('Drone completing missions')
            return 'pass'
        else:
            rospy.loginfo('Missions Failed')
            return 'fail'