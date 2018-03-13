#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:44:59 2018

@author: María José Gamonal Sáenz
         Cristian Lopez
"""

from SpeedTyper import speed_typer

letters = ["dcab", "keyboard", "rewq", "abc"]

times =[ [250, 300, 400, 800], [100,200,300,500,600,800,900,1200] , [500, 1000, 1500, 4000] ,  [2000, 4000, 6000] ]

real_results = ["db","bad","q",""]

for i in range(len(letters)):
    print("Prueba "+str(i+1))
    result = speed_typer(letters[i], times[i])
    if result == real_results[i]:
        print("Aprobada")
    else:
        print("Reprobada")
    print("")
