# -*- coding: utf-8 -*-
"""
Created on Sun May 30 21:00:05 2021

@author: Sabri
"""

#factorial.py
def factorial(n):
    if n == 1:
        r = 1
        return r
    
    f = factorial(n - 1)
    r = n * f
    return r