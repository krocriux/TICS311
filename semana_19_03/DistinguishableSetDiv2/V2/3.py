# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 07:58:32 2018

@author: Cristian
"""

def for_recursivo(conjunto, n):
    conjunto_inicial = conjunto
    conjunto_retornar = []
    for i in range(n):
        conjunto_en_for = conjunto_inicial + [i]
        conjunto_retornar.append(conjunto_en_for)
    return conjunto_retornar
        
    
def operador(n):
    conjunto = []
    conj = for_recursivo(conjunto, n)
    for i in conj:
        conjunto.append(i)
    for i in range(n - 1):
        conj, conjunto = auxiliar(conjunto, conj, n)
    """ el largo se le resta 1 por que no agregamos el conjunto vacio """
    if len(conjunto) == ((2 ** n) - 1):
        print("Se encontraron las combinaciones adecuadamente")
        return conjunto
    else:
        print("El numero de combinaciones no coincide con las que tiene que haber")

def auxiliar(conjunto, conjunto_iterar, n):
    conj = []
    for i in conjunto_iterar:
        c = for_recursivo(i, n)
        for j in c:
            j.sort()
            if len(set(j)) == len(j) and not j in conjunto:                
                conjunto.append(j)
                conj.append(j)
    return conj, conjunto

for i in range(10):
    print("Aqui los resultados para i = {}".format(i))
    print(operador(i))