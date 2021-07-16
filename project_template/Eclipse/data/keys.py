from data.point import Point
from data import constants

#I'm adding the code below on my own
import random

import arcade

class Keys(arcade.Sprite):
    """TODO: Implement the Enemy class. It should inherit from Sprite and
    provide two methods in addition to init: bounce_horizontal and
    bounce_vertical. It should also have a center x & y,
    and a change x & y."""
    def __init__(self):
        super().__init__(constants.KEY_IMAGE)

        #Below is their original spot on the board
        #self.center_x = random.randrange(constants.SCREEN_WIDTH)
#
        #self.center_y = random.randrange(constants.SCREEN_HEIGHT)
        self.center_x = random.randrange(constants.MAP_WIDTH)

        self.center_y = random.randrange(constants.MAP_HEIGHT)
