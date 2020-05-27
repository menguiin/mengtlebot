#include <ros/ros.h>
#include <sensor_msgs/LaserScan.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/Bool.h>
#include "menguiin_bot/Angle.h"

// 전역 변수 선언
static geometry_msgs::Twist vel;

void scanCallback(const sensor_msgs::LaserScan::ConstPtr &msg)
{
    ROS_INFO("recieve msg[180] = %f", msg->ranges[180]);

    //start
    vel.linear.x = 1;
    vel.linear.y = 0;
    vel.angular.z = 0;

    // in 0.4m, stop
    if(msg->ranges[180] < 0.4 && msg->ranges[180] > 0.2)
    {
        vel.linear.x = 0;
        vel.linear.y = 0;
        vel.angular.z = 0;
    }

    // in 0.2m, go back
    if(msg->ranges[180] < 0.2 && msg->ranges[180] > 0)
    {
        vel.linear.x = -0.5;
        vel.linear.y = 0;
        vel.angular.z = 0;
    }

    // left obstacle, turn right
    if(msg->ranges[90] < 0.3 && msg->ranges[90] > 0)
    {
        vel.linear.x = 0;
        vel.linear.y = 0;
        vel.angular.z = 1;
        ROS_INFO("recieve msg[90] = %f", msg->ranges[90]);
    }

    // right obstacle, turn left
    if(msg->ranges[270] < 0.3 && msg->ranges[270] > 0)
    {
        vel.linear.x = 0;
        vel.linear.y = 0;
        vel.angular.z = 1;
        ROS_INFO("recieve msg[270] = %f", msg->ranges[270]);
    }
}

int main(int argc, char **argv)
{
    using namespace ros;
    init(argc, argv, "project1");
    NodeHandle nh;
    Publisher laser_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 1);
    Subscriber laser_sub = nh.subscribe("/scan", 1, scanCallback);
    Publisher motor_pub = nh.advertise<std_msgs::Bool>("/motor_power", 1);
    Rate loop_rate(10); // 주기는 10HZ로..

    // 모터 켜기
    std_msgs::Bool power;
    power.data = true;
    motor_pub.publish(power);
    
    while(ok())
    {
        laser_pub.publish(vel);
        spinOnce();
        loop_rate.sleep();
    }

    return 0;
}