import os

RANGE = 50
TRACKING = 150

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAP_HEIGHT = 2400
MAP_WIDTH = 2400

MAX_X = 800
MAX_Y = 600
NUM_ENEMY = 50

ENEMY_SPEED = 3
ENEMY_Y = MAX_Y / 2

PLAYER_Y = 25

PLAYER_MOVE_SCALE = 3

BRICK_WIDTH = 25
BRICK_HEIGHT = 15
BRICK_SPACE = 10

ENEMY_CAN_DIE = False

TILE_SCALING = 1

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 100
TOP_VIEWPORT_MARGIN = 100


PATH = os.path.dirname(os.path.abspath(__file__))
ENEMY_IMAGE = os.path.join(PATH, "..", "assets/goomba.png")
PLAYER_IMAGE = os.path.join(PATH, "..", "assets/player.png")
ATTACK_PLAYER_IMAGE = os.path.join(PATH, "..", "assets/goomba2.png")
MAP = os.path.join(PATH, "..", "assets/final_map.tmx")

GROUND = os.path.join(PATH, "..", "assets/ground.png")

# MAP = ":resources:/tmx_maps/map.tmx"
