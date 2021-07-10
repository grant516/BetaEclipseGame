from data.point import Point
from data import constants

#I'm adding the code below on my own
import random

import arcade

class Enemy(arcade.Sprite):
    """TODO: Implement the Enemy class. It should inherit from Sprite and
    provide two methods in addition to init: bounce_horizontal and
    bounce_vertical. It should also have a center x & y,
    and a change x & y."""
    def __init__(self):
        super().__init__(constants.ENEMY_IMAGE)

        #Below is their original spot on the board
        #self.center_x = random.randrange(constants.SCREEN_WIDTH)
#
        #self.center_y = random.randrange(constants.SCREEN_HEIGHT)

        self.center_x = random.randrange(constants.MAP_WIDTH)

        self.center_y = random.randrange(constants.MAP_HEIGHT)

        #This is where they are
        direction_list = [-constants.ENEMY_SPEED,constants.ENEMY_SPEED]
        self.change_x = 0 #random.choice(direction_list)
        self.change_y = 0 #random.choice(direction_list)

        self._health = 5

    def get_health(self):
        return(self._health)

    def sub_health(self):
        self._health -= 1

    def change_x_neg(self):
        self.change_x = -constants.ENEMY_SPEED

    def change_y_neg(self):
        self.change_y = -constants.ENEMY_SPEED

    def change_x_pos(self):
        self.change_x = constants.ENEMY_SPEED

    def change_y_pos(self):
        self.change_y = constants.ENEMY_SPEED