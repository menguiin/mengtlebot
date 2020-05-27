#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from menguiin_bot.msg import Angle

print("Window 3")

rospy.init_node('input_angle', anonymous=True)
stop_pub = rospy.Publisher("isStop", Bool, queue_size=1)
angle_pub = rospy.Publisher("angle", Angle, queue_size=1)

twist = Twist()
angle = Angle()

angle1 = int(input("Put the angle1: "))
angle2 = int(input("Put the angle2: "))

angle.data1, angle.data2 = angle1, angle2

def scanCallback(scan):
    estop = Bool()
    for i in range(angle1, angle2):
        distance = scan.ranges[i]
        if distance < 0.3:
            print("Distance: ", distance)
            estop = False
            stop_pub.publish(estop)
        else:
            estop = True
            stop_pub.publish(estop)
    angle_pub.publish(angle)

def inputAngle():
    rospy.Subscriber("scan", LaserScan, scanCallback)

    rospy.spin()

if __name__ == '__main__':
    try:
        inputAngle()
    except rospy.ROSInterruptException:
        pass 