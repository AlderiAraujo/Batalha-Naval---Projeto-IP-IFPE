from modulo.jogo import *

tela = pygame.display.set_mode((1060,500))
pygame.display.set_caption("Batalha Naval")
RED = (255, 0, 0)
GREY = (50, 50, 50)
WHITE = (255, 255, 255)
tela.fill(GREY)

jogador1 = Tabuleiro(tela, 610, 50)
jogador2 = Tabuleiro(tela, 50, 50)
VEZ = 'JOGADOR1'



def verifica_vencedor():

    if jogador1.quant_barcos == 9:
        Vencedor1 = pygame.image.load("./modulo/Repositorio-Imagens/Vencedor1.jpg")
        Vencedor1Img = pygame.transform.scale(Vencedor1, (150, 150))
        print("JOGADOR 1 VENCEU")
        tela.blit(Vencedor1Img, (450, 200))
        pygame.time.wait(5000)
        return True
    elif jogador2.quant_barcos == 9:
        Vencedor2 = pygame.image.load("./modulo/Repositorio-Imagens/Vencedor2.jpg")
        Vencedor2Img = pygame.transform.scale(Vencedor2, (150, 150))
        print("JOGADOR 2 VENCEU")
        tela.blit(Vencedor2Img, (450, 200))
        pygame.time.wait(5000)
        return True



continuar = True
while continuar:

    for event in pygame.event.get():
        pygame.draw.rect(tela, RED, [525, 0, 10, 500])  # linha divisória dos tabuleiros
        if event.type == pygame.QUIT:   #condição para saída do loop de eventos, apertando o botão "X" da janela
            continuar = False

        if verifica_vencedor():
            continuar = False

        if VEZ == 'JOGADOR1':
            if event.type == pygame.MOUSEBUTTONDOWN:
                jogador1.avalia_clique(tela)
                VEZ = 'JOGADOR2'


        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                jogador2.avalia_clique(tela)
                VEZ = 'JOGADOR1'


    pygame.display.update() #comando para atualização de frame