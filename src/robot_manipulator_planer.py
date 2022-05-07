#!/usr/bin/env python3
from posixpath import split
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
#import RPi.GPIO as GPIO
from gpiozero import Servo

# Angulos iniciales de cada motor
global difA
global difB
global difC
global difD

global ActualA
global ActualB
global ActualC
global ActualD

InicialA=0
InicialB=40
InicialC=110
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


difA=1
difB=1
difC=1
difD=10

# Angulo actual

ActualA=InicialA
ActualB=InicialB
ActualC=InicialC
ActualD=InicialD

global maxX
global minX
global maxY
global minY 

maxX=150
minX=40

maxY=150
minY=40

def set_pose(r,th,z):

    metaR=minX+int((maxX-minX)*r)
    metaTH=th
    metaZ=minY+int((maxY-minY)*z)

    servoA.value=convertirAngulo(metaTH)

    while(ActualB!=metaR):
        adelante()

    servoB.value=convertirAngulo(ActualB)
    servoC.value=convertirAngulo(ActualC)
    
    ActualB=InicialB
    ActualC=InicialC

    while(ActualB!=metaZ):
        arriba()

    servoB.value=convertirAngulo(ActualB)
    servoC.value=convertirAngulo(ActualC)







# Convierte el angulo a un valor valido entre -1 y 1

def arriba():
    moveMotor("b",1)
    moveMotor("c",-1)

def abajo():
    moveMotor("b",-1)
    moveMotor("c",1)

def adelante():
    moveMotor("b",1)
    moveMotor("c",1)

def atras():
    moveMotor("b",-1)
    moveMotor("c",-1)



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
        angulo=ActualA+dire*(difA)
        
        


        if angulo < 0:
            angulo =0
        if angulo > 180:
            angulo =180
        ActualA=angulo
        print("angulo A:")
        print(ActualA)
        #print(convertirAngulo(angulo))

        #servoA.value=convertirAngulo(angulo)

    if motor== 'b':

        angulo=ActualB+dire*(difB)


        if angulo < 40:
            angulo =40
        if angulo > 150:
            angulo =150
        ActualB=angulo
        print("angulo B:")
        print(ActualB)

        #servoB.value=convertirAngulo(angulo)
    if motor== 'c':

        angulo=ActualC+dire*(difC)


        if angulo < 110:
            angulo =110
        if angulo > 180:
            angulo =180
        ActualC=angulo
        print("angulo C:")
        print(ActualC)
        #servoC.value=convertirAngulo(angulo)


    if motor== 'd':

        angulo=ActualD+dire*(difD)


        if angulo < 90:
            angulo =90
        if angulo > 90:
            angulo =180
        ActualD=angulo
        print("angulo D:")
        print(ActualD)
        #servoD.value=convertirAngulo(angulo)
    if motor=='i':
        arriba()
    if motor=='k':
        abajo()
    if motor=='j':
        adelante()
    if motor=='l':
        atras()

def inicio():
    servoA.value=convertirAngulo(ActualA)
    servoB.value=convertirAngulo(ActualB)
    servoC.value=convertirAngulo(ActualC)
    servoD.value=convertirAngulo(ActualD)




while True:

    print("Objetivo")
    goal=input("r,thetha,z").split(',')
    r=float(goal[0])
    th=int(goal[1])
    z=float(goal[2])

    set_pose(r,th,z)