import os

RANGE = 10
TRACKING = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAX_X = 800
MAX_Y = 600
NUM_ENEMY = 5

ENEMY_SPEED = 3
ENEMY_Y = MAX_Y / 2

PLAYER_Y = 25

PLAYER_MOVE_SCALE = 4

BRICK_WIDTH = 25
BRICK_HEIGHT = 15
BRICK_SPACE = 10

ENEMY_CAN_DIE = False

"""BALL_IMAGE = "images/goomba.png"
PADDLE_IMAGE = "images/paddle-0.png"
BRICK_IMAGE = "images/brick-0.png"""


PATH = os.path.dirname(os.path.abspath(__file__))
ENEMY_IMAGE = os.path.join(PATH, "..", "assets/goomba.png")
PLAYER_IMAGE = os.path.join(PATH, "..", "assets/player.png")
BRICK_IMAGE = os.path.join(PATH, "..", "assets/brick-0.png")
ATTACK_PLAYER_IMAGE = os.path.join(PATH, "..", "assets/goomba2.png")


