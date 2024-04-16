import serial
import serial.tools.list_ports
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import matplotlib.dates as mdates

puerto = input("Puerto serial (ej COM3):")
Tmuestreo = float(input("Período muestreo [ms] (min 100ms):"))
Tmuestreo=Tmuestreo/1000

ser = serial.Serial(puerto, 9600, timeout=1)  # crear puerto serial
ser.flushInput()

while 1:

    # Leer datos del puerto serial. Si hay error, devolver -1.
    try:
        linea = str(ser.readline().decode('ascii'))
        # Leer tiempo
        now = datetime.datetime.now()
        vtemp = float(linea[0:4])
        vpower = float(linea[5:9])
    except:
        # Leer tiempo
        now = datetime.datetime.now()
        vtemp = -1
        vpower = -1

    t = now.timestamp()

    dia = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
    dia_archivo = dia + ".txt"

    # Escribir datos leídos a txt
    f = open(dia, "+a")
    s = str(t) + "," + str(vtemp) + "," + str(vpower) + '\n'
    f.write(s)
    f.close()

    # Imprimir en consola
    # Plast = getPower(vpower, 5000) #convertir voltaje a potencia RF
    print(str(now)+", "+"Potencia: "+str(vpower)+" V")
    ser.flushInput()
    time.sleep(Tmuestreo)

