# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:25:22 2018

@author: Cristian
"""

def count(n) :
    contador = 0
    for integer in range(1,n) :
        
        if son_diferentes(integer) :
            
            contador += 1
    return contador
        
        
def son_diferentes(number) :
    number = [int(i) for i in str(number)]
    numeros = []
    estado = True
    for i in range(len(number)) :
        diff = 0
        for n in numeros:
            if number[i] == n :
                estado = False
            else :
                diff += 1
        if diff == 0 :
            numeros.append(number[i])
    return estado

print(count(21))
        