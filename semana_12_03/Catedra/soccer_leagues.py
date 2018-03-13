# -*- coding: utf-8 -*-

"""
'W' represents a home team victory, 'D' represents a draw,
and 'L' represents an away team victory. All characters on the main diagonal
of matches will be '-' because a team never plays against itself.
"""

RESULTADOS = ['W', 'D', 'L']
OPUESTOS = {'W': 'L', 'D': 'D', 'L': 'W'}
PUNTAJES = {'W': 3, 'D': 1, 'L': 0}


def points(matches):
    n = len(matches)
    puntos = [0 for i in range(n)]

    for local in range(n):
        for visitante in range(n):
            if visitante != local:
                resultado_local = matches[local][visitante]
                puntaje_local = PUNTAJES[resultado_local]
                puntos[local] += puntaje_local

                resultado_visitante = OPUESTOS[resultado_local]
                puntaje_visitante = PUNTAJES[resultado_visitante]
                puntos[visitante] += puntaje_visitante

    return puntos
