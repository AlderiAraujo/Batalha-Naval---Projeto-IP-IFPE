import pygame

matriz = []

linha = 8
coluna = 8

AZUL = (0, 0, 255)

for l in range(0, linha):
    listaLinha = []
    for c in range(0, coluna):
        listaLinha.append(0)
    matriz.append(listaLinha)


