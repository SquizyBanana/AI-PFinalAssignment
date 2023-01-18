import random as rnd
from helpers.cards import Cards

class Player:

    def __init__(self, name, mark, cards):
        self.name = name
        self.mark = mark
        self.hand = []
        self.cards = cards

    def do_move(self, board):
        """
        int(input("Where do you want to place your move"))
        """
        rnd.seed()
        return int(rnd.random() * 9)

    def set_result(self):
        pass

    def get_name(self):
        return self.name

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark

    def set_move(self, move):
        pass

    def other_mark(self, mark):
        if mark == "X":
            return "O"
        else:
            return "X"

    def drawCard(self):
        self.hand.append(self.cards.drawCard())
