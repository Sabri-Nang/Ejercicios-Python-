# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:43:38 2021

@author: Sabri
"""

import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import os

dir1 = '..'
dir2 = 'Data'
archivo = 'OBS_SHN_SF-BA.csv'
fname = os.path.join(dir1, dir2, archivo)

#Levanto las dos series
df = pd.read_csv(fname, index_col = ['Time'], parse_dates = True)


#Me quedo con un fragmento
dh = df['10-01-2014':].copy()

#Selecciono los intervalos que voy a usar para desplazar SF
shifts = np.arange(-12, 13)
#Genero un vector donde guardar los coeficientes de correlación para cada desplazamiento
corrs = np.zeros(shifts.shape)
for i, sh in enumerate(shifts):
    #guardo el coeficiente de correlación r entre SF desplazada con BA original
    corrs[i] = pearsonr(dh['H_SF'].shift(sh)[12:-12], dh['H_BA'][12:-12])[0]
#ploteo los resultados
plt.plot(shifts, corrs)

#%% Ejercicio 8.11

#Interpolación
#Este ejemplo muestra una manera de interplolar la serie de manera de poder 
#usar desplazamientos menores a una hora

#cada cuarto de hora
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import os

dir1 = '..'
dir2 = 'Data'
archivo = 'OBS_SHN_SF-BA.csv'
fname = os.path.join(dir1, dir2, archivo)

#Levanto las dos series
df = pd.read_csv(fname, index_col = ['Time'], parse_dates = True)
dh = dh['10-01-2014':].copy()  #último trimestre
freq_horaria = 60 #4 para 15 min, 60 para 1 min
cant_horas = 24
N = cant_horas * freq_horaria
#resampleo cada tantos minutos
dh = dh.resample(f'{int(60/freq_horaria)}T').mean()
#relleno los NaNs suavemente
dh = dh.interpolate(method = 'quadratic')
#genero vector de desplazamientos (enteros)
ishifts = np.arange(-N, N+1)
#y su desplazamiento horario asociado
shifts = ishifts / freq_horaria
#finalmente calculo las correlaciones correspondientes
corrs = np.zeros(shifts.shape)

for i, sh in enumerate(ishifts):
    corrs[i] = pearsonr(dh['H_SF'].shift(sh)[N:-N], dh['H_BA'][N:-N])[0]

#y grafico
plt.plot(shifts, corrs)

#el comando np.argmax(corrs) nos devuelve la coordenada de máxima correlación
max_corrs = np.argmax(corrs)
time_max_corrs = shifts[max_corrs]
print('Hay un desfasaje de ', abs(time_max_corrs*60), ' minutos')



