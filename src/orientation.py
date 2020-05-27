#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from tf.transformations import quaternion_from_euler, euler_from_quaternion
import numpy as np

print("Window5")
roll = pitch = yaw = 0.0

def imu_callback(msg):
    global roll, pitch, yaw
    orientation_q = msg.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = np.rad2deg(euler_from_quaternion(orientation_list))
    print(roll)

def time_callback(event):
    rospy.loginfo("X: %f\n" % roll)
    rospy.loginfo("Y: %f\n" % pitch)
    rospy.loginfo("Z: %f\n" % yaw)


def listener():
    rospy.init_node("orientation", anonymous=True)
    rospy.Subscriber("imu", Imu, imu_callback)
    rospy.Timer(rospy.Duration.from_sec(0.1), time_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass