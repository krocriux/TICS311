# -*- coding: utf-8 -*-

import random as rnd

"""
'W' represents a home team victory, 'D' represents a draw,
and 'L' represents an away team victory. All characters on the main diagonal
of matches will be '-' because a team never plays against itself.
"""
RESULTADOS = ['W', 'D', 'L']
OPUESTOS = {'W': 'L', 'D': 'D', 'L': 'W'}


def crea_partidos(n):
    """Crea matriz de RESULTADOS de partidos para el problema SoccerLeagues


    Argumentos:
    n - indica la cantidad de equipos
    """

    partidos = [['-' for visitante in range(n)] for local in range(n)]
    for local in range(n):
        for visitante in range(n):
            if local != visitante:
                resultado = rnd.choice(RESULTADOS)
                partidos[local][visitante] = resultado

    resultado = []
    for i in range(n):
        resultado.append("".join(partidos[i]))
    return resultado


#funcion con los puntajes de cada equipo
st = crea_partidos(3)
print(st)


def points_league(matches):
    n = len(matches)
    points =[0]*n 
    for i in range(n):
        for j in range(n):
            if matches[i][j] == "D" :
                points[i] += 1
                points[j] += 1
            if matches[i][j] == "W" :
                points[i] += 3
            if matches[i][j] == "L" :
                points[j] += 3
    return points

pt = points_league(st)
print(pt)
