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

ENEMY_SPEED = 4
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

#The walking sprite images
PLAYER_RIGHT1 = os.path.join(PATH, "..", "assets/player_walking_right_1.png")
PLAYER_RIGHT2 = os.path.join(PATH, "..", "assets/player_walking_right_2.png")
PLAYER_LEFT1 = os.path.join(PATH, "..", "assets/player_walking_left_1.png")
PLAYER_LEFT2 = os.path.join(PATH, "..", "assets/player_walking_left_2.png")
PLAYER_UP1 = os.path.join(PATH, "..", "assets/player_walking_up_1.png")
PLAYER_UP2 = os.path.join(PATH, "..", "assets/player_walking_up_2.png")
PLAYER_DOWN1 = os.path.join(PATH, "..", "assets/player_walking_down_1.png")
PLAYER_DOWN2 = os.path.join(PATH, "..", "assets/player_walking_down_2.png")

#Sword Images
PLAYER_SWORD_RIGHT_1 = os.path.join(PATH, "..", "assets/right_sword_1.png")
PLAYER_SWORD_RIGHT_2 = os.path.join(PATH, "..", "assets/right_sword_2.png")
PLAYER_SWORD_RIGHT_3 = os.path.join(PATH, "..", "assets/right_sword_3.png")

PLAYER_SWORD_LEFT_1 = os.path.join(PATH, "..", "assets/left_sword_1.png")
PLAYER_SWORD_LEFT_2 = os.path.join(PATH, "..", "assets/left_sword_2.png")
PLAYER_SWORD_LEFT_3 = os.path.join(PATH, "..", "assets/left_sword_3.png")

PLAYER_SWORD_DOWN_1 = os.path.join(PATH, "..", "assets/down_sword_1.png")
PLAYER_SWORD_DOWN_2 = os.path.join(PATH, "..", "assets/down_sword_2.png")
PLAYER_SWORD_DOWN_3 = os.path.join(PATH, "..", "assets/down_sword_3.png")

PLAYER_SWORD_UP_1 = os.path.join(PATH, "..", "assets/up_sword_1.png")
PLAYER_SWORD_UP_2 = os.path.join(PATH, "..", "assets/up_sword_2.png")
PLAYER_SWORD_UP_3 = os.path.join(PATH, "..", "assets/up_sword_3.png")

PLAYER_FRAMES = 4

RIGHT_FACING = 0
LEFT_FACING = 1
UP_FACING = 2
DOWN_FACING = 3