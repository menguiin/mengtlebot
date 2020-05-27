#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from menguiin_bot.msg import Angle

print("Window 4")

angle1, angle2 = 0, 0
angle_bool = False
range_data = [0]

def scan_callbak(scan):
    global range_data
    if angle_bool == True:
        range_data = []
        for i in range(angle1, angle2):
            range_data.append(scan.ranges[i])
    else:
        pass
    
def time_callback(event):
    rospy.loginfo("MINIMUM: %f" % min(range_data))

def angle_callback(angle):
    global angle1
    global angle2 
    angle1, angle2 = angle.data1, angle.data2
    global angle_bool 
    angle_bool = True

def listener():
    rospy.init_node('min_distance', anonymous=True)
    rospy.Subscriber('scan', LaserScan, scan_callbak)
    rospy.Subscriber('angle', Angle, angle_callback)
    rospy.Timer(rospy.Duration(1), time_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()