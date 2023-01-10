from player import Player


class HumanPlayer(Player):

    def __init__(self, name, mark):
        Player.__init__(self, name, mark)
        self.next_move = 100
        '''super.name = name
        super.mark = mark'''

    def do_move(self, board):
        return self.next_move

    def set_move(self, move):
        self.next_move = move
