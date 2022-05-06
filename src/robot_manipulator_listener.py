#!/usr/bin/env python3
from posixpath import split
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
#import RPi.GPIO as GPIO
from gpiozero import Servo

# Angulos iniciales de cada motor
global dif
global ActualA
global ActualB
global ActualC
global ActualD

InicialA=0
InicialB=0
InicialC=0
InicialD=0

# Definicion de los servos

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

# Angulo de cada paso

dif=10

# Angulo actual

ActualA=InicialA
ActualB=InicialB
ActualC=InicialC
ActualD=InicialD

# lee la informacion de teleop
print('hola')
def callback_read(data):
    #print("call")
    global dif
    dato = data.data
    datos=dato.split(',')
    #if datos[0]!="0":
    #    print(datos)
    #Direcion de giro

    dire=int(datos[0])

    # Motor

    motor=datos[1]
    moveMotor(motor,dire)

# Convierte el angulo a un valor valido entre -1 y 1

def convertirAngulo(angulo):

    return (-1+(angulo*(1/90)))

# Mueve el motor a un angulo

def moveMotor(motor,dire):
    global ActualA
    global ActualB
    global ActualC
    global ActualD
    global maxPW
    global minPW
    if motor== 'a':
        angulo=ActualA+dire*(dif)

        


        if angulo < 0:
            angulo =0
        if angulo > 180:
            angulo =180
        ActualA=angulo
        print("angulo A:")
        print(ActualA)
        #print(convertirAngulo(angulo))

        servoA.value=convertirAngulo(angulo)

    if motor== 'b':

        angulo=ActualB+dire*(dif)


        if angulo < 40:
            angulo =40
        if angulo > 150:
            angulo =150
        ActualB=angulo
        print("angulo B:")
        print(ActualB)

        servoB.value=convertirAngulo(angulo)
    if motor== 'c':

        angulo=ActualC+dire*(dif)


        if angulo < 110:
            angulo =110
        if angulo > 180:
            angulo =180
        ActualC=angulo
        print("angulo C:")
        print(ActualC)
        servoC.value=convertirAngulo(angulo)


    if motor== 'd':

        angulo=ActualD+dire*(dif)


        if angulo < 90:
            angulo =90
        if angulo > 90:
            angulo =180
        ActualD=angulo
        print("angulo D:")
        print(ActualD)
        servoD.value=convertirAngulo(angulo)


def listener():
    print("buenas")
    rospy.init_node('robot_listener', anonymous=True)
    rospy.Subscriber('/robot_cmdVel', String, callback_read)
    rospy.spin()


if __name__ == '__main__':
    listener()
