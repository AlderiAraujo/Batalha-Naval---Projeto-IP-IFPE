#Arquivo cópia do Main para efeito de teste, deve ser apagado no fim do projeto
import pygame
from modulo.TabuleiroTest import *


tela = pygame.display.set_mode((1060,500))
pygame.display.set_caption("Batalha Naval")
RED = (255, 0, 0)
GREY = (50, 50, 50)

tela.fill(GREY)


continuar = True
while continuar:
    for event in pygame.event.get():
        pygame.draw.rect(tela, RED, [525, 0, 10, 500])  # linha divisória dos tabuleiros
        if event.type == pygame.QUIT:   #condição para saída do loop de eventos, apertando o botão "X" da janela
            continuar = False

        #funções de tabuleiro

        tabuleiroJogador = Tabuleiro(tela, 50, 50)

        tabuleiroJogador2 = Tabuleiro(tela, 610, 50)

        if event.type == pygame.MOUSEBUTTONDOWN:
            #tabuleiroJogador.avaliaCliqueTabuleiro()
            #print(tabuleiroJogador.pos_clicada)

            tabuleiroJogador2.avaliaCliqueTabuleiro()
            print(tabuleiroJogador2.pos_clicada)




    #funções de jogabilidade
    pygame.display.update() #comando para atualização de frame