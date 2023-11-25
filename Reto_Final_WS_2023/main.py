#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.iodevices import Ev3devSensor 
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from tarea import Tareas 
from pybricks.nxtdevices import LightSensor
import time



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
MD = Motor(Port.C, Direction.COUNTERCLOCKWISE)
MI = Motor(Port.B, Direction.COUNTERCLOCKWISE)
MG = Motor(Port.A, Direction.COUNTERCLOCKWISE)
SD = LightSensor(Port.S4)
SI = ColorSensor(Port.S2)
SC = Ev3devSensor(Port.S3)
Sonidos =  SoundFile()




# Write your program here.
movimientos = Tareas(ev3, MD, MI, MG, SD, SI , SC, wait,  Stop, Sonidos, Color, DriveBase, time)
ev3.speaker.beep()
movimientos.mover_por_distancia(40,"adelante")
movimientos.girar_n_grados(90,"izquierda")
