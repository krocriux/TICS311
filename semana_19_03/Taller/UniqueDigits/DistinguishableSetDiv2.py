# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:10:13 2018

@author: Cristian
"""



def count(answer) :
    contador = 0
    ind_status = index_status(answer)
    sets = posible_sets(len(answer[0]))
    for sett in sets:
        indicador = False
        if len(sett) > 0 :
            for indice in sett:
                if ind_status[indice]:
                    indicador = ind_status[indice]
        if indicador:
            contador = contador + 1
    return contador
        
                
        
    
               

def index_status(answer) :
    n = len(answer)
    len_ans = len(answer[0])
    answer = [list(i) for i in answer]
    index_status = [False]*len_ans
    for j in range(len_ans) :
        list1 = []
        for i in range(n) :
            list1.append(answer[i][j])
        list2 = set(list1)
        if len(list1) == len(list2) :
            index_status[j] = True
    return index_status

def posible_sets(n):
    lista1 = [i for i in range(n)]
    lista2 = []
    lista_temporal = [lista1]
    lista_final = []
    while len(lista_temporal) > 0:
        for i in lista_temporal:
            lista_auxiliar1 = []
            for j in i:
                lista_auxiliar2 = []
                for k in i:
                    if not k == j:
                        lista_auxiliar2.append(k)
                lista_auxiliar1.append(lista_auxiliar2)
            lista_final.extend(lista_temporal)
            lista_temporal = []
            lista_temporal.extend(lista_auxiliar1)
    for i in lista_final:
        i.sort()
        lista_temporal.append(i)
    lista_final = []
    for i in lista_temporal:
        indicador = True
        for j in lista_final:
            if i==j:
                indicador = False
        if indicador:
            lista_final.append(i)
    
    return lista_final
        
            
        
        
        
        
        
        
        
        
        
        
        
        
    