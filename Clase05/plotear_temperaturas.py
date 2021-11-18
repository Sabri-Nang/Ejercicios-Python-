# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 05:29:09 2021

@author: Sabri
"""

#Ejercicio 5.8: Empezando a plotear

import numpy as np
import matplotlib.pyplot as plt

path_file = '../Data/temperaturas.npy'
temperaturas = np.load(path_file)
plt.hist(temperaturas, bins=50)


