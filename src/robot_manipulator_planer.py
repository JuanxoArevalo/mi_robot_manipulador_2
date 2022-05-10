#!/usr/bin/env python3
from posixpath import split
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
#import RPi.GPIO as GPIO
from gpiozero import Servo
import numpy as np
import math
math.degrees(math.pi/2)



myGPIO1=25
myGPIO2=8
myGPIO3=1
myGPIO4=7

global maxPW
global minPW

myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

servoA = Servo(myGPIO1,min_pulse_width=minPW,max_pulse_width=maxPW)
#servoA.value=None
servoB = Servo(myGPIO2,min_pulse_width=minPW,max_pulse_width=maxPW)
servoC = Servo(myGPIO3,min_pulse_width=minPW,max_pulse_width=maxPW)
servoD = Servo(myGPIO4,min_pulse_width=minPW,max_pulse_width=maxPW)


def set_pose2(x,y,th):
    
    print('ver')
    c=((x**2)+(y**2)-128)/(128)

#print(c)
    q2=-1*np.arccos(c)
    
    d=(8*np.sin(q2))/(8+8*np.cos(q2)*q2)
    q1=np.arctan(y/x)+np.arctan(d)

#print(q1)
#print(q2)
    anguloC=180-(math.degrees(q1)+90)
    anguloB=(anguloC+(math.degrees(q2)))-112

    print(anguloB)
    print(anguloC)

    servoB.value=convertirAnguloB(-anguloB)
    servoC.value=convertirAnguloC(anguloC)
    servoA.value=convertirAngulo(th)



def convertirAngulo(angulo):

    return (-1+(angulo*(1/90)))


def convertirAnguloB(angulo):

    if angulo < 20:
        angulo =40
    if angulo > 150:
        angulo =150    
    return (-1+(angulo*(1/90)))
def convertirAnguloC(angulo):

    if angulo < 110:
        angulo =110
    if angulo > 180:
        angulo =180    
    return (-1+(angulo*(1/90)))
# Mueve el motor a un angulo





while True:

    print("Objetivo")
    goal=input("x,y,theta").split(',')
    x=float(goal[0])
    th=int(goal[2])
    y=float(goal[1])

    set_pose2(x,y,th)