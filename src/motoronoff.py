#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
from sensor_msgs.msg import Imu
from tf.transformations import quaternion_from_euler, euler_from_quaternion
import numpy as np

print("Window 1")
roll = pitch = yaw = 0.0
onoff = Bool()
is_on = False

def imu_callback(msg):
    global roll, pitch, yaw
    orientation_q = msg.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = np.rad2deg(euler_from_quaternion(orientation_list))

    if abs(roll) > 45 or abs(pitch) > 45 or abs(yaw) > 45:
        onoff.data = 0
    else:
        onoff.data = is_on
    motor_pub.publish(onoff)

def motor():
    global motor_pub
    global is_on
    motor_pub = rospy.Publisher('motor_power', Bool, queue_size=1)
    rospy.init_node('motoronoff', anonymous=True)
    rospy.Subscriber('imu', Imu, imu_callback)

    is_on = input("On(1)/Off(0): ")
    if is_on == 1 or is_on == 0:
        is_on = bool(is_on)
    else:
        print("plz input 1 or 0...")
        is_on = False
        pass
    
    onoff.data = is_on
    rospy.spin()

if __name__ == '__main__':
    try:
        motor()
    except rospy.ROSInterruptException:
        pass