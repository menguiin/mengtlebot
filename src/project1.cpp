#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include "geometry_msgs/Twist.h"

geometry_msgs::Twist vel;
ros::Publisher *publishPtr;

void scanCallback(const sensor_msgs::LaserScan::ConstPtr &msg)
{
    ros::Publisher laser_pub = (ros::Publisher)*publishPtr;

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
    laser_pub.publish(vel);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "project1");
    ros::NodeHandle nh;
    ros::Publisher laser_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 1);
    ros::Subscriber laser_sub = nh.subscribe("/scan", 1, scanCallback);
    publishPtr = &laser_pub;

    ros::spin();

    return 0;
}