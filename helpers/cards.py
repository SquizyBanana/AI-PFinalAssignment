# this class loads all the images before use
import pygame
import os

class Cards:

    def __int__(self):
        pass

    def loadCards(self): #hardcoded instead of proceduraly because with proceduraly, no names could be given to the images.
        self.Corner = pygame.image.load("helpers/Cards/Corner.png").convert()

        self.H2 = pygame.image.load("helpers/Cards/H2.png").convert()
        self.H3 = pygame.image.load("helpers/Cards/H3.png").convert()
        self.H4 = pygame.image.load("helpers/Cards/H4.png").convert()
        self.H5 = pygame.image.load("helpers/Cards/H5.png").convert()
        self.H6 = pygame.image.load("helpers/Cards/H6.png").convert()
        self.H7 = pygame.image.load("helpers/Cards/H7.png").convert()
        self.H8 = pygame.image.load("helpers/Cards/H8.png").convert()
        self.H9 = pygame.image.load("helpers/Cards/H9.png").convert()
        self.H10 = pygame.image.load("helpers/Cards/H10.png").convert()
        self.HA = pygame.image.load("helpers/Cards/HA.png").convert()
        self.HJ = pygame.image.load("helpers/Cards/HJ.png").convert()
        self.HQ = pygame.image.load("helpers/Cards/HQ.png").convert()
        self.HK = pygame.image.load("helpers/Cards/HK.png").convert()

        self.K2 = pygame.image.load("helpers/Cards/K2.png").convert()
        self.K3 = pygame.image.load("helpers/Cards/K3.png").convert()
        self.K4 = pygame.image.load("helpers/Cards/K4.png").convert()
        self.K5 = pygame.image.load("helpers/Cards/K5.png").convert()
        self.K6 = pygame.image.load("helpers/Cards/K6.png").convert()
        self.K7 = pygame.image.load("helpers/Cards/K7.png").convert()
        self.K8 = pygame.image.load("helpers/Cards/K8.png").convert()
        self.K9 = pygame.image.load("helpers/Cards/K9.png").convert()
        self.K10 = pygame.image.load("helpers/Cards/K10.png").convert()
        self.KA = pygame.image.load("helpers/Cards/KA.png").convert()
        self.KJ = pygame.image.load("helpers/Cards/KJ.png").convert()
        self.KQ = pygame.image.load("helpers/Cards/KQ.png").convert()
        self.KK = pygame.image.load("helpers/Cards/KK.png").convert()

        self.R2 = pygame.image.load("helpers/Cards/R2.png").convert()
        self.R3 = pygame.image.load("helpers/Cards/R3.png").convert()
        self.R4 = pygame.image.load("helpers/Cards/R4.png").convert()
        self.R5 = pygame.image.load("helpers/Cards/R5.png").convert()
        self.R6 = pygame.image.load("helpers/Cards/R6.png").convert()
        self.R7 = pygame.image.load("helpers/Cards/R7.png").convert()
        self.R8 = pygame.image.load("helpers/Cards/R8.png").convert()
        self.R9 = pygame.image.load("helpers/Cards/R9.png").convert()
        self.R10 = pygame.image.load("helpers/Cards/R10.png").convert()
        self.RA = pygame.image.load("helpers/Cards/RA.png").convert()
        self.RJ = pygame.image.load("helpers/Cards/RJ.png").convert()
        self.RQ = pygame.image.load("helpers/Cards/RQ.png").convert()
        self.RK = pygame.image.load("helpers/Cards/RK.png").convert()

        self.S2 = pygame.image.load("helpers/Cards/S2.png").convert()
        self.S3 = pygame.image.load("helpers/Cards/S3.png").convert()
        self.S4 = pygame.image.load("helpers/Cards/S4.png").convert()
        self.S5 = pygame.image.load("helpers/Cards/S5.png").convert()
        self.S6 = pygame.image.load("helpers/Cards/S6.png").convert()
        self.S7 = pygame.image.load("helpers/Cards/S7.png").convert()
        self.S8 = pygame.image.load("helpers/Cards/S8.png").convert()
        self.S9 = pygame.image.load("helpers/Cards/S9.png").convert()
        self.S10 = pygame.image.load("helpers/Cards/S10.png").convert()
        self.SA = pygame.image.load("helpers/Cards/SA.png").convert()
        self.SJ = pygame.image.load("helpers/Cards/SJ.png").convert()
        self.SQ = pygame.image.load("helpers/Cards/SQ.png").convert()
        self.SK = pygame.image.load("helpers/Cards/SK.png").convert()

    def addCards(self):
        self.card_list = []

        self.card_list.append(self.Corner)
        self.card_list.append(self.S2)
        self.card_list.append(self.S3)
        self.card_list.append(self.S4)
        self.card_list.append(self.S5)
        self.card_list.append(self.S6)
        self.card_list.append(self.S7)
        self.card_list.append(self.S8)
        self.card_list.append(self.S9)
        self.card_list.append(self.Corner)

        self.card_list.append(self.K6)
        self.card_list.append(self.K5)
        self.card_list.append(self.K4)
        self.card_list.append(self.K3)
        self.card_list.append(self.K2)
        self.card_list.append(self.HA)
        self.card_list.append(self.HK)
        self.card_list.append(self.HQ)
        self.card_list.append(self.H10)
        self.card_list.append(self.S10)

        self.card_list.append(self.K7)
        self.card_list.append(self.SA)
        self.card_list.append(self.R2)
        self.card_list.append(self.R3)
        self.card_list.append(self.R4)
        self.card_list.append(self.R5)
        self.card_list.append(self.R6)
        self.card_list.append(self.R7)
        self.card_list.append(self.H9)
        self.card_list.append(self.SQ)

        self.card_list.append(self.K8)
        self.card_list.append(self.SK)
        self.card_list.append(self.K6)
        self.card_list.append(self.K5)
        self.card_list.append(self.K4)
        self.card_list.append(self.K3)
        self.card_list.append(self.K2)
        self.card_list.append(self.R8)
        self.card_list.append(self.H8)
        self.card_list.append(self.SK)

        self.card_list.append(self.K9)
        self.card_list.append(self.SQ)
        self.card_list.append(self.K7)
        self.card_list.append(self.H6)
        self.card_list.append(self.H5)
        self.card_list.append(self.H4)
        self.card_list.append(self.HA)
        self.card_list.append(self.R9)
        self.card_list.append(self.H7)
        self.card_list.append(self.SA)

        self.card_list.append(self.K10)
        self.card_list.append(self.S10)
        self.card_list.append(self.K8)
        self.card_list.append(self.H7)
        self.card_list.append(self.H2)
        self.card_list.append(self.H3)
        self.card_list.append(self.HK)
        self.card_list.append(self.R10)
        self.card_list.append(self.H6)
        self.card_list.append(self.R2)

        self.card_list.append(self.KQ)
        self.card_list.append(self.S9)
        self.card_list.append(self.K9)
        self.card_list.append(self.H8)
        self.card_list.append(self.H9)
        self.card_list.append(self.H10)
        self.card_list.append(self.HQ)
        self.card_list.append(self.RQ)
        self.card_list.append(self.H5)
        self.card_list.append(self.R3)

        self.card_list.append(self.KK)
        self.card_list.append(self.S8)
        self.card_list.append(self.K10)
        self.card_list.append(self.KQ)
        self.card_list.append(self.KK)
        self.card_list.append(self.KA)
        self.card_list.append(self.RA)
        self.card_list.append(self.RK)
        self.card_list.append(self.H4)
        self.card_list.append(self.R4)

        self.card_list.append(self.KA)
        self.card_list.append(self.S7)
        self.card_list.append(self.S6)
        self.card_list.append(self.S5)
        self.card_list.append(self.S4)
        self.card_list.append(self.S3)
        self.card_list.append(self.S2)
        self.card_list.append(self.H2)
        self.card_list.append(self.H3)
        self.card_list.append(self.R5)

        self.card_list.append(self.Corner)
        self.card_list.append(self.RA)
        self.card_list.append(self.RK)
        self.card_list.append(self.RQ)
        self.card_list.append(self.R10)
        self.card_list.append(self.R9)
        self.card_list.append(self.R8)
        self.card_list.append(self.R7)
        self.card_list.append(self.R6)
        self.card_list.append(self.Corner)
    def sizeCards(self):
        for image in self.card_list:
            image = pygame.transform.rotozoom(image,0,0.5)
            print(image)