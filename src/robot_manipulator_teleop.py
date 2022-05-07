#!/usr/bin/env python3
import rospy
import keyboard
from std_msgs.msg import String
import os
import numpy as np

## Variables

global msg
global dire

msg = String()

dire=1


def getPos():
    print('ToDo_getPos')




def key_press(key):
    global msg
    global dire

    if key.event_type == "down":
        if key.name == "r":
            dire=-1*dire

        elif key.name == "1":
            msg.data = str(dire)+",a"
            #getPos()

        elif key.name == "2":
            msg.data = str(dire)+",b"
            #getPos()

        elif key.name == "3":
            msg.data = str(dire)+",c"
            #getPos()
        elif key.name == "4":
            msg.data = str(dire)+",d"
            #getPos()
        elif key.name == "k":
            msg.data = str(dire)+",k"
            #getPos()
        elif key.name == "i":
            msg.data = str(dire)+",i"
            #getPos()
        

    elif key.event_type == "up":
        if key.name == "1":
            msg.data="0,0"
        elif key.name == "2":
            msg.data="0,0"
        elif key.name == "3":
            msg.data="0,0"
        elif key.name == "4":
            msg.data="0,0"
        elif key.name == "k":
            msg.data="0,0"
        elif key.name == "i":
            msg.data="0,0"
        elif key.name == "r":
            dire=dire


def talker():




    #vel = int(input('Ingrese la velocidad deseada: '+"[0-"+str(int(velmax))+"](cm/s):"))
    


    rospy.init_node('robot_manipulator_teleop', anonymous=True)
    pub = rospy.Publisher('/robot_cmdVel', String, queue_size=10)
    rate = rospy.Rate(10) #10Hz

    keyboard.hook(key_press)

    while not rospy.is_shutdown():
        #print("\n" +str(msg.data))
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
