# program entry point
import random
from data import constants
from data.point import Point
from data.control_actors_action import ControlActorsAction
from data.draw_actors_action import DrawActorsAction
from data.collisions import Collisions
from data.move_actors_action import MoveActorsAction
from data.arcade_input_service import ArcadeInputService
from data.arcade_output_service import ArcadeOutputService


from data.player import Player
from data.brick import Brick
from data.enemy import Enemy

from data.director import Director
import arcade
from arcade import sprite_list

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    player = Player(constants.PLAYER_IMAGE, 1, 24, 33, 10, 25, 5, 25)
    cast["player"] = [player]

    maze_walls = 'Walls'
    wall_list = arcade.SpriteList()

    my_map = arcade.tilemap.read_tmx(constants.MAP)

    wall_list = arcade.tilemap.process_layer(map_object = my_map,
                                                  layer_name = maze_walls,
                                                  scaling = constants.TILE_SCALING,
                                                  use_spatial_hash=True)
    #adding wall_list to the cast
    cast["wall"] = wall_list
    cast["enemy"] = []

    for i in range(constants.NUM_ENEMY):
        enemy = Enemy(constants.ENEMY_IMAGE, 1, 24, 33, 10, 15, 5, 5)
        cast["enemy"].append(enemy)
        while len(arcade.check_for_collision_with_list(enemy, cast["wall"])) > 0:
            enemy.change_center_x()
            enemy.change_center_y()


    #cast["background"] = None

    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()

    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = Collisions()
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the data
    director = Director(cast, script, input_service, output_service)
    director.setup()
    arcade.run()


if __name__ == "__main__":
    main()
