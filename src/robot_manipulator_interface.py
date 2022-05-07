#!/usr/bin/env python3
from posixpath import split
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import math
import matplotlib.patches as patches
import tkinter as Tk
import tkinter.font as TkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

global difA
global difB
global difC
global difD

global ActualA
global ActualB
global ActualC
global ActualD

InicialA=120
InicialB=40
InicialC=130
InicialD=0

ActualA=InicialA
ActualB=InicialB
ActualC=InicialC
ActualD=InicialD

trackX = []
trackY = []
trackZ = []

global largoBr
largoBr = 80
def radioDeAng(angleB, angleC):
    angleB=40
    angleC=130
    largoBr=80
    global distx1
    distx1 = 0
    global distx2
    distx2 = 0
    global distxT
    distxT = 0


    #angulo B
    angleBcorr = angleB-15

    angleCcorr = abs(angleC-180)

    distx1 = largoBr*math.cos(math.radians(angleCcorr))

    distx2 = largoBr*math.sin(math.radians(angleBcorr/2))

    distxT = distx1 + distx2

    return distxT

def alturaDeAng(angleB, angleC):
    global disty1
    disty1 = 0
    global disty2
    disty2 = 0
    global distyT
    distyT = 0


    #angulo B
    angleBcorr = angleB-15
    angleCcorr = abs(angleC-180)
    disty1 = largoBr*(math.radians(angleCcorr))
    disty2 = largoBr*(math.radians(angleBcorr/2))
    distyT = disty1 - disty2
    return distyT
def callback_read(data):
    #print("call")


    dato = data.data
    datos=dato.split(',')
    #if datos[0]!="0":
    #    print(datos)
    #Direcion de giro

    dire=int(datos[0])
    difA=int(datos[2])
    difB=int(datos[3])
    difC=int(datos[4])

    motor=datos[1]

    angulosActuales(motor,dire,difA,difB,difC)


def angulosActuales(motor,dire,difA,difB,difC):
    global ActualA
    global ActualB
    global ActualC
    global pos
    if motor== 'a':
        angulo=ActualA+dire*(difA)




        if angulo < 0:
            angulo =0
        if angulo > 180:
            angulo =180
        ActualA=angulo
    if motor== 'b':

        angulo=ActualB+dire*(difB)


        if angulo < 40:
            angulo =40
        if angulo > 150:
            angulo =150
        ActualB=angulo
    if motor== 'c':

        angulo=ActualC+dire*(difC)


        if angulo < 110:
            angulo =110
        if angulo > 180:
            angulo =180
        ActualC=angulo
    print(ActualB)
    print(ActualC)
    global radio
    global z
    radio = radioDeAng(int(ActualB), int(ActualC))
    z = alturaDeAng(int(ActualB), int(ActualC))

    pos = [ActualA, radio, z]
    print(pos)
    #print(pos)
    posCart = cil2cart(radio, ActualA, z)
    print(posCart)
    posx=posCart[0]
    posy=posCart[1]
    posz=posCart[2]

    trackX.append(posx)
    trackY.append(posy)
    pos_array = [posx, posy]


def cil2cart(r, angle, z):
    x = r*math.cos(math.radians(angle))
    y = r*math.sin(math.radians(angle))
    z = z

    coord = [x,y,z]
    return coord
#Funciones para graficar
def animate(i, trackX, trackY):
    # Draw x and y lists
    ax.clear()
    if trackX:
        ax.scatter(trackX[-1], trackY[-1], color='r', marker='*')
    ax.scatter(trackX, trackY, color='b')

def save_plot():
    title = title_input.get()
    fig.suptitle(title)
    plt.savefig(title + '.png')
    fig.suptitle('')





if __name__ == '__main__':
    rospy.init_node('robot_manipulator_interface', anonymous=True)
    rospy.Subscriber('/robot_cmdVel', String, callback_read)
    rospy.Rate(60)

    fig = plt.figure(figsize=(4,4))
    root = Tk.Tk()
    root.geometry("800x900")
    root.configure(background='white')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=0, rely=0.05)

    ax = fig.add_subplot(1, 1, 1)
    # Format plot
    fontFamily = TkFont.Font(family="Arial", size=14, weight="bold", slant="italic")

    label = Tk.Label(master=root, text="Ingrese el titulo para guardar \n la grafica", foreground='black', background='white', font=fontFamily)
    label.place(x=75, y=25)


    title_input = Tk.Entry(master=root,
                            width=50,
                            font=fontFamily)
    title_input.place(x=75,rely=0.1)
    save_btn = Tk.Button(master = root,
                        height=2,
                        width=80,
                        command=save_plot,
                        text='Save')
    save_btn.place(relx=0.1, rely=0.95)

    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(trackX, trackY), interval=0)


    Tk.mainloop()
