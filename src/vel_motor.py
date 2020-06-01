#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from menguiin_bot.msg import Distance

print("Window 2")
twist = Twist()

BURGER_MAX_LIN_VEL = 0.22
BURGER_MAX_ANG_VEL = 2.84

vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
is_scan = 0
lin_vel= ang_vel = 0
# lin_vel = float(input("Input Linear velocity(-0.22 ~ 0.22): "))
# ang_vel = float(input("Input angular velocity(-2.84 ~ 2.84): "))

def stopCallback(mini):
    rate1 = rospy.Rate(10)
    global is_scan
    is_scan = 1
    if mini.data < 0.3 and mini.data > 0:
        twist.linear.x = 0
        twist.angular.z = 0
    else:
        twist.linear.x = lin_vel
        twist.angular.z = ang_vel
    rate1.sleep()
    vel_pub.publish(twist)

def inputVel():
    rospy.init_node('vel_motor', anonymous=True)
    rospy.Subscriber('distance', Distance, stopCallback)
    rate = rospy.Rate(10)
    global lin_vel, ang_vel
    while is_scan == 0:
        twist.linear.x = lin_vel
        twist.angular.z = ang_vel

        vel_pub.publish(twist)
        lin_vel = float(input("Input Linear velocity(-0.22 ~ 0.22): "))
        ang_vel = float(input("Input angular velocity(-2.84 ~ 2.84): "))
        rate.sleep()
    rospy.spin()
        
if __name__ == '__main__':
    try:
        inputVel()
    except rospy.ROSInterruptException:
        pass 
