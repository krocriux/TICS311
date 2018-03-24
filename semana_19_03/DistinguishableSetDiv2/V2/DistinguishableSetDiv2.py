# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:13:59 2018

@author: Cristian
"""
def conjuntos(n_items, conjunto):
    conjunto_final = []
    conjunto_final = for_anidado(len(conjunto), [], conjunto_final)

    return conjunto_final

def for_anidado(n, conjunto_actual, conjunto_final):
    print("Llamada a for_anidad con los siguientes valores: n, conjunto_actual, conjunto_final:",n, conjunto_actual, conjunto_final)
    for i in range(n):
        conjunto_temporal = conjunto_actual + [i]
        itemes = len(conjunto_temporal)
        if itemes == n:
            conjunto_final.append(conjunto_temporal)
            return conjunto_final
        elif itemes <= n:
            for_anidado(n, conjunto_temporal, conjunto_final)
            
conjuntos(1, [0, 1, 2, 3, 4, 5])