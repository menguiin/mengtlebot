#!/usr/bin/env python

import rospy
from menguiin_bot.msg import Angle

def talker():
    rospy.init_node('min_distance', anonymous=True)
    pub = rospy.Publisher("angle2", Angle, queue_size=1)
    ang = Angle()

    while not rospy.is_shutdown():
        angle1 = int(input("Put the angle1: "))
        angle2 = int(input("Put the angle2: "))
    
        ang.data1 = angle1
        ang.data2 = angle2
        pub.publish(ang)

if __name__ == '__main__':
    talker()