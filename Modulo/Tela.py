import pygame
#varáveis com as proporções que irão compor a tela do jogo
largura = 1080
altura = 480

try: #iniciando o pygame
    pygame.init()
except:
    print("Pygame com falha")
#inicialização da tela
tela_fundo = pygame.display.set_mode((largura,altura))  #definição da proporção da tela
pygame.display.set_caption("Batalha Naval")             #título da janela
#loop para atualização de frames
sair = True
while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #condição para saída, apertando o botão "X" da janela
            sair = False
    pygame.display.update() #comando para atualização de frame

pygame.quit()   #comando para fechar a janela do game