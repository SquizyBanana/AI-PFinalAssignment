import math
import copy
from helpers.cards import Cards
class Board:

    def __init__(self):
        self.cards = Cards()
        self.board = [" "] * 100
        self.board[0] = "C"     # see if this can be done cleaner
        self.board[9] = "C"
        self.board[90] = "C"
        self.board[99] = "C"
        self.row_length = int(math.sqrt(len(self.board)))

    def move_is_legal(self, move):
        return self.check_move_in_board(move) and self.board[move] == " "

    def place_move(self, move, mark):
        self.board[move] = mark

    def check_win(self, marks):
        win = False
        # check for all marks if there is a 5 in a row in a diagnol, row, or column
        for mark in marks:
            win = self.winDiagnol(mark) or self.win_row(mark) or self.win_column(mark)
            if win:
                return win

            '''
            if win:
                print(str(self.winDiagnol(mark)) + " " + str(self.winRow(mark)) + " " + str(
                    self.winColumn(mark)))
                print("Player " + mark + " is the winner!")
            '''
        return win

    def check_move_in_board(self, move):
        try:
            move = int(move)
            if not (-1 < move < 100):
                raise ValueError
        except:
            return False
        return True

    def winDiagnol(self, mark):
        for j in range(0,6):
            for k in range(0,6):
                diagnol_Right = True
                for i in range(0, 5):
                    if self.board[j + k * self.row_length + i + i * self.row_length ] != mark and not ((j ==0 and k == 0 and i == 0) or (j == 5 and k == 5 and i == 4)):
                        diagnol_Right = False
                        break
                if diagnol_Right:
                    return diagnol_Right
        for l in range(4, 10):
            for m in range(0, 6):
                diagnol_Left = True
                for n in range(0, 5):
                    if self.board[l + m * self.row_length -n + n * self.row_length] != mark and not ((l == 9 and m == 0 and n == 0) or (l == 4 and m ==5 and n == 4)):
                        diagnol_Left = False
                        break
                if diagnol_Left:
                    return diagnol_Left

    def win_row(self, mark):
        for i in range(0, self.row_length):
            for k in range(0, 6):
                win = True
                for j in range(0, 5):
                    if self.board[k + j + (i * self.row_length)] != mark and not ((i == 0 and k == 0 and j == 0) or (i == 0 and k == 5 and j == 4) or (i == 9 and k == 0 and j == 0) or (i == 9 and k == 5 and j == 4)) :
                        win = False
                        break
                if win:
                    return win
        return win

    def win_column(self, mark):
        for i in range(0, self.row_length):

            for k in range(0, 6):
                win = True
                for j in range(0, 5):
                    if self.board[i + (k * self.row_length) +(j * self.row_length)] != mark and not ((i == 0 and k == 0 and j == 0) or (i == 0 and k == 5 and j == 4) or (i == 9 and k == 0 and j == 0) or (i == 9 and k == 5 and j == 4)):
                        win = False
                        break
                if win:
                    return win
        return win

    def board_full(self):
        # if not (" " in self.board):
        #     print("Board is full")
        return not (" " in self.board)

    def get_board(self):
        return self.board

    def get_possible_moves(self):
        moves = []
        for i in range(len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def create_board(self):
        self.board = [" "] * 100

    def board_to_string(self):
        field = self.get_board()
        print("\n---------------------------")
        for i in range(len(field)):
            if i % 10 == 0:
                print(" ")
            print("|" + field[i] + "|", end='')

    def deep_copy(self):
        return copy.deepcopy(self)
