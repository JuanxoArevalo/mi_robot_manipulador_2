#!/usr/bin/env python3
import rospy
import keyboard
from std_msgs.msg import String
import os
import numpy as np

## Variables

global msg
global dire
global velA
global velB
global velC

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
            msg.data = str(dire)+",a"+','+str(velA)+','+str(velB)+','+str(velC)
            #getPos()

        elif key.name == "2":
            msg.data = str(dire)+",b"+','+str(velA)+','+str(velB)+','+str(velC)
            #getPos()

        elif key.name == "3":
            msg.data = str(dire)+",c"+','+str(velA)+','+str(velB)+','+str(velC)
            #getPos()
        elif key.name == "4":
            msg.data = str(dire)+",d"+','+str(velA)+','+str(velB)+','+str(velC)
            #getPos()
        elif key.name == "k":
            msg.data = str(dire)+",k"+','+str(velA)+','+str(velB)+','+str(velC)
            #getPos()
        elif key.name == "i":
            msg.data = str(dire)+",i"+','+str(velA)+','+str(velB)+','+str(velC)
        elif key.name == "j":
            msg.data = str(dire)+",j"+','+str(velA)+','+str(velB)+','+str(velC)
            #getPos()
        elif key.name == "l":
            msg.data = str(dire)+",l"+','+str(velA)+','+str(velB)+','+str(velC)
            #getPos()
        

    elif key.event_type == "up":
        if key.name == "1":
            msg.data="0,0,0,0,0"
        elif key.name == "2":
            msg.data="0,0,0,0,0"
        elif key.name == "3":
            msg.data="0,0,0,0,0"
        elif key.name == "4":
            msg.data="0,0,0,0,0"
        elif key.name == "k":
            msg.data="0,0,0,0,0"
        elif key.name == "i":
            msg.data="0,0,0,0,0"
        elif key.name == "j":
            msg.data="0,0,0,0,0"
        elif key.name == "l":
            msg.data="0,0,0,0,0"
        elif key.name == "r":
            dire=dire


def talker():




    #vel = int(input('Ingrese la velocidad deseada: '+"[0-"+str(int(velmax))+"](cm/s):"))
    
    velA=int(input("Velocidad motor A: "))
    velB=int(input("Velocidad motor B: "))
    velC=int(input("Velocidad motor C: "))
    
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
