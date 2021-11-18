# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 03:55:13 2021

@author: Sabri
"""
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
ax = plt.axes([0, 0, 1, 1], polar = True)
N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.show()
