#!/usr/bin/env python2

import cv2
import rospy
import time
import math as m
try:
    import pubs
    import subs
    import video
except:
    import bluerov.pubs as pubs
    import bluerov.subs as subs
    import bluerov.video as video

from mavros_msgs.srv import CommandBool
from sensor_msgs.msg import Joy
from nav_msgs.msg import Odometry
from mavros_msgs.msg import OverrideRCIn, RCIn, RCOut
from std_msgs.msg import Float32
from bluerov_ros_playground.msg import Custom

def Angle(des, curr):
    x = 3.14 - abs(des) + 3.14 - abs(curr)
    if abs(des - curr) > x:
        if (des-curr)>0:
            return x
        else:
            return -x
    else:
        return curr-des

def Val(old, curr, des):
    if ((old > 0 and curr < 0) or (old < 0 and curr > 0)):
        if (abs(old - des) > 2):
            x = 3.14 - abs(old - des) + 3.14 - abs(curr - des)
            return x
        else:
            return curr - old
    else:
        return curr - old

def error(er):
    if (abs(er > 20)):
        er = 20 * er / abs(er)
    return er

class Auto(object):

    """Class to provide user access

    Attributes:
        cam (Video): Video object, get video stream
        pub (Pub): Pub object, do topics publication
        sub (Sub): Sub object, subscribe in topics
    """

    curr_pitch_setting = 0.0
    curr_roll_setting = 0.0 

    def enforce_limit(self, value):
        if (value < -1.0):
            value = -1.0
        elif (value > 1.0):
            value = 1.0
        return value

    def __init__(self):
        super(Auto, self).__init__()

        self.sub = subs.Subs()
        self.pub = pubs.Pubs()

	self.pub.subscribe_topic('/auto', Custom)
        self.pub.subscribe_topic('/next_pos', Custom)

        self.sub.subscribe_topic('/joy', Joy)
	self.sub.subscribe_topic('/odom', Odometry)
	self.sub.subscribe_topic('/odometry/filtered', Odometry)

    def run(self):
        """Run user code
        """

        #pid variables rotational
	Pr = [0 for u in range(2)]
	Ir = [0 for u in range(2)]
	Dr = [0 for u in range(2)]
	k_py = 250
	k_iy = 1
	k_dy = 50
	er = [0 for u in range(2)]
	oldr = [0 for u in range(2)]

        #pid variables translational
	P =[0 for u in range(3)]
	I = [0 for u in range(3)]
	D = [0 for u in range(3)]
	k_p = [390, 300, 170] 
	k_i = [20, 20, 50]
	k_d = [690, 590, 500]
	e = [0 for u in range(3)]
	old = [0 for u in range(3)]

        while not rospy.is_shutdown():
            time.sleep(0.1)

            # Try to get data
            try:
                a = self.sub.get_data()['desiredposition']['data']
            except:
                a = [-1, 1, -1, -1.5708, 0.1]

            d = [a[0], a[1], a[2]]
            dr = [a[3], a[4]]

            try:
                # Get joystick data
                joy = self.sub.get_data()['joy']['axes']
                but = self.sub.get_data()['joy']['buttons']
                # Get ROV positions
                pos1 = self.sub.get_data()['odometry']['filtered']['pose']['pose']['position']
                q = self.sub.get_data()['odometry']['filtered']['pose']['pose']['orientation']
                pos = [pos1['x'], pos1['y'], pos1['z']]
                # Converting button presses to roll and pitch setting modification
                self.curr_pitch_setting = self.enforce_limit(self.curr_pitch_setting - joy[7] * 0.1)
                self.curr_roll_setting = self.enforce_limit(self.curr_roll_setting - joy[6] * 0.1)
                if (but[4] == 1):
                    self.curr_pitch_setting = 0.0
                if (but[5] == 1):
                    self.curr_roll_setting = 0.0

                sinr_cosp = +2.0 * (q['w'] * q['x'] + q['y'] * q['z'])
                cosr_cosp = +1.0 - 2.0 * (q['x'] * q['x'] + q['y'] * q['y'])
                sinp = +2.0 * (q['w'] * q['y'] - q['z'] * q['x'])
                siny_cosp = +2.0 * (q['w'] * q['z'] + q['x'] * q['y'])
                cosy_cosp = +1.0 - 2.0 * (q['y'] * q['y'] + q['z'] * q['z'])  
                yaw = m.atan2(siny_cosp, cosy_cosp)
                roll = m.atan2(sinr_cosp, cosr_cosp)
                posr = [yaw, roll]

                for i in range(2):
                    val1 = Angle(dr[i], posr[i])
                    Pr[i] = val1 * k_py
                    Ir[i] += val1 * k_iy * 0.11
                    Dr[i] = -(abs(Val(oldr[i], val1, dr[i])) / 0.11) * k_dy * (Pr[i] / abs(Pr[i]))
                    er[i] = Pr[i] + Dr[i] + Ir[i]
                    oldr[i] = val1

                for i in range(3):
                    P[i] = (d[i] - pos[i]) * k_p[i]
                    I[i] += (d[i] - pos[i]) * k_i[i] * 0.11
                    D[i] = ((-old[i] + d[i] - pos[i]) / 0.11) * k_d[i]
                    if I[i] > 150 or I[i] < -150:
                        I[i] = 150 * I[i] / abs(I[i])
                    e[i] = P[i] + I[i] + D[i]
                    old[i] = d[i] - pos[i]

                if (abs(e[2]) > 1000):
                    e[2] = 1000 * e[2] / abs(e[2])
                if (abs(er[0]) > 650):
                    er[0] = 650 * er[0] / abs(er[0])
                if (abs(e[0]) > 1000):
                    e[0] = 1000 * e[0] / abs(e[0])
                if (abs(e[1]) > 900):
                    e[1] = 900 * e[1] / abs(e[1])

                forces = [0.0, 0.0, 0.0]
                torques = [0.0, 0.0, 0.0]

                forces[0] = e[1] / (1300) * (1-er[0] / 950) #Surge
                forces[1] = (1-er[0] / 950) * e[0] / 1300 #Sway
                forces[2] = e[2] / 300 #Heave
                torques[0] = self.curr_roll_setting #Roll
                torques[1] = self.curr_pitch_setting #Pitch
                torques[2] = er[0] / 950 #Yaw

                data = Custom()
                data.id = "autonomous"
                data.data = forces + torques
                self.pub.set_data('/auto', data)

            except Exception as error:
                print('send data /auto error:', error)

            if (abs(m.sqrt((d[0] - pos[0]) ** 2 + (d[1] - pos[1]) ** 2 + (d[2] - pos[2]) ** 2)) < 0.2):
                data = Custom()
                data.id = "fetch"
                data.data = next
                self.pub.set_data('/next_pos', data)

if __name__ == "__main__":
    try:
        rospy.init_node('auto_node', log_level=rospy.DEBUG)
    except rospy.ROSInterruptException as error:
        print('pubs error with ROS: ', error)
        exit(1)
    code = Auto()
    code.run()

