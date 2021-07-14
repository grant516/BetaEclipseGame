import arcade
from arcade import sprite_list
from data import constants


class Director(arcade.Window):
    def __init__(self, cast, script, input_service, output_service):
        """Initialize the game
        """
        super().__init__(constants.MAX_X, constants.MAX_Y, "director")

        self._cast = cast
        self._script = script
        self._input_service = input_service
        self._output_service = output_service

        self.player_list = arcade.SpriteList()
        #self.wall_list = arcade.SpriteList()
        #self.ground_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.key_list = arcade.SpriteList()

        self.background = arcade.load_texture(constants.GROUND)
        #self.enemy_physics = []

        #used to keep track of the scrolling
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):

        #setting up the player so it works...
        """image_source = os.path.join(PATH, "assets/player.png")
        self.player_sprite = arcade.Sprite(image_source)
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)"""
        player_sprite = self._cast["player"][0]
        enemy_sprites = self._cast["enemy"]
        wall_list = self._cast["wall"]

        for x in range (0, len(enemy_sprites)):
            self.enemy_list.append(enemy_sprites[x])

        self.player_list.append(player_sprite)
        
        keys_layer_name = 'Keys'

        arcade.set_background_color(arcade.color.BLACK)
        my_map = arcade.tilemap.read_tmx(constants.MAP)
        """
        #maze_ground = 'Ground'
        maze_walls = 'Walls'
        

        arcade.set_background_color(arcade.color.BLACK)
        my_map = arcade.tilemap.read_tmx(constants.MAP)

        #self.ground_list = arcade.tilemap.process_layer(map_object = my_map,
        #                                              layer_name = maze_ground,
        #                                              scaling = constants.TILE_SCALING,
        #                                              use_spatial_hash=True)

        self.wall_list = arcade.tilemap.process_layer(map_object = my_map,
                                                      layer_name = maze_walls,
                                                      scaling = constants.TILE_SCALING,
                                                      use_spatial_hash=True)

        #adding wall_list to the cast
        self._cast["wall"] = self.wall_list
        """
        
        self.key_list = arcade.tilemap.process_layer(my_map, keys_layer_name, constants.TILE_SCALING)

        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(player_sprite, wall_list, 0)

        #self.enemy_physics = (arcade.PhysicsEnginePlatformer(self.enemy_list, self.wall_list, 0))

    def on_update(self, delta_time):

        player_sprite = self._cast["player"][0]
        self.physics_engine.update()
        #self.enemy_physics.update()

        self._cue_action("update")
        if(player_sprite.get_game_over()):
            print("game over")
            #self.texture = arcade.load_texture("game_over.png")

        self.player_list.update_animation(delta_time)

        #Below is all the code potintially needed so the map moves with the user
        changed = False
        # Scroll left
        left_boundary = self.view_left + constants.LEFT_VIEWPORT_MARGIN
        if player_sprite.left < left_boundary:
            self.view_left -= left_boundary - player_sprite.left
            changed = True
        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_VIEWPORT_MARGIN
        if player_sprite.right > right_boundary:
            self.view_left += player_sprite.right - right_boundary
            changed = True
        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.TOP_VIEWPORT_MARGIN
        if player_sprite.top > top_boundary:
            self.view_bottom += player_sprite.top - top_boundary
            changed = True
        # Scroll down
        bottom_boundary = self.view_bottom + constants.BOTTOM_VIEWPORT_MARGIN
        if player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - player_sprite.bottom
            changed = True
        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)
            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)


    def on_draw(self):
        self._output_service.clear_screen()

        #need to figure out how not to hard code the width and the height. -Grant_Note
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            2400, 2400,
                                            self.background)
        self._cast["wall"].draw()
        self._cue_action("output")

        

    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        self._input_service.end_attack() #this will end the attack so it doesn't kill everything for the rest of the game.
        self._cast["player"][0].set_attack2(True)
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)