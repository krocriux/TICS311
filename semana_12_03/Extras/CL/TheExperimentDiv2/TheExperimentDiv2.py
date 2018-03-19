# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 08:44:14 2018

@author: Cristian
"""
intensity = [3, 4, 1, 1, 5, 6]
leftEnd = [3, 1, 0]
L = 3

def determineHumidity(intensity, L, leftEnd) :
    posiciones_bloqueadas = []
    total_gotas_esponja = [0]*len(leftEnd)
    j = 0
    for comienzo_esponja in leftEnd :
        for i in range(comienzo_esponja, comienzo_esponja + L) :
            if i not in posiciones_bloqueadas :
                total_gotas_esponja[j] += intensity[i]
                posiciones_bloqueadas.append(i)
        j += 1
    return total_gotas_esponja
    
    