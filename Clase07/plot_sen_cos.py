# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 17:52:06 2021

@author: Sabri
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

plt.plot(X, S)
plt.plot(X, C)

plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt

#Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada
plt.figure(figsize = (10, 6), dpi = 80)

#Crea un nuevo subplot, en una grilla de 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
 
#Plotea el coseno con una línea azul continua de ancho 1 (en pixeles)
#con label y plt.legend pone nombre a los graficos
plt.plot(X, C, color = 'blue', linewidth = 2.5, linestyle = '-', label = 'coseno')

#Plotea el seno con una línea verde continua de ancho 1 (en pixeles)
plt.plot(X, S, color = 'red', linewidth = 2.5, linestyle = '-', label = 'seno')

#Rango del eje x
plt.xlim(X.min() * 1.1, X.max() * 1.1)

#Ponemos marcas (ticks) en el eje x
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

#Rango del eje y
plt.ylim(C.min() * 1.1, C.max() * 1.1)

#Ponemos marcas (ticks) en el eje y
plt.yticks([-1, 0, 1],
           [r'$-1$', r'$0$', r'$+1$'])

#Podemos grabar el gráfico (con 72 dpi)
#plt.savefig('ejericio_2.png', dpi = 72)

#mover el contorno
ax = plt.gca()  #gca es 'get current axis' o 'tomar eje actual'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

#legendas (vienen del label)
plt.legend(loc='upper left')

#Puntos interesantes usando el comando annotate, elegimos 2pi/2 y marcamos
#el seno como el coseno. Vamos a dibujar una marca en la curva y una linea
#recta punteada. Vamos a usar annotate para mostrar texto y una flecha
#para destacar el valor de las funciones

t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color = 'blue', linewidth = 2.5, linestyle = '--')
plt.scatter([t, ], [np.cos(t), ], 50, color = 'blue')
plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90,-50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

plt.plot([t, t], [0, np.sin(t)], color = 'red', linewidth = 2.5, linestyle = '--')
plt.scatter([t, ], [np.sin(t), ], 50, color = 'red')
plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
              xy=(t, np.sin(t)), xycoords='data',
              xytext=(10, 30), textcoords='offset points', fontsize=16,
              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
#Mostramos el resultado en pantalla
plt.show()
