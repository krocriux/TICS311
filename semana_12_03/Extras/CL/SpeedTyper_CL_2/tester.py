# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:31:23 2018

@author: Cristian
"""
from SpeedTyper import lettersToPractice

# Explamples from topcoder
Examples = {'db':["dcab",[250, 300, 400, 800]],
            'bad':["keyboard",[100,200,300,500,600,800,900,1200]],
            'q':["rewq",[500, 1000, 1500, 4000]],
            '':["abc",[2000, 4000, 6000]],
            }

def tester():
    # recorriendo las soluciones de ejemplo
    for key in Examples.keys():
        if lettersToPractice(Examples[key][0],Examples[key][1])==key:
            print("El programador clickeo las letras",
                  Examples[key][0],
                  "que tenían como tiempos",
                  Examples[key][1],
                  "y el programa retorno exitosamente",
                  key,)
            print()
        else:
            print("El programador clickeo las letras",
                  Examples[key][0],
                  "que tenían como tiempos",
                  Examples[key][1],
                  "y el programa retorno fallidamente",
                  lettersToPractice(Examples[key][0],Examples[key][1]),
                  "cuando debio haber retornado",
                  key,)
            print()
            
tester()
