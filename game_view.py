from pygame import draw

import human_player
from sequence import Sequence
from helpers.cards import Cards


class GameView:

    def __init__(self, game, screen, font, cards, human):
        self.human_player = human
        self.game = game
        self.screen = screen
        screen_size = self.screen.get_size()
        self.offset = [100, 150]
        grid_x = (screen_size[0]-self.offset[0]*2)/10
        grid_y = (screen_size[1]-self.offset[0]*2)/10    #Based on offset for x position to keep a square board
        self.grid_size = [grid_x, grid_y]
        self.font = font
        self.line_width = 10
        self.cards = cards


    def draw_game(self):
        self.draw_board()
        self.draw_status_text()
        self.draw_hand()

    def resize(self):
        pass

    def draw_board(self):
        for i, mark in enumerate(self.game.get_board()):
            x = int(i % 10) * self.grid_size[0] + self.offset[0]
            y = int(i / 10) * self.grid_size[1] + self.offset[1]
            draw.rect(self.screen, (0, 0, 0), ((x, y), self.grid_size), int(self.line_width/5))
            self.screen.blit(self.cards.card_list[i].image, (x,y))

            self.draw_mark(x, y, self.grid_size, mark)


    def draw_mark(self, x, y, size, mark):
        radius = int(size[0] / 2)

        if mark == "X":
            color = (255, 0, 0)
            draw.circle(self.screen, color, [int(x+radius), int(y+radius)], radius)

        if mark == "O":
            color = (0, 0, 255)
            draw.circle(self.screen, color, [int(x+radius), int(y+radius)], radius)

    def draw_status_text(self):
        text = self.font.render(self.game.players[self.game.current_player].mark + "'s turn", True, (0, 0, 0))
        self.screen.blit(text, (self.offset[0], self.offset[1]/5))

    def draw_text(self):
        pass

    def on_mouse_clicked(self, pos):
        x_new = int((pos[0]-self.offset[0])/self.grid_size[0])
        y_new = int((pos[1]-self.offset[1])/self.grid_size[1])
        if -1 < x_new < self.game.row_length():
            if -1 < y_new < self.game.row_length():
                board = self.game.get_board()
                if (x_new + 10 * y_new) in [i for i, x in enumerate(self.cards.card_list) if x in self.human_player.hand] and board[x_new + 10 * y_new]  == " ":
                    self.game.players[self.game.current_player].set_move((x_new + 10 * y_new), self.cards)

    def draw_hand(self):
        for i in range(len(self.human_player.hand)):
            self.screen.blit(self.human_player.hand[i].image, (0,50*i))