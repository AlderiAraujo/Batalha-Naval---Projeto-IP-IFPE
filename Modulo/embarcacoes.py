import pygame

class Embarcacao:

    def __init__(self, nome, imagem):

        self.nome = nome
        self.imagem = imagem

        if self.nome == "submarino":
            self.pontuacao = 1

        elif self.nome == "portaAvioes":
            self.pontuacao = 2

        elif self.nome == "cruzador":
            self.pontuacao = 4


        #ImgSubmarino = pygame.image.load("./Repositorio-Imagens/submarino.png")
        #TabuleiroImgSubmarino = pygame.transform.scale(ImgSubmarino, (30,30))



