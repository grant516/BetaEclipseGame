from data.point import Point
from data import constants

#I'm adding the code below on my own
import random

import arcade

class Balls(arcade.Sprite):
    """TODO: Implement the Ball class. It should inherit from Sprite and 
    provide two methods in addition to init: bounce_horizontal and 
    bounce_vertical. It should also have a center x & y, 
    and a change x & y."""
    def __init__(self):
        super().__init__(constants.BALL_IMAGE)

        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.BALL_Y)

        #Grant code
        direction_list = [-constants.BALL_SPEED,constants.BALL_SPEED]
        self.change_x = random.choice(direction_list)
        self.change_y = random.choice(direction_list)

    def bounce_horizontal(self):
        if(self.change_y < 0):
            self.change_y = constants.BALL_SPEED
        elif(self.change_y > 0):
            self.change_y = -constants.BALL_SPEED


    def bounce_vertical(self):
        if(self.change_x < 0):
            self.change_x = constants.BALL_SPEED
        elif(self.change_x > 0):
            self.change_x = -constants.BALL_SPEED