from player import Player


class HumanPlayer(Player):

    def __init__(self, name, mark, cards):
        Player.__init__(self, name, mark, cards)
        for i in range(6):
            self.drawCard()
        self.next_move = 100
        '''super.name = name
        super.mark = mark'''

    def do_move(self, board):
        print(board.get_possible_moves(self.hand, self.cards))
        return self.next_move

    def set_move(self, move, cards):
        self.drawCard()
        self.hand.remove(cards.card_list[move])
        self.next_move = move