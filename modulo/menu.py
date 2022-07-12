import pygame
import sys
pygame.font.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
fundoMenu = pygame.image.load("./modulo/Repositorio-Imagens/fundoMenu.jpeg")
fundoMenuFormat = pygame.transform.scale(fundoMenu, (1060, 500))
fonteTextoMenu = pygame.font.SysFont("Unispace", 50)

class botao ():
    def __init__(self, imagem, textoInserido, fonte, cor):
        self.imagem = imagem
        self.X = pos[0]
        self.Y = pos[1]
        self.fonte = fonte
        self.cor = cor
        self.textoInserido = texto
        self.texto = self.font.render(self.textoInserido, True, self.cor)
        if self.imagem is None:
            self.imagem = self.texto
        self.rect = self.imagem.get_rect(center = (self.X, self.Y))
        self.textoRect = self.texto.get_rect(center = (self.X, self.Y))

    def update(self, tela):
        if self.imagem is not None:
            tela.blit(self.imagem, self.rect)
        tela.blit(self.texto, self.textoRect)

    def checkInput (self, posicao):
        if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.botton):
            return True
        return False

def menu (tela):
    tela.blit(fundoMenuFormat, (0, 0))
    tela.fill(BLACK)

    posicaoMouse = pygame.mouse.get_pos()
    menuTexto = pygame.font.Font.render()
    menuRect = menuTexto.get_rect(center = (350, 100))

    tela.blit(menuTexto, menuRect)

    botaoPlay = botao(imagem = pygame.draw.rect(tela, WHITE, [350, 200, 80, 60]), textoInserido = "JOGAR", fonte = pygame.font.Font.render(45), cor = BLACK)
    botaoSair = botao(imagem = pygame.draw.rect(tela, WHITE, [350, 300, 80, 60]), textoInserido = "SAIR", fonte = pygame.font.Font.render(45), cor = BLACK)

    for botao in [botaoPlay, botaoSair]:
        botao.update(tela)

    if event.type == pygame.MOUSEBUTTONDOWN:
        if botaoPlay.checkInput(posicaoMouse):
            play()
        if botaoSair.checkInput(posicaoMouse):
            pygame.quit()
            sys.exit()