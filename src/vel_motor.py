#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

print("Window 2")
twist = Twist()

BURGER_MAX_LIN_VEL = 0.22
BURGER_MAX_ANG_VEL = 2.84

vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
lin_vel = float(input("Input Linear velocity(-0.22 ~ 0.22): "))
ang_vel = float(input("Input angular velocity(-2.84 ~ 2.84): "))

def constrain(put, low, high):
    if put < low:
      put = low
    elif put > high:
      put = high
    else:
      put = put

    return put

def checkLinearLimitVelocity(vel):
    vel = constrain(vel, -BURGER_MAX_LIN_VEL, BURGER_MAX_LIN_VEL)

    return vel

def checkAngularLimitVelocity(vel):
    vel = constrain(vel, -BURGER_MAX_ANG_VEL, BURGER_MAX_ANG_VEL)

    return vel

def stopCallback(estop):
    rate = rospy.Rate(10)
    if estop.data is False:
        twist.linear.x = 0
        twist.angular.z = 0
    else:
        target_lin_vel = checkLinearLimitVelocity(lin_vel)
        target_ang_vel = checkAngularLimitVelocity(ang_vel)

        twist.linear.x = target_lin_vel
        twist.angular.z = target_ang_vel
    vel_pub.publish(twist)
    rate.sleep()

def inputVel():
    rospy.init_node('vel_motor', anonymous=True)
    rospy.Subscriber('isStop', Bool, stopCallback)

    rospy.spin()
        
if __name__ == '__main__':
    try:
        inputVel()
    except rospy.ROSInterruptException:
        pass 
