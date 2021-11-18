# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:52:56 2021

@author: Sabri
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

dir1 = '..'
dir2 = 'Data'
file = 'OBS_SHN_SF-BA.csv'
fname = os.path.join(dir1, dir2, file)

#Creo el df
df = pd.read_csv(fname, index_col = ['Time'], parse_dates = True)

#Graficar los últimos datos
#df['12-25-2014':].plot()
#df['10-15-2014':'12-15-2014'].plot()


#copia de datos desde 12-25-2014
dh = df['12-25-2014':].copy()
delta_t = 0  #tiempo que tarda la marea entre ambos puertos
delta_h = 0  #diferencia de los ceros de escala entre ambos puertos
#Uso shift(delta_t) para desplazar la serie un valor delta_t

#pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()


#Busco delta_h como la diferencia de las medias
delta_h = dh['H_SF'].mean() - dh['H_BA'].mean()

#a mano delta_t=-1, una hora de diferencia

delta_t = -1
#delta_t = datetime.strptime(delta_t, '%d-%m-%Y %H:%m:%S')
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
plt.show()


