# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 02:51:50 2021

@author: Sabri
"""
import numpy as np
import matplotlib.pyplot as plt
 
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.figure()
plt.bar(X, +Y1, facecolor = '#9999ff', edgecolor = 'white')
plt.bar(X, -Y2, facecolor = '#ff9999', edgecolor = 'white')
for x, y in zip(X, Y1):
    plt.text(x + 1, y + 0.05, '%.2f' % y, ha = 'right', va = 'bottom')
for x, y in zip(X, Y2):
    plt.text(x + 1, - y - 0.05, '%.2f' % y, ha = 'right', va = 'top')
plt.ylim(-1.25, +1.25)
