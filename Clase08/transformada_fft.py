# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 19:54:15 2021

@author: Sabri
"""

from scipy import signal #para procesar señales
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', 
                 index_col = ['Time'], 
                 parse_dates = True)

inicio = '2014-01'
fin = '2014-06'
alturas_sf = df[inicio:fin]['H_SF'].to_numpy()
alturas_ba = df[inicio:fin]['H_BA'].to_numpy()

def calcular_fft(y, freq_sampleo = 24.0):
    '''y debe ser un vector con números reales representando datos
    de una serie temporal.
    freq_sampleo está seteado para considerar 24 datos por unidad.
    Devuelve dos vectores, uno de frecuencias y otro con la transformada
    propiamente.
    La transformada contiene los valores complejos que le corresponden
    con respectivas frecuencias.'''
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1 / freq_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran


#Calculamos la transformada de las alturas de San Fernando
freq_sf, fft_sf = calcular_fft(alturas_sf) #la potencia o amplitud es abs(fft_sf)
                                           #para cada frecuencia
                                           
#print(signal.find_peaks(np.abs(fft_sf), prominence = 8))
#Hay un pico com la prominencia solicitada que tiene magnitud 11.45 y
#corresponde a la posición 350 del vector

plt.plot(freq_sf, np.abs(fft_sf))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.xlim(0, 4)    
plt.ylim(0, 20)
# me quedo solo con el último pico
pico_sf = signal.find_peaks(np.abs(fft_sf), prominence = 8)[0][-1]
# es el pico a analizar, el de las ondas de mareas
# marco ese pico
plt.scatter(freq_sf[pico_sf], np.abs(fft_sf)[pico_sf], facecolor = 'r')
plt.title("Espectro de Potencias San Fernando")
plt.show()


# Calcular la fase de la componente
ang_sf = np.angle(fft_sf)[pico_sf]

#Desfasaje ang_sf * 24 / (2 * np.pi * freq_sf[350])

# Espectro de potencia y de ángulos para Buenos Aires
freq_ba, fft_ba = calcular_fft(alturas_ba)

plt.figure()
plt.plot(freq_ba, np.abs(fft_ba))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.xlim(0, 4)
plt.ylim(0, 20)

# Calculo los picos y me quedo con el último
pico_ba = signal.find_peaks(np.abs(fft_ba), prominence = 8)[0][-1]
plt.scatter(freq_ba[pico_ba], np.abs(fft_ba)[pico_ba], facecolor = 'r')
plt.title("Espectro de Potencias Bs. As.")
plt.show()

# Fases
ang_ba = np.angle(fft_ba)[pico_ba]
freq = freq_ba[pico_ba]
ang2h = 24 / (2 * np.pi * freq)
print(ang_ba * ang2h)
#El retardo de la onda de mareas puede calcularse usando
# (ang_ba - ang_sf) * ang2h

