#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:15:14 2018

@author: María José Gamonal Sáenz
         Cristian López
"""
import math

def speed_typer(letters, times) :
    
    more_than_avarage = "" #lo que se va a retornar
    n = len(letters) #numero de letras
    real_time = [0]*n #tiempo real que se demoraron
    
    minimo = min(times) #la primera tecla
    
    for i in range(n):
        # encontrar la tecla que venia antes y guardar el tiempo real que tardo
        mini = math.inf 
        for j in range(n):
            t = times[i]-times[j]
            if t>0 and t<mini :
                mini = t
        if times[i] == minimo:
            mini = times[i] 
        
        real_time[i] = mini
        
    #se encuentar el promedio    
    prom = sum(real_time) / n
    
    #se recorre nuevamente buscando aquellas letras que se demoraron  más que el promedio
    for k in range(n):
        if real_time[k]>prom :
            more_than_avarage += str(letters[k]) 
    
    return more_than_avarage

