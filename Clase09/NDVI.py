# -*- coding: utf-8 -*-
"""
Created on Wed May 19 00:56:53 2021

@author: Sabri
"""

import numpy as np
import os
import matplotlib.pyplot as plt

dir1 = '../Data/clip'
red = 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band4_clip.npy'
blue = 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band2_clip.npy'
green = 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band3_clip.npy'
nir = 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band5_clip.npy'

#Levanto las bandas
bR = np.load(os.path.join(dir1, red))
bG = np.load(os.path.join(dir1, green))
bB = np.load(os.path.join(dir1, blue))
bNIR = np.load(os.path.join(dir1, nir))

#ploteo las bandas
#%%
fig = plt.figure()
fig.suptitle('Bandas sin ajustar los colores')
ax1 = fig.add_subplot(221)
ax1.imshow(bR)
ax1.set_title('Banda del rojo')

ax2 = fig.add_subplot(222)
ax2.imshow(bG)
ax2.set_title('Banda del verde')

ax3 = fig.add_subplot(223)
ax3.imshow(bB)
ax3.set_title('Banda del azul')

ax4 = fig.add_subplot(224)
ax4.imshow(bNIR)
ax4.set_title('Banda del infrarrojo')

#%%

#Para ver el contraste hago los histogramas de los valores de las matrices
#así puedo ver entre que valores se refleja

#histograma de los valores de la matriz bR
#Veo que hay valores que reflejan mas y otros menos
#tiene relevancia entre esos valores

fig = plt.figure()

fig.suptitle('Histogramas')
ax1 = fig.add_subplot(221)
ax1.hist(bR.flatten(), bins = 250, range=(0, 2))
ax1.set_title('Histograma del rojo')

ax2 = fig.add_subplot(222)
ax2.hist(bG.flatten(), bins = 250, range=(0, 2))
ax2.set_title('Histograma del verde')

ax3 = fig.add_subplot(223)
ax3.hist(bB.flatten(), bins = 250, range=(0, 2))
ax3.set_title('Histograma del azul')

ax4 = fig.add_subplot(224)
ax4.hist(bNIR.flatten(), bins = 250, range=(0, 5))
ax4.set_title('Histograma del infrarrojo')

#%%
#Bandas ajustando los colores

fig = plt.figure()
fig.suptitle('Bandas luego de ajustar vmin vmax')
ax1 = fig.add_subplot(221)
ax1.imshow(bR, vmin = 0.3, vmax = 2)
ax1.set_title('Banda del rojo')

ax2 = fig.add_subplot(222)
ax2.imshow(bG, vmin = 0.3, vmax = 2)
ax2.set_title('Banda del verde')

ax3 = fig.add_subplot(223)
ax3.imshow(bB, vmin = 0.3, vmax = 1.5)
ax3.set_title('Banda del azul')

ax4 = fig.add_subplot(224)
ax4.imshow(bNIR, vmin = 1, vmax = 5)
ax4.set_title('Banda del infrarrojo')

#%%Tomando el percentil al 25, o sea el 25%
q = 25

fig = plt.figure()
fig.suptitle('Bandas luego de ajustar vmin vmax')
ax1 = fig.add_subplot(221)
vmin = np.percentile(bR.flatten(), q)
vmax = np.percentile(bR.flatten(), 100 - q)
ax1.imshow(bR, vmin = vmin, vmax = vmax)
ax1.set_title('Banda del rojo')

ax2 = fig.add_subplot(222)
vmin = np.percentile(bG.flatten(), q)
vmax = np.percentile(bG.flatten(), 100 - q)
ax2.imshow(bG, vmin = vmin, vmax = vmax)
ax2.set_title('Banda del verde')

ax3 = fig.add_subplot(223)
vmin = np.percentile(bB.flatten(), q)
vmax = np.percentile(bB.flatten(), 100 - q)
ax3.imshow(bB, vmin = vmin, vmax = vmax)
ax3.set_title('Banda del azul')

ax4 = fig.add_subplot(224)
vmin = np.percentile(bNIR.flatten(), q)
vmax = np.percentile(bNIR.flatten(), 100 - q)
ax4.imshow(bNIR, vmin = vmin, vmax = vmax)
ax4.set_title('Banda del infrarrojo')

#%%
def crear_img_png(carpeta, banda):
    '''Dada una carpeta y un número de banda 
    muestra la imagen de dicha banda y la guarda en 
    .png.
    '''
    for root, dirs, files in os.walk(dir1):
        for name in files:            
            if f'band{banda}' in name:
                archivo = os.path.join(root, name)            
                band = np.load(archivo)
                q = 25
                vmin = np.percentile(bB.flatten(), q)
                vmax = np.percentile(bB.flatten(), 100 - q)
                im = plt.imshow(band, vmin = vmin, vmax = vmax)
                plt.colorbar(im)
                plt.title(f'Banda {banda}')
                plt.savefig(os.path.join(carpeta,f'banda{banda}.png'))
                plt.close()

