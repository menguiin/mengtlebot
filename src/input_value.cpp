#include "ros/ros.h"
#include "menguiin_bot/Angle.h"
#include "menguiin_bot/Velocity.h"

int main(int argc, char **argv)
{
    using namespace ros;
    init(argc, argv, "input_value");
    NodeHandle nh;
    Publisher pub = nh.advertise<menguiin_bot::Angle>("/angle", 1);
    menguiin_bot::Angle ang;
    Rate loop_rate(10); // 주기는 10HZ로..

    
    while(ok())
    {
        ang.data1 = scanf("angle1: ");
        ang.data2 = scanf("angle2: ");
        pub.publish(ang);
        loop_rate.sleep();
    }

    return 0;
}