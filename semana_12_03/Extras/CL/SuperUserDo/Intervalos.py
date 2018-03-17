# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 08:35:25 2018

@author: Cristian
"""

def intervalsMaker(A, B):
    #lista de listas para los intervalos de librerias a instalar
    libraries_to_install = []
    for i in range(len(A)) :
        if len(libraries_to_install) == 0 :
            libraries_to_install.append([A[i], B[i]])
        else :
            for j in range(len(libraries_to_install)):
                #3 casos en cada iteración:
                # -1. Que el intervalo nuevo este por debajo del intervalo actual (interval)
                # -2. Que el intervalo nuevo este dentro del intervalo actual (interval)
                # -3. Que el intervalo nuevo este por adelante del intervalo actual (interval)
                # -4. Intervalos se traslapan
                interval = libraries_to_install[j]
                memoria = libraries_to_install
                if interval[1] < A[i] or interval[0] > B[i]: # -1. or -3.
                    # append in libraries_to_install
                    #iterate to search in all intervals
                    for k in range(j + 1, len(libraries_to_install)):
                        # edit an interval, edit actual interval
                        if libraries_to_install[k][0] < A[i] and libraries_to_install[k][1] > B[i]:
                            # el intervalo [A[i], B[i]] está dentro de el intervalo actual
                            # no hacemos nada
                            print("El intervalo",[A[i], B[i]]," está contenido en el intervalo actual",[libraries_to_install[k][0], libraries_to_install[k][1]])
                            break
                        elif libraries_to_install[k][0] > A[i] and libraries_to_install[k][1] < B[i]:
                            # el intervalo [A[i], B[i]] está conteniendo de el intervalo actual
                            # actualizamos el valor de libraries_to_install[j]
                            libraries_to_install[k] = [A[i], B[i]]
                            break
                        elif libraries_to_install[k][0] < A[i] and libraries_to_install[k][1] < B[i]:
                            # el intervalo [A[i], B[i]] está desfasado hacia la derecha con respecto al intervalo actual
                            # por lo que el limite derecho se actualiza y el izquierdo no 
                            libraries_to_install[k][1] = B[i]
                            break
                        elif libraries_to_install[k][0] > A[i] and libraries_to_install[k][1] > B[i]:
                            # el intervalo [A[i], B[i]] está desfasado hacia la izquierda con respecto al intervalo actual
                            # por lo que el limite izquierdo se actualiza y el derecho no 
                            libraries_to_install[k][0] = A[i]
                            break
                        else:
                            continue
                    if memoria == libraries_to_install:
                        libraries_to_install.append([A[i], B[i]])
                else:
                    # edit an interval, edit actual interval
                    if interval[0] < A[i] and interval[1] > B[i]:
                        # el intervalo [A[i], B[i]] está dentro de el intervalo actual
                        # no hacemos nada
                        print("El intervalo",[A[i], B[i]]," está contenido en el intervalo actual",[interval[0], interval[1]])
                    elif interval[0] > A[i] and interval[1] < B[i]:
                        # el intervalo [A[i], B[i]] está conteniendo de el intervalo actual
                        # actualizamos el valor de libraries_to_install[j]
                        libraries_to_install[j] = [A[i], B[i]]
                    elif interval[0] < A[i] and interval[1] < B[i]:
                        # el intervalo [A[i], B[i]] está desfasado hacia la derecha con respecto al intervalo actual
                        # por lo que el limite derecho se actualiza y el izquierdo no 
                        libraries_to_install[j][1] = B[i]
                    elif interval[0] > A[i] and interval[1] > B[i]:
                        # el intervalo [A[i], B[i]] está desfasado hacia la izquierda con respecto al intervalo actual
                        # por lo que el limite izquierdo se actualiza y el derecho no 
                        libraries_to_install[j][0] = A[i]
    return libraries_to_install