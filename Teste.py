#Arquivo cópia do Main para efeito de teste, deve ser apagado no fim do projeto
import pygame
from modulo.TabuleiroTest import *
from modulo.Jogabilidade import Jogabilidade
from modulo.menu import menu

tela = pygame.display.set_mode((1060,500))
pygame.display.set_caption("Batalha Naval")
RED = (255, 0, 0)
GREY = (50, 50, 50)

tela.fill(GREY)

tabuleiroJogador1 = Tabuleiro(tela, 50, 50)
tabuleiroJogador2 = Tabuleiro(tela, 610, 50)
#tabuleiroJogador1.desenhaMatrizJogavel(tela)
continuar = True
while continuar:
    for event in pygame.event.get():
        pygame.draw.rect(tela, RED, [525, 0, 10, 500])  # linha divisória dos tabuleiros
        if event.type == pygame.QUIT:   #condição para saída do loop de eventos, apertando o botão "X" da janela
            continuar = False

        #menu(tela)

        #funções de tabuleiro




        #funções de jogabilidade
        if event.type == pygame.MOUSEBUTTONDOWN:
            joga = Jogabilidade()
            joga.avaliaCliqueTabuleiro(50, 50, tabuleiroJogador1.matrizFundo)
            linha, coluna = joga.pos_clicada
            joga.inserirBarco('submarino')
            tabuleiroJogador1.atualiza(linha, coluna, joga.tipo.img, tela)

            #joga.avaliaCliqueTabuleiro(tabuleiroJogador2.matrizTabuleiro, 610, 50)
            #print(joga.pos_tela)
            #print(joga.pos_clicada)





    pygame.display.update() #comando para atualização de frame