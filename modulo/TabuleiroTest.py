import pygame
import random

class Tabuleiro(pygame.sprite.Sprite):
    def __init__(self, tela, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.imgOceano = pygame.image.load("./modulo/Repositorio-Imagens/oceano.jpg")
        self.imgOceanoFormat = pygame.transform.scale(self.imgOceano, (48, 48))
        self.imgOnda = pygame.image.load("./modulo/Repositorio-Imagens/onda.png")
        self.imgOndaFormat = pygame.transform.scale(self.imgOnda, (48, 48))

        self.sprites = []
        self.sprites.append(self.imgOceanoFormat)
        self.sprites.append(self.imgOndaFormat)

        self.spriteAtual = 0
        self.image = self.sprites[self.spriteAtual]
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

        self.matrizFundo = []
        self.matrizTabuleiro = []
        self.linhaTabuleiro = []
        self.desenhaTabuleiro(tela)
        #self.desenhaMatrizJogavel(tela)
        self.adicionaEmbarcacao(9)

    def desenhaMatrizJogavel(self, tela, linha=8, coluna=8):

        self.matrizTabuleiro = []
        for l in range(0, linha):
            self.linhaTabuleiro = []
            for c in range(0, coluna):
                self.linhaTabuleiro.append(0)
            self.matrizTabuleiro.append(self.linhaTabuleiro)


        y = self.pos_y
        for l in range(0, linha):
            x = self.pos_x
            for c in range(0, coluna):
                if self.matrizTabuleiro[l][c] == 0:
                    tela.blit(self.matrizTabuleiro[l][c], (x, y))
                x += 50
            y += 50

    def desenhaTabuleiro(self, tela, linha=8, coluna=8):

        self.matrizFundo = []
        for l in range(0, linha):
            linhaTabuleiro = []
            for c in range(0, coluna):
                linhaTabuleiro.append(self.imgOceanoFormat)
            self.matrizFundo.append(linhaTabuleiro)

        y = self.pos_y
        for l in range(0, linha):
            x = self.pos_x
            for c in range(0, coluna):
                tela.blit(self.matrizFundo[l][c], (x, y))
                x += 50
            y += 50
        pygame.display.update()
        indiceAlfabetico, indiceNumerico = self.criaIndices()
        if self.pos_x == 50:
            #loop para posicionamento dos índices alfabeticos (colunas) do lado 1
            y = 0
            for l in range(0, linha):
                x = 50
                for c in range(0, coluna):
                    tela.blit(indiceAlfabetico[c], (x, y))
                    x += 50
            #loop para posicionamento dos índices numéricos (linhas) do lado 1
            y = 50
            for l in range(0, linha):
                x = 0
                for c in range(0, coluna):
                    tela.blit(indiceNumerico[l], (x, y))
                y += 50
        else:
            #loop para posicionamento dos índices alfabeticos (colunas) do lado 2
            y = 0
            for l in range(0, linha):
                x = 610
                for c in range(0, coluna):
                    tela.blit(indiceAlfabetico[c], (x, y))
                    x += 50
            #loop para posicionamento dos índices numéricos (linhas) do lado 2
            y = 50
            for l in range(0, linha):
                x = 1010
                for c in range(0, coluna):
                    tela.blit(indiceNumerico[l], (x, y))
                y += 50



    def criaIndices(self):
        #loop para load, redimensionamento e adição de imagens dos índices alfabeticos (colunas) em lista
        indiceAlfabetico = []
        base = 65
        for cont in range(0, 8):
            atual = base + cont
            img = pygame.image.load(f"./modulo/Repositorio-Imagens/Img{atual}.jpg")
            imgIndice = pygame.transform.scale(img, (48, 48))
            indiceAlfabetico.append(imgIndice)

        #loop para load, redimensionamento e adição de imagens dos índices numericos (linhas) em lista
        indiceNumerico = []
        base = 1
        for cont in range(0, 8):
            atual = base + cont
            img = pygame.image.load(f"./modulo/Repositorio-Imagens/Img{atual}.jpg")
            imgIndice = pygame.transform.scale(img, (48, 48))
            indiceNumerico.append(imgIndice)

        return indiceAlfabetico, indiceNumerico

    def sorteia(self, quantidade):

        self.tuplas_sorteadas = []
        for i in range(0, quantidade):
            tupla = ()
            lista = [0, 1, 2, 3, 4, 5, 6, 7]
            pos_sorteada = []

            for i in range(0, 2):
                pos_sorteada.append(random.choice(range(0, len(lista))))
            tupla = tuple(pos_sorteada)
            if tupla not in self.tuplas_sorteadas:
                self.tuplas_sorteadas.append(tupla)
            else:
                continue

        return self.tuplas_sorteadas

    def adicionaEmbarcacao(self, quantidade):
        listaDeTuplas = self.sorteia(quantidade)

        for i in range(0, quantidade):
            try:
                if quantidade > 4 :
                    imgSubmarino = pygame.image.load("./modulo/Repositorio-Imagens/submarino.png")
                    imgSubmarinoFormat = pygame.transform.scale(imgSubmarino, (48, 48))

                    tupla1 = listaDeTuplas[0]
                    tupla2 = listaDeTuplas[1]
                    tupla3 = listaDeTuplas[2]
                    tupla4 = listaDeTuplas[3]
                    tupla5 = listaDeTuplas[4]

                    l0, c0 = tupla1
                    l1, c1 = tupla2
                    l2, c2 = tupla3
                    l3, c3 = tupla4
                    l4, c4 = tupla5

                    self.matrizFundo[l0][c0] = imgSubmarinoFormat
                    self.matrizFundo[l1][c1] = imgSubmarinoFormat
                    self.matrizFundo[l2][c2] = imgSubmarinoFormat
                    self.matrizFundo[l3][c3] = imgSubmarinoFormat
                    self.matrizFundo[l4][c4] = imgSubmarinoFormat
                    quantidade-=1

                elif quantidade > 1:
                    imgCruzador = pygame.image.load("./modulo/Repositorio-Imagens/cruzador.png")
                    imgCruzadorFormat = pygame.transform.scale(imgCruzador, (48, 48))
                    tupla6 = listaDeTuplas[5]
                    tupla7 = listaDeTuplas[6]
                    tupla8 = listaDeTuplas[7]

                    l5, c5 = tupla6
                    l6, c6 = tupla7
                    l7, c7 = tupla8

                    self.matrizFundo[l5][c7] = imgCruzadorFormat
                    self.matrizFundo[l6][c6] = imgCruzadorFormat
                    self.matrizFundo[l7][c5] = imgCruzadorFormat
                    quantidade-=1

                elif quantidade == 1:
                    imgPortaAvioes = pygame.image.load("./modulo/Repositorio-Imagens/portaAvioes.png")
                    imgPortaAvioesFormat = pygame.transform.scale(imgPortaAvioes, (48, 48))
                    tupla9 = listaDeTuplas[8]
                    linha, coluna = tupla9
                    self.matrizFundo[linha][coluna] = imgPortaAvioesFormat
                    break
            except IndexError:
                continue





    def exibe(self, tela):
        y = self.pos_y
        for l in range(0, 8):
            x = self.pos_x
            for c in range(0, 8):
                tela.blit(self.matrizFundo[l][c], (x, y))
                x += 50
            y += 50


    def avaliaCliqueTabuleiro(self, pos_x, pos_y, tela=None):
        mouse = pygame.mouse.get_pos()
        self.pos_clicada = ()
        self.pos_tela = ()
        y = pos_y
        for l in range(0, 8):
            x = pos_x
            for c in range(0, 8):
                if mouse[0] and self.matrizFundo[l][c].get_rect(topleft=(x, y)).collidepoint(mouse):
                    if self.matrizFundo[l][c] == self.imgOceanoFormat:
                        print("errou")
                        erro = pygame.image.load("./modulo/Repositorio-Imagens/x.png")
                        erroImg = pygame.transform.scale(erro, (48, 48))
                        self.matrizFundo[l][c] = erroImg
                        tela.blit(self.matrizFundo[l][c], (x, y))
                    else:
                        print("acertou")
                        tela.blit(self.matrizFundo[l][c], (x, y))
                    self.pos_clicada = (l, c)
                    self.pos_tela = (x, y)
                    return self.pos_clicada, self.pos_tela
                x += 50
            y += 50