import os

RANGE = 50
TRACKING = 150

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

TILE_SCALING = 1


PATH = os.path.dirname(os.path.abspath(__file__))
ENEMY_IMAGE = os.path.join(PATH, "..", "assets/goomba.png")
PLAYER_IMAGE = os.path.join(PATH, "..", "assets/player.png")
ATTACK_PLAYER_IMAGE = os.path.join(PATH, "..", "assets/goomba2.png")
MAP = os.path.join(PATH, "..", "assets/test_map.tmx")
# MAP = ":resources:/tmx_maps/map.tmx"
