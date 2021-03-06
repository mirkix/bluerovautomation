#!/usr/bin/env python2

import cv2
import rospy
import time
import math as m
try:
    import pubs
    import subs
except:
    import bluerov.pubs as pubs
    import bluerov.subs as subs

from mavros_msgs.srv import CommandBool
from sensor_msgs.msg import Joy, JointState
from std_msgs.msg import Float32
from bluerov_ros_playground.msg import Custom

class Joystick(object):

    """Class to provide user access

    Attributes:
        pub (Pub): Pub object, do topics publication
        sub (Sub): Sub object, subscribe in topics
    """

    curr_pitch_setting = 0.0
    curr_roll_setting = 0.0
    curr_gain_setting = 1
    gain = [0.25, 0.5, 0.75, 1]

    def enforce_limit(self, value):
        if (value < -1.0):
            value = -1.0
        elif (value > 1.0):
            value = 1.0
        return value

    def limit_gain(self, value):
        if (value < 0):
            value = 0
        elif (value > 3):
            value = 3
        return value

    def __init__(self):
        super(Joystick, self).__init__()

        self.sub = subs.Subs()
        self.pub = pubs.Pubs()
	self.pub.subscribe_topic('/act', Custom)
        self.sub.subscribe_topic('/joy', Joy)


    def run(self):
        """Run user code
        """

        while not rospy.is_shutdown():
            time.sleep(0.1)

            try:
                # Get joystick data
                joy = self.sub.get_data()['joy']['axes']
                but = self.sub.get_data()['joy']['buttons']
		# Converting button presses to roll and pitch setting modification
		self.curr_pitch_setting = self.enforce_limit(self.curr_pitch_setting - joy[7]*0.1)
		self.curr_roll_setting = self.enforce_limit(self.curr_roll_setting - joy[6]*0.1)
                self.curr_gain_setting = self.limit_gain(self.curr_gain_setting + but[7] - but[6])
                g = self.gain[self.curr_gain_setting]
                print 'gain:', g
		if (but[4] == 1):
		    self.curr_pitch_setting = 0.0
		if (but[5] == 1):
		    self.curr_roll_setting = 0.0                    
		
		forces = [0.0, 0.0, 0.0]
		torques = [0.0, 0.0, 0.0]
		
		forces[0] = joy[1]*g #Surge
		forces[1] = joy[3]*g #Sway
		forces[2] = joy[4]*g #Heave
		torques[0] = self.curr_roll_setting #Roll
		torques[1] = self.curr_pitch_setting #Pitch
		torques[2] = joy[0]*g #Yaw
                forces = forces + torques

		data = Custom()
		data.id = "joystick"
		data.data = forces
		self.pub.set_data('/act', data)

            except Exception as error:
                print('joy error:', error)

if __name__ == "__main__":
    try:
        rospy.init_node('joystick_node', log_level=rospy.DEBUG)
    except rospy.ROSInterruptException as error:
        print('pubs error with ROS: ', error)
        exit(1)
    code = Joystick()
    code.run()

