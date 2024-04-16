import serial
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import matplotlib.dates as mdates

tiempoV = input("Tiempo visualizacion [s]:")
Tmuestreo = input("Período de muestreo [ms]:")

# MAX NO. OF POINTS TO STORE: 30 min data
quex = deque(maxlen = int(np.round(int(tiempoV)*1000/int(Tmuestreo))))
quey = deque(maxlen = int(np.round(int(tiempoV)*1000/int(Tmuestreo))))

def getPower(vpower, freq):
    if freq == 1000:
        Pmin = -55
        Pmax = 0
    elif freq == 5000:
        Pmin = -60
        Pmax = -5
    elif freq == 6000:
        Pmin = -55
        Pmax = 5
    elif freq == 8000:
        Pmin = -50
        Pmax = 5
    k = (Pmax - Pmin) / (0.5 - 2.1)
    P = (k) * vpower + (Pmin - k * 2.1)
    return P

while 1:
    now = datetime.datetime.now()
    t = now.timestamp()

    dia = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
    dia_archivo = dia + ".txt"

    # Graficar últimos 30 min
    f = open(dia, "r")
    lineas = f.readlines()
    f.close()
    x = list(None for _ in range(len(lineas)))
    y = list(None for _ in range(len(lineas)))

    for indice in range(len(lineas)):
        esta = lineas[indice].split(",")
        x[indice] = float(esta[0])
        dt=(x[indice]-t)/60
        y[indice] = float(esta[2])
        # P = getPower(y[indice], 5000)	
        quey.append(y[indice])
        quex.append(dt)
    # PLOTTING THE POINTS
    plt.stem(quex,quey,bottom=0.3)
    plt.ylabel("Vout [V]")
    plt.xlabel("Min. antes de "+str(now.hour)+":"+str(now.minute))
    plt.xlim([-int(tiempoV)/60, 0])
    plt.ylim([0, 2.1])	
    plt.title(dia)
    # DRAW, PAUSE AND CLEAR
    plt.draw()
    plt.pause(0.1)
    plt.clf()
    #
    time.sleep(1)

