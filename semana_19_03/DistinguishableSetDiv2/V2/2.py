# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 16:06:38 2018

@author: Cristian
"""
def conjuntos(n_items, conjunto):
    conjunto_final = []
    if not n_items >= 1:
        conjunto_final.append([])
    else:
        for n1 in conjunto:
            conjunto_1 = [n1]
            if n_items <= 1:
                conjunto_final.append(conjunto_1)
            else:
                for n2 in conjunto:
                    conjunto_2 = conjunto_1 + [n2]
                    if n_items <= 2:
                        conjunto_final.append(conjunto_2)
                    else:
                        for n3 in conjunto:
                            conjunto_3 = conjunto_2 + [n3]
                            if n_items <= 3:
                                conjunto_final.append(conjunto_3)
                            else:
                                for n4 in conjunto:
                                    conjunto_4 = conjunto_3 + [n4]
                                    if n_items <= 4:
                                        conjunto_final.append(conjunto_4)
                                    else:
                                        for n5 in conjunto:
                                            conjunto_5 = conjunto_4 + [n5]
                                            if n_items <= 5:
                                                conjunto_final.append(conjunto_5)
                                            else:
                                                for n6 in conjunto:
                                                    conjunto_6 = conjunto_5 + [n6]
                                                    if n_items <= 6:
                                                        conjunto_final.append(conjunto_6)
                                                    else:
                                                        for n7 in conjunto:
                                                            conjunto_7 = conjunto_6 + [n7]
                                                            if n_items <= 7:
                                                                conjunto_final.append(conjunto_7)
                                                            else:
                                                                for n8 in conjunto:
                                                                    conjunto_8 = conjunto_7 + [n8]
                                                                    if n_items <= 8:
                                                                        conjunto_final.append(conjunto_8)
                                                                    else:
                                                                        for n9 in conjunto:
                                                                            conjunto_9 = conjunto_8 + [n9]
                                                                            if n_items <= 9:
                                                                                conjunto_final.append(conjunto_9)
                                                                            else:
                                                                                for n10 in conjunto:
                                                                                    conjunto_10 = conjunto_9 + [n10]
                                                                                    if n_items == 10:
                                                                                        conjunto_final.append(conjunto_10)
    #aqui seguimos, porque hasta ahora conjunto_final tiene duplicados
    conjunto_temporal = []
    for i in conjunto_final:
        if len(set(i)) == len(i):
            i.sort()
            if not i in conjunto_temporal:
                conjunto_temporal.append(i)
    
    return conjunto_temporal