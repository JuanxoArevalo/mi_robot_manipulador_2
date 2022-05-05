#!/usr/bin/env python3
import rospy
import keyboard
from std_msgs.msg import String
import os
import numpy as np

## Variables
global msg
global vel
global dir
global velmax

msg = String()




def getPos():
    print('ToDo_getPos')




def key_press(key):
    global msg
    global velLin
    global velAng
    global name
    global x
    global y
    global theta
    global position

    if key.event_type == "down":
        if key.name == "r":
            dir=-1*dir

        elif key.name == "1":
            msg.data = str(dir)+",a"
            getPos()

        elif key.name == "2":
            msg.data = str(dir)+",b"
            getPos()

        elif key.name == "3":
            msg.data = str(dir)+",c"
            getPos()
        elif key.name == "4":
            msg.data = str(dir)+",d"
            getPos()


    elif key.event_type == "up":
        if key.name == "1":
            msg.data=0
        elif key.name == "2":
            msg.data=0
        elif key.name == "3":
            msg.data=0
        elif key.name == "4":
            msg.data=0
        elif key.name == "r":
            dir=dir


def talker():
    global vel
    global velmax
    velmax=0
    global msg


    vel = int(input('Ingrese la velocidad deseada: '+"[0-"+str(int(velmax))+"](cm/s):"))



    rospy.init_node('robot_manipulator_teleop', anonymous=True)
    pub = rospy.Publisher('/robot_cmdVel', String, queue_size=10)
    rate = rospy.Rate(10) #10Hz

    keyboard.hook(key_press)

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
