#!/usr/bin/env python

import rospy
import smach
import time
from random import randint
from assignment4.inactive import Inactive
from assignment4.missionconfig import MissionConfig
from assignment4.preflight import PreflightChecks
from assignment4.standby import Standby
from assignment4.arming import Arming
from assignment4.takeoff import TakeOff
from assignment4.mission import Mission
from assignment4.home import ReturningHome
from assignment4.landing import Landing
from assignment4.disarming import Disarming

# define state Stop
class Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_exit'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Drone sequence stopped')
	time.sleep(2)
        return 'do_exit'

# main
def main():

    rospy.init_node('smach_turtle_dance')
    
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['do_exit'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('MissionConfig', MissionConfig(), 
                               transitions={'pass':'Inactive', 'fail':'do_exit'})
        smach.StateMachine.add('Inactive', Inactive(), 
                               transitions={'pass':'PreflightChecks', 'fail':'do_exit'})
        smach.StateMachine.add('PreflightChecks', PreflightChecks(), 
                                transitions={'pass':'Standby','fail':'Inactive'})
        smach.StateMachine.add('Standby', Standby(), 
                                transitions={'pass':'Arming','fail':'PreflightChecks'})
        smach.StateMachine.add('Arming', Arming(), 
                                transitions={'pass':'TakeOff','fail':'Standby'})
        smach.StateMachine.add('TakeOff', TakeOff(), 
                                transitions={'pass':'Mission','fail':'Arming'})
        smach.StateMachine.add('Mission', Mission(), 
                                transitions={'pass':'ReturningHome','fail':'Takeoff'})
        smach.StateMachine.add('ReturningHome', ReturningHome(), 
                                transitions={'pass':'Landing','fail':'Mission'})
        smach.StateMachine.add('TakeOff', TakeOff(), 
                                transitions={'pass':'Landing','fail':'Landing'})
        smach.StateMachine.add('Landing', Landing(), 
                                transitions={'pass':'Disarming','fail':'TakeOff'})
        smach.StateMachine.add('Disarming', Disarming(), 
                                transitions={'pass':'Inactive','fail':'do_exit'})


    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()