#%%
def crear_hist_png(carpeta, banda, bins):
    '''Dada una carpeta, un número de banda y una cantidad de bins
    muestra la imagen de dicho histograma y la guarda en 
    .png.
    '''
    for root, dirs, files in os.walk(dir1):
        for name in files:            
            if f'band{banda}' in name:
                archivo = os.path.join(root, name)            
                band = np.load(archivo)
                plt.hist(band.flatten(), bins = bins, range = (0, 5))
                plt.title(f'Histograma banda {banda}')
                plt.savefig(os.path.join(carpeta,f'histograma_banda{banda}.png'))
                plt.close()
            
#%%Ejercicio 9.17
#Genero todas las imágenes y las guardo en la carpeta imagenes

for i in range(1, 8):
    crear_img_png('imagenes', i)
    crear_hist_png('imagenes', i, 250)
    
#Tomando la banda del rojo (banda 4)
#Puedo ver que entre 0 y 0.5 hay una distribucion y otra de 0.5 en adelante
#En menos de 0.5 hay pixeles reflejando menos y mas en 0.5 en adelante
#%%
#armo una matriz del mismo tamaño que bR
mascara = bR.copy()

for i, v in enumerate(mascara):
    for j, u in enumerate(v):
        if u > 0.5:
            mascara[i][j] = 1
        else:
            mascara[i][j] = 0
#grafico
im = plt.imshow(mascara)
plt.colorbar(im)
plt.title('Mascara rojo')

#mas simple
mascara = bR.copy()
mascara[mascara > 0.5] = 1
mascara[mascara <= 0.5] = 0
            
#%%Ejercicio 9.18
#(INFRARROJO_CERCANO - ROJO) / (INFRARROJO_CERCANO + ROJO)
red = 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band4_clip.npy'
nir = 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band5_clip.npy'

dir1 = '../Data/clip'
bR = np.load(os.path.join(dir1, red))
bNIR = np.load(os.path.join(dir1, nir))
try:
    NDVI = (bNIR - bR) / (bNIR + bR)
except:
    pass

clases_ndvi = NDVI.copy()
for i, f in enumerate(clases_ndvi):
    for j, c in enumerate(f):
        if c < 0:
            clases_ndvi[i][j] = 0
        elif 0 < c and c < 0.1:
            clases_ndvi[i][j] = 1
        elif 0.1 < c and c < 0.25:
            clases_ndvi[i][j] = 2
        elif 0.25 < c and c < 0.4:
            clases_ndvi[i][j] = 3
        elif c > 0.4:
            clases_ndvi[i][j] = 4
#propusieron hacer 
#nvdi2[(0 < nvdi2) & (nvdi2 < 0.1)] = 1
      
from matplotlib import colors
# Creo colores
cmap = colors.ListedColormap(['black', 'y',
                              'yellowgreen', 'green', 'darkgreen'])
# Defino los limites de cada color
limites = [0, 1, 2, 3, 4]
norm = colors.BoundaryNorm(limites, cmap.N)
# Genero el grafico con colores
#plt.imshow(clases_ndvi, cmap=cmap, norm=norm)

import matplotlib.patches as mpatches
# Genero leyenda y grafico con leyenda
texts = ['Sin vegetacion', 'Area desnuda', 'Vegetacion baja',
         'Vegetacion moderada', 'Vegetacion densa']
patches = [mpatches.Patch(color=cmap(i), label="{:s}".format(texts[i]) ) for i in range(len(texts))]
plt.legend(handles=patches, bbox_to_anchor=(0.2,1.3), loc='center', ncol=1 )
plt.imshow(clases_ndvi, cmap=cmap, norm=norm)
plt.show()

#otra forma para ver la leyenda
# plt.figure(figsize=(9,7))
# patches = [mpatches.Patch(color=cmap(i), label="{:s}".format(texts[i]) ) for i in range(len(texts))]
# plt.legend(handles=patches, bbox_to_anchor=(1.01,0.5,0.5, 0.5),
#           loc= 'upper left', borderaxespad = 0, prop={'size': 6})

# #plt.legend(handles=patches, bbox_to_anchor=(0.2,1.3), loc='center', ncol=1 )
# plt.imshow(clases_ndvi, cmap=cmap, norm=norm)
# plt.show()
#Falta el ejercicio 9.19

