# -*- coding: utf-8 -*-

from soccer_leagues import points

pruebas = []
resultados = []

pruebas.append(["-WW", "W-W", "WW-"])
resultados.append([6, 6, 6])

pruebas.append(["-DD", "L-L", "WD-"])
resultados.append([5, 2, 8])

pruebas.append(["-DWWD", "L-WLL", "DD-WD", "DDL-L", "DDLL-"])
resultados.append([14, 7, 12, 8, 10])

pruebas.append(
    [
        "-LWWLWDLDWWWWWWDDWDW",
        "D-WWLDDWDWDLWDDWLWDD",
        "LL-DLDWDLDLDWWWLWDDW",
        "LDD-LLLDLWLWWWWDWDWL",
        "LWWW-DWDLWDWDWWWDWDW",
        "DLLWD-WWLLDDDLWWDWWW",
        "WWLWDL-LLDWWWWWDWWLW",
        "LLLLLDW-LDLWDDLLLDWL",
        "DWWWWDDD-DWWWWDWWWDW",
        "WWWWLLLWL-LWWWWWLWWW",
        "DWWWWWWWLW-WDWWWWWWW",
        "DDDLLLDWWWL-DDWDWLDD",
        "LWLWLDLLLDLW-DDDWWDD",
        "LLWWLWDDLWLWL-WWWDLL",
        "WWWWLLDDDWLWDD-WWWLW",
        "DLDLLLWWLLLWWLW-DWLL",
        "DLWWWLDLWWDWWDWL-WWD",
        "LLDDLLWLLWLWLDLWW-WW",
        "LLWLLLWWLWLWWDWWLD-W",
        "LLWDLWDWDWLLWWDDWWL-"
    ]
)
resultados.append(
    [
        72, 62, 41, 41, 83, 63, 53, 35, 86, 50, 90, 32, 34, 41, 45, 36, 51, 32,
        51, 45]
)


for i in range(len(pruebas)):
    print("Prueba " + str(i))
    res = points(pruebas[i])
    if res == resultados[i]:
        print("¡Aprobada!")
    else:
        print("¡Reprobada!")
