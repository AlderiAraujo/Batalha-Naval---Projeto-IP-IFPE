import pygame
from modulo.TabuleiroTest import *

tuplas_sorteadas = []
while True:
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


    print(tuplas_sorteadas)
