import pygame

PosSubmarino = 1
QuantSubmarino = 3

ImgSubmarino = pygame.image.load("./Repositorio-Imagens/submarino.png")
TabuleiroImgSubmarino = pygame.transform.scale(ImgSubmarino, (30,30))

def Submarino ():
    print(f"Navegação de ocupação de {PosSubmarino} casa, podendo posicionar até {QuantSubmarino} no tabuleiro.")
    return TabuleiroImgSubmarino