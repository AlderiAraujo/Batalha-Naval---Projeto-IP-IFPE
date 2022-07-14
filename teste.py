import pygame
from modulo.jogo import *

tuplas_sorteadas = []
for i in range(0, 10):
    tupla = ()
    lista = [0, 1, 2, 3, 4, 5, 6, 7]
    pos_sorteada = []

    for i in range(0,2):
        pos_sorteada.append(random.choice(range(0, len(lista))))
    tupla = tuple(pos_sorteada)
    if tupla not in tuplas_sorteadas:
        tuplas_sorteadas.append(tupla)
    else:
        continue

tupla1 = tuplas_sorteadas[0]
tupla2 = tuplas_sorteadas[1]
tupla3 = tuplas_sorteadas[2]

print(tuplas_sorteadas)
print(tupla1)
print(tupla2)
print(tupla3)
