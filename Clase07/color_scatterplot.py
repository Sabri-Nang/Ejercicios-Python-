# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 04:23:48 2021

@author: Sabri
"""
import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)
plt.figure()
plt.axes([0.025, 0.025, 0.95, 0.95]) #margenes recuadro grafico
                                     #[left, bottom, width, height]
plt.scatter(X, Y, s = 95, c = T, alpha = .5)
plt.xlim(-1.5, 1.5)
plt.xticks([])
plt.ylim(-1.5, 1.5)
plt.yticks([])
plt.show()