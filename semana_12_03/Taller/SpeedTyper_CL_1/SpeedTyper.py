# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 13:39:14 2018

@author: Cristian
"""

import random

letters = "aswer"

def crear_tiempo(words):
    instante_tiempo = 0
    times = [0 for i in range(len(words))]
    for i in range(len(words)):
        instante_tiempo = instante_tiempo + random.randint(0,10000)
        times[i] = instante_tiempo
    return times
            
times = crear_tiempo(letters)

def lettersToPractice(letters,times):
    avg = 0
    suma = 0
    last_instant = 0
    tiempos = [0 for i in range(len(times))]
    k = 0
    for instante in times:
        tiempo = instante - last_instant
        last_instant = instante
        tiempos[k] = tiempo
        suma = suma + tiempo
        k = k + 1
        if k == len(times):
            avg = int(suma/len(times))
    posisiones_letras_a_trabajar = []
    for i in range(len(times)):
        if tiempos[i] > avg:
            posisiones_letras_a_trabajar.append(tiempos[i])
    letras_a_trabajar = []
    kk = 0
    print(letters)
    for kk in range(len(letters)):
        for j in range(len(posisiones_letras_a_trabajar)):
            if kk == j:
                print(letters[kk])
                letras_a_trabajar.append(letters[kk])
        kk = kk + 1
    print(tiempos)
    return "".join(letras_a_trabajar)

letras_trabajar = lettersToPractice(letters,times)
print(letras_trabajar)
        
        
        
        
        
        
        

        
    