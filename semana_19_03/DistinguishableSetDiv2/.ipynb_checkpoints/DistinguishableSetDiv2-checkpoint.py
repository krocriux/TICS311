# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:10:13 2018

@author: Cristian Javier López Portius and Maria José Gamonal Saenz

{"AA","AB","CC"} Returns: 2
{"XYZ","XYZ","XYZ"} Returns: 0
{"AAAA","BACA","CDCE"} Returns: 11
{"HGHHGUHUHI","BQHJWOSZMM","NDKSKCNXND","QOEOEIWIDS","IIQIWUNNZM"} Returns: 1017
{"XYZ","XAB","YAC"} Returns: 5

"""



def count(answer) :
    contador = 0
    sets = operador(len(answer[0]))
    for sett in sets:
        if verificacion(answer, sett):
            contador += 1
    return contador
        
def verificacion(answer, conjunto):
    variable_retorno = True
    conjunto_a_verificar = []
    for string in answer:
        conjunto_iterable = []
        for index in conjunto:
            conjunto_iterable.append(string[index])
        conjunto_iterable = "".join(conjunto_iterable)
        conjunto_a_verificar.append(conjunto_iterable)
    for i in range(len(conjunto_a_verificar)):
        for j in range(i + 1,len(conjunto_a_verificar)):
            if conjunto_a_verificar[i] == conjunto_a_verificar[j] and variable_retorno:
                variable_retorno = False
                
    return variable_retorno

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