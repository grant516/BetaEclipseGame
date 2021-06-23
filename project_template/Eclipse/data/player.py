from data.point import Point
from data import constants

import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.PLAYER_IMAGE)

        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.PLAYER_Y)