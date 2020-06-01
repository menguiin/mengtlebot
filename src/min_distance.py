#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from menguiin_bot.msg import Angle
from menguiin_bot.msg import Distance

print("Window 4")

angle1, angle2 = 0, 0
angle_bool = False
minimum = 0

def distance_callbak(scan):
    global minimum
    minimum = scan.data
    
def time_callback(event):
    rospy.loginfo("MINIMUM: %f" % minimum)

def angle_callback(angle):
    if angle_bool is True:
        pass
    global angle1
    global angle2 
    angle1, angle2 = angle.data1, angle.data2

def angle2_callback(angle):
    angle1, angle2 = angle.data1, angle.data2
    global angle_bool 
    angle_bool = True

def listener():
    rospy.init_node('min_distance', anonymous=True)
    rospy.Subscriber('distance', Distance, distance_callbak)
    rospy.Subscriber('angle', Angle, angle_callback)
    rospy.Subscriber('angle2', Angle, angle2_callback)
    rospy.Timer(rospy.Duration(1), time_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()