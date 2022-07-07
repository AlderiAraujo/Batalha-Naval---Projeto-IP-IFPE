import pygame
from Modulo.Jogabilidade import cliqueEsquerdo


class Tabuleiro(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.imgOceano = pygame.image.load("./Modulo/Repositorio-Imagens/oceano.jpg")
        self.imgOceanoFormat = pygame.transform.scale(self.imgOceano, (48, 48))
        self.imgOnda = pygame.image.load("./Modulo/Repositorio-Imagens/onda.png")
        self.imgOndaFormat = pygame.transform.scale(self.imgOnda, (48, 48))

        self.sprites = []
        self.sprites.append(self.imgOceanoFormat)
        self.sprites.append(self.imgOndaFormat)

        self.spriteAtual = 0
        self.image = self.sprites[self.spriteAtual]
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

        self.matrizTabuleiro = []

    def desenhaTabuleiro(self, tela, linha=8, coluna=8):

        for l in range(0, linha):
            linhaTabuleiro = []
            for c in range(0, coluna):
                linhaTabuleiro.append(self.image)
            self.matrizTabuleiro.append(linhaTabuleiro)

        y = self.pos_y
        for l in range(0, linha):
            x = self.pos_x
            for c in range(0, coluna):
                tela.blit(self.matrizTabuleiro[l][c], (x, y))
                x += 50
            y += 50

        indiceAlfabetico, indiceNumerico = self.criaIndices()
        if self.pos_x == 50:
            # loop para posicionamento dos índices alfabeticos(colunas) do lado 1
            y = 0
            for l in range(0, linha):
                x = 50
                for c in range(0, coluna):
                    tela.blit(indiceAlfabetico[c], (x, y))
                    x += 50
            # loop para posicionamento dos índices numéricos(linhas) do lado 1
            y = 50
            for l in range(0, linha):
                x = 0
                for c in range(0, coluna):
                    tela.blit(indiceNumerico[l], (x, y))
                y += 50
        else:
            # loop para posicionamento dos índices alfabeticos(colunas) do lado 2
            y = 0
            for l in range(0, linha):
                x = 610
                for c in range(0, coluna):
                    tela.blit(indiceAlfabetico[c], (x, y))
                    x += 50
            # loop para posicionamento dos índices numéricos(linhas) do lado 2
            y = 50
            for l in range(0, linha):
                x = 1010
                for c in range(0, coluna):
                    tela.blit(indiceNumerico[l], (x, y))
                y += 50



    def criaIndices(self):
        # loop para load, redimensionamento e adição de imagens dos índices alfabeticos(colunas) em lista
        indiceAlfabetico = []
        base = 65
        for cont in range(0, 8):
            atual = base + cont
            img = pygame.image.load(f"./Modulo/Repositorio-Imagens/Img{atual}.jpg")
            imgIndice = pygame.transform.scale(img, (48, 48))
            indiceAlfabetico.append(imgIndice)

        # loop para load, redimensionamento e adição de imagens dos índices numericos(linhas) em lista
        indiceNumerico = []
        base = 1
        for cont in range(0, 8):
            atual = base + cont
            img = pygame.image.load(f"./Modulo/Repositorio-Imagens/Img{atual}.jpg")
            imgIndice = pygame.transform.scale(img, (48, 48))
            indiceNumerico.append(imgIndice)

        return indiceAlfabetico, indiceNumerico

    def avaliaCliqueTabuleiro(self):

        mouse = pygame.mouse.get_pos()
        y = self.pos_y
        for l in range(0, 8):
            x = self.pos_x
            for c in range(0, 8):
                if cliqueEsquerdo() and self.matrizTabuleiro[l][c].get_rect(topleft=(x, y)).collidepoint(mouse):
                    #Implementar lógica para mudança no tabuleiro
                    print("clique funcionando")
                x += 50
            y += 50