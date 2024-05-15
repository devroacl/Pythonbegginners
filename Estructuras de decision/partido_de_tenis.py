'''
Un partido de tenis se divide en sets.Para ganar un set, 
un jugador debe ganar 6 juegos, pero además debe haber 
ganado por lo menos dos juegos más que su rival. Si el set 
está empatado a 5 juegos, el ganador es el primero que llegue a 7.
Si el set está empatado a 6 juegos, el set se define en un último juego, 
en cuyo caso el resultado final es 7-6.Sabiendo que el 
jugador A ha ganado m juegos, y el jugador B, n juegos, determine:
● si A ganó el set, o
● si B ganó el set, o
● si el set todavía no termina, o
● si el resultado es inválido (por ejemplo, 8-6 o 7-3).'''

jA=int(input('Ingrese puntos Jugador A: '))
jB=int(input('Ingrese puntos Jugador B: '))
#comprobar jugadas NO válidas
if (jA>7 or jB>7) or (jA==7 and jB==7) or (jA==7 and jB<5) or (jB==7 and jA<5):
    print('Juego Inválido')
elif (jA<6 and jB<6) or (jA==6 and jB==5) or (jB==6 and jA==5):
    print('Juego NO ha terminado')
elif (jA>=jB+2) or (jA==7 and jB==6):
    print('Ganó A')
elif (jB>=jA+2) or (jB==7 and jA==6):
    print('Ganó B')
