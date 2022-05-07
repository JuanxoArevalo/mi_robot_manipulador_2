#!/usr/bin/env python3
from posixpath import split
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
#import RPi.GPIO as GPIO
from gpiozero import Servo
import numpy as np



def set_pose2(x,y,th):
    
    c=((x**2)+(y**2)-128)/(2*8*8)
    q2=-np.arcos(c)
    
    d=(8*np.sin(q2)*q2)/(8+8*np.cos(q2)*q2)
    q1=np.arctan(y/x)+np.arctan(d)

    anguloB=q2+60
    anguloC=q1+180

    servoB.value=convertirAngulo(anguloB)
    servoC.value=convertirAngulo(anguloC)
    servoA.value=convertirAngulo(th)






def convertirAngulo(angulo):

    return (-1+(angulo*(1/90)))

# Mueve el motor a un angulo





while True:

    print("Objetivo")
    goal=input("x,y,theta").split(',')
    x=float(goal[0])
    th=int(goal[1])
    z=float(goal[2])

    set_pose2(x,z,th)