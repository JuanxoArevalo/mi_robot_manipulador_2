#!/usr/bin/env python3
from posixpath import split
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import RPi.GPIO as GPIO
from gpiozero import Servo


# Definicion de los servos

servoA = Servo(25)
servoB = Servo(8)
servoC = Servo(7)
servoD = Servo(1)



def convertirAngulo(angulo):

    return (-1+(angulo*(1/90)))

# Mueve el motor a un angulo

def moveMotor(motor,angulo):

    if motor== 'a':

 
        servoA.value=convertirAngulo(angulo)
    if motor== 'b':



        servoB.value=convertirAngulo(angulo)
    if motor== 'c':


        servoC.value=convertirAngulo(angulo)


    if motor== 'd':



        servoD.value=convertirAngulo(angulo)


while True:
    datos=input("Angulo,motor")
    d=datos.split(',')
    motor=d[1]
    angulo=int(d[0])
    moveMotor(motor,angulo)