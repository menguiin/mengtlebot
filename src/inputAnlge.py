#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from menguiin_bot.msg import Angle
from menguiin_bot.msg import Distance

print("Window 3")

rospy.init_node('input_angle', anonymous=True)
stop_pub = rospy.Publisher("distance", Distance, queue_size=1)
angle_pub = rospy.Publisher("angle", Angle, queue_size=1)

twist = Twist()
angle = Angle()
minimum = Distance()
minimum = 0
angle1, angle2 = 0.0, 0.0
angle1 = int(input("Put the angle1: "))
angle2 = int(input("Put the angle2: "))

def scanCallback(scan):
    global minimum, angle1, angle2
    distance = []
    for i in range(angle1, angle2):
        if scan.ranges[i] > 0:
            distance.append(scan.ranges[i])
        if not distance:
            pass
        else:
            minimum = min(distance)
    print("Distance: %f" % minimum)
    stop_pub.publish(minimum)
    angle_pub.publish(angle)


def angleCallback(ang):
    global angle1, angle2
    angle1 = ang.data1
    angle2 = ang.data2
    print(angle1, angle2)

def inputAngle():
    rospy.Subscriber("scan", LaserScan, scanCallback)
    rospy.Subscriber("angle2", Angle, angleCallback)
    global angle1, angle2
    rospy.spin()

if __name__ == '__main__':
    try:
        inputAngle()
    except rospy.ROSInterruptException:
        pass 