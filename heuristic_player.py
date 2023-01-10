from player import Player
from board import Board

class HeuristicPlayer(Player):

    def __init__(self, name, mark):
        Player.__init__(self, name, mark)
        self.saved_boards = {}
        self.check_counter = 0
        self.calculate_counter = 0
        self.heuristics_counter = 0


    def do_move(self, board):
        return self.calculate_next_move(board, self.mark)

    def calculate_next_move(self, current_board, mark):

        # for every possible move, add a pair of a min_max score and the move to a list scores.
        score_move_pairs = []
        self.depth = 0
        for next_move in current_board.get_possible_moves():
            next_score = self.min_max(current_board, next_move, mark)
            score_move_pairs.append((next_score, next_move))
        # if there is no score/move pair, return 0

        if not score_move_pairs:
            return 0
        # otherwise
        else:
            # compute the max score/move
            highest_score, best_move = max(score_move_pairs)
            print("calculate" + str(self.calculate_counter))
            print("check" + str(self.check_counter))
            print("heuristics" + str(self.heuristics_counter))
            # return the move
            return best_move

    def min_max(self, current_board, move, mark):
        next_board = current_board.deep_copy()
        next_board.place_move(move, mark)
        check = tuple(next_board.board)
        # if check in self.saved_boards:
        #     self.check_counter += 1
        #     return self.saved_boards.get(check)
        if next_board.check_win(mark):
            return 10
        elif next_board.board_full():
            return 0
        else:
            self.depth += 1
            if self.depth > 5:
                self.heuristics_counter += 1
                return self.calculate_heuristics(next_board,mark)
            scores = []
            for moves in next_board.get_possible_moves():
                self.calculate_counter += 1
                scores.append(self.max_min(next_board, moves, self.other_mark(mark)))
            self.next_score = min(scores)
            # self.saved_boards.update({tuple(next_board.board): self.next_score})
        return self.next_score

    def max_min(self, current_board, move, mark):
        next_board = current_board.deep_copy()
        next_board.place_move(move, mark)
        # check = tuple(next_board.board)
        # if check in self.saved_boards:
        #     self.check_counter += 1
        #     return self.saved_boards.get(check)
        if next_board.check_win(mark):
            return -10
        elif next_board.board_full():
            return 0
        else:
            self.depth += 1
            if self.depth > 5:
                self.heuristics_counter += 1
                return self.calculate_heuristics(next_board,mark)
            scores = []
            for moves in next_board.get_possible_moves():
                self.calculate_counter += 1
                scores.append(self.min_max(next_board, moves, self.other_mark(mark)))
            self.next_score = max(scores)
            # self.saved_boards.update({tuple(next_board.board) : self.next_score })
        return self.next_score


    def calculate_heuristics(self, next_board, mark):
        heuristic_score = 0
        heuristic_score += self.check_row(next_board, [0, 1, 2], mark) # top row
        heuristic_score += self.check_row(next_board, [3, 4, 5], mark) # middle row
        heuristic_score += self.check_row(next_board, [6, 7, 8], mark) # bottom row
        heuristic_score += self.check_row(next_board, [0, 3, 6], mark) # left colum
        heuristic_score += self.check_row(next_board, [1, 4, 7], mark) # middle colum
        heuristic_score += self.check_row(next_board, [2, 5, 8], mark) # right colum
        heuristic_score += self.check_row(next_board, [0, 4, 8], mark) # diagonal top left to bottom right
        heuristic_score += self.check_row(next_board, [2, 4, 6], mark) # diagonal top right to bottom left
        return heuristic_score

    def check_row(self, board,check_rows, mark):
        check_array = []
        check_array.append(board.board[check_rows[0]])
        check_array.append(board.board[check_rows[1]])
        check_array.append(board.board[check_rows[2]])
        max_score = check_array.count(mark)
        min_score = check_array.count(self.other_mark(mark))
        if max_score == 2 and min_score == 0:
            return 3
        elif max_score == 1 and min_score == 0:
            return 1
        elif max_score == 0 and min_score == 1:
            return -1
        elif max_score == 0 and min_score == 2:
            return -3
        else:
            return 0
