#!/usr/bin/env python3
from posixpath import split
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import RPi.GPIO as GPIO
from gpiozero import Servo

# Angulos iniciales de cada motor

InicialA=0
InicialB=0
InicialC=0
InicialD=0

# Definicion de los servos 

servoA = Servo(25)
servoB = Servo(24)
servoC = Servo(23)
servoD = Servo(22)

# Angulo de cada paso 

dif=2

# Angulo actual

ActualA=InicialA
ActualB=InicialB
ActualC=InicialC
ActualD=InicialD

# lee la informacion de teleop
def callback_read(data):
    
    dato = data.data
    datos=dato.split(',')
    
    #Direcion de giro
    
    dir=int(datos[1])*dif
    
    # Motor
    
    motor=datos[0]
    moveMotor(motor,dir)

# Convierte el angulo a un valor valido entre -1 y 1

def convertirAngulo(angulo):
     
    return (-1+(angulo*(1/90)))

# Mueve el motor a un angulo 

def moveMotor(motor,dir):

    if motor== 'a':
        
        angulo=ActualA+dir*(dif)
        ActualA=angulo
        
        if angulo < 0:
            angulo =0
        if angulo > 180:
            angulo =180

        servoA.value=convertirAngulo(angulo)
    if motor== 'b':
        
        angulo=ActualB+dir*(dif)
        ActualB=angulo

        if angulo < 0:
            angulo =0
        if angulo > 180:
            angulo =180

        servoB.value=convertirAngulo(angulo)
    if motor== 'c':
        
        angulo=ActualC+dir*(dif)
        ActualC=angulo

        if angulo < 0:
            angulo =0
        if angulo > 180:
            angulo =180

        servoC.value=convertirAngulo(angulo)
    if motor== 'd':

        angulo=ActualD+dir*(dif)
        ActualD=angulo

        if angulo < 0:
            angulo =0
        if angulo > 180:
            angulo =180

        servoD.value=convertirAngulo(angulo)
   


def listener():

    rospy.init_node('robot_listener', anonymous=True)
    rospy.Subscriber('/robot_cmdVel', String, callback_read)
    rospy.spin()


if __name__ == '__main__':
    listener()