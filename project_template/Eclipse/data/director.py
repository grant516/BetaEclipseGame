import arcade
from arcade import sprite_list
from data import constants


class Director(arcade.Window):
    def __init__(self, cast, script, input_service):
        """Initialize the game
        """
        super().__init__(constants.MAX_X, constants.MAX_Y, "director")

        self._cast = cast
        self._script = script
        self._input_service = input_service

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

    def setup(self):

        #setting up the player so it works...
        """image_source = os.path.join(PATH, "assets/player.png")
        self.player_sprite = arcade.Sprite(image_source)
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)"""
        player_sprite = self._cast["player"][0]

        self.player_list.append(player_sprite)
        
        maze_ground = 'Ground'
        maze_walls = 'Walls'
        arcade.set_background_color(arcade.color.BLACK)
        my_map = arcade.tilemap.read_tmx(constants.MAP)
        self.ground_list = arcade.tilemap.process_layer(map_object = my_map,
                                                      layer_name = maze_ground,
                                                      scaling = constants.TILE_SCALING,
                                                      use_spatial_hash=True)

        self.wall_list = arcade.tilemap.process_layer(map_object = my_map,
                                                      layer_name = maze_walls,
                                                      scaling = constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(player_sprite, self.wall_list, 0)

    def on_update(self, delta_time):
        self.physics_engine.update()

        self._cue_action("update")
        if(self._cast["player"][0].get_game_over()):
            print("game over")
            #self.texture = arcade.load_texture("game_over.png")


    def on_draw(self):
        self._cue_action("output")
        self.wall_list.draw()

        

    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        self._input_service.end_attack() #this will end the attack so it doesn't kill everything for the rest of the game.
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)