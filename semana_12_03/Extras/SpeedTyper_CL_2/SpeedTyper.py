# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:37:34 2018

@author: Cristian
"""
def lettersToPractice(letters,times):
    last = 0
    suma = 0
    for instant in times:
        suma += instant - last
        last = instant
    avg = int(suma/len(times))
    lettersToPractice = []
    last = 0
    for i in range(len(times)):
        if (times[i] - last) > avg :
            lettersToPractice.append(letters[i])
        last = times[i]
    return "".join(lettersToPractice)

