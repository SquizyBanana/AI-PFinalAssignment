# this class loads all the images before use
import pygame
from numpy import *
import random
from helpers.image import Image
class Cards:

    def __init__(self):
        self.card_stack = []
        self.card_list = []
        self.loadCards()
        self.addCards()  # Create the board
        self.sizeCards()
        self.createStack()  # Create the stack of cards to draw from

    def createStack(self):
        self.card_stack = self.card_list.copy()
        del self.card_stack[99]    # remove corner cards from the stack
        del self.card_stack[90]
        del self.card_stack[9]
        del self.card_stack[0]
        random.shuffle(self.card_stack)

    def drawCard(self):
        return self.card_stack.pop(0)

    def sizeCards(self):
        for image in self.card_list:
            image = pygame.transform.rotozoom(image.image,0,0.5)
    def loadCards(self): #hardcoded instead of proceduraly because with proceduraly, no names could be given to the images.
        self.Corner = Image("Corner")

        self.H2 = Image("H2")
        self.H3 = Image("H3")
        self.H4 = Image("H4")
        self.H5 = Image("H5")
        self.H6 = Image("H6")
        self.H7 = Image("H7")
        self.H8 = Image("H8")
        self.H9 = Image("H9")
        self.H10 = Image("H10")
        self.HA = Image("HA")
        self.HJ = Image("HJ")
        self.HQ = Image("HQ")
        self.HK = Image("HK")

        self.K2 = Image("K2")
        self.K3 = Image("K3")
        self.K4 = Image("K4")
        self.K5 = Image("K5")
        self.K6 = Image("K6")
        self.K7 = Image("K7")
        self.K8 = Image("K8")
        self.K9 = Image("K9")
        self.K10 = Image("K10")
        self.KA = Image("KA")
        self.KJ = Image("KJ")
        self.KQ = Image("KQ")
        self.KK = Image("KK")

        self.R2 = Image("R2")
        self.R3 = Image("R3")
        self.R4 = Image("R4")
        self.R5 = Image("R5")
        self.R6 = Image("R6")
        self.R7 = Image("R7")
        self.R8 = Image("R8")
        self.R9 = Image("R9")
        self.R10 = Image("R10")
        self.RA = Image("RA")
        self.RJ = Image("RJ")
        self.RQ = Image("RQ")
        self.RK = Image("RK")

        self.S2 = Image("S2")
        self.S3 = Image("S3")
        self.S4 = Image("S4")
        self.S5 = Image("S5")
        self.S6 = Image("S6")
        self.S7 = Image("S7")
        self.S8 = Image("S8")
        self.S9 = Image("S9")
        self.S10 = Image("S10")
        self.SA = Image("SA")
        self.SJ = Image("SJ")
        self.SQ = Image("SQ")
        self.SK = Image("SK")

    def addCards(self):
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

