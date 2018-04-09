# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:13:37 2018

@author: Cristian
"""

def minCost(altitude):
    n = len(altitude)
    cost = 0
    altitudes_rehechas = [0]*n
    for i in range(n):
        if i == 0:
            altitudes_rehechas[i] = altitude[i]
        else:
            if altitude[i] > altitudes_rehechas[i - 1]:
                cost += altitude[i] - altitudes_rehechas[i - 1]
                altitudes_rehechas[i] = altitudes_rehechas[i - 1]
    return 
        