#Arquivo cópia do Main para efeito de teste, deve ser apagado no fim do projeto
import pygame
from Modulo.TabuleiroTest import *


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

        tabuleiroJogador = Tabuleiro(50, 50)
        tabuleiroJogador.desenhaTabuleiro(tela)

        tabuleiroJogador2 = Tabuleiro(610, 50)
        tabuleiroJogador2.desenhaTabuleiro(tela)

        if event.type == pygame.MOUSEBUTTONDOWN:
            #tabuleiroJogador.avaliaCliqueTabuleiro()
            tabuleiroJogador2.avaliaCliqueTabuleiro()

            """y = 50
            for l in range(0, 8):
                x = 50
                for c in range(0, 8):
                    if tabuleiroJogador.matrizTabuleiro[l][c].get_rect(topleft=(x, y)).collidepoint(mouse):
                        print("cliquei dentro do sprite\n")
                        print((x, y))
                        print(is_cliclked)
                    else:
                        print("Não pegou o clique")
                        #print((x, y), is_cliclked)
                    x += 50
                y += 50"""

            #if tabuleiroJogador.rect.collidepoint(x, y):
            #    print("cliquei dentro do sprite")
            #    print((x, y))
            #    print(is_cliclked)
           #else:
            #    print("Não pegou o clique")
            #    print((x, y), is_cliclked)

    #funções de jogabilidade
    pygame.display.update() #comando para atualização de frame