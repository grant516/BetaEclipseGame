from data.point import Point
from data import constants
from data.health import SpriteWithHealth

import arcade

class Player(arcade.Sprite):
    def __init__(self, image, scale, health_y_position, text_y_position, text_x_position, health_width, height, max_health):
        super().__init__(constants.PLAYER_IMAGE, image, scale, health_y_position,
                         text_y_position, text_x_position, health_width, height, max_health)

        #self.center_x = int(constants.MAX_X / 2)
        #self.center_y = int(constants.PLAYER_Y)

        self.center_x = 128
        self.center_y = 128
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
