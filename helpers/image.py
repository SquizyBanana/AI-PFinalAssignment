import pygame

class Image:

    def __init__(self,string):
        self.image = pygame.image.load("helpers/Cards/" + string + ".png").convert()