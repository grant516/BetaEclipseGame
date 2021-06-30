from data.point import Point
from data import constants

import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.PLAYER_IMAGE)

        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.PLAYER_Y)

        self._health = 100
        self._game_over = False
        self._attack = False

    def get_health(self):
        return(self._health)

    def sub_health(self):
        self._health -= 1

    def get_game_over(self):
        return(self._game_over)

    def set_game_over(self):
        self._game_over = True

    def get_attack(self):
        return(self._attack)

    def set_attack(self, state):
        self._attack = state