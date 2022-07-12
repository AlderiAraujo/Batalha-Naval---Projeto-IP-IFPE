import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
fundoMenu = pygame.image.load(f"./modulo/Repositorio-Imagens/fundoMenu.jpeg")
fundoMenuFormat = pygame.transform.scale(fundoMenu, (1060, 500))
pygame.font.init

def menu (tela):
    tela.blit(fundoMenuFormat, (0, 0))
    tela.fill(BLACK)

    posicaoMouse = pygame.mouse.get_pos()
    botaoPlay = (pygame.draw.rect(tela, WHITE, [350, 200, 70, 70]), "JOGAR", pygame.font.get_fonts()[60], BLACK)