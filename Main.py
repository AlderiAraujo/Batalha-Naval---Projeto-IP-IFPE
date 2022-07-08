import pygame
from modulo.Tabuleiro import fundoTabuleiro, tabuleiroPlayer1, tabuleiroPlayer2
from modulo.Jogabilidade import *


pygame.display.set_caption("Batalha Naval")


continuar = True
while continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #condição para saída do loop de eventos, apertando o botão "X" da janela
            continuar = False
    #funções de tabuleiro
        fundoTabuleiro()
        tabuleiroPlayer1()
        tabuleiroPlayer2()
    #funções de jogabilidade
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass



    pygame.display.update() #comando para atualização de frame