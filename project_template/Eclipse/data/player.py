# from data.point import Point
from data import constants
from data.health import SpriteWithHealth

import arcade


class Player(SpriteWithHealth):
    def __init__(self, image, scale, health_y_position, text_y_position, text_x_position, health_width, height, max_health):
        super().__init__(image, scale, health_y_position,
                         text_y_position, text_x_position, health_width, height, max_health)

#class Player(arcade.Sprite):
#    def __init__(self):
#        #super().__init__(constants.PLAYER_DOWN1)
#        super().__init__()


        #self.center_x = int(constants.MAX_X / 2)
        #self.center_y = int(constants.PLAYER_Y)

        self.center_x = 128
        self.center_y = 128
        self._health = 100
        self._game_over = False
        self._attack = False
        self._attack2 = True

        # Default to face-right
        self.character_face_direction = constants.RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.idle_texture_pair = arcade.load_texture(constants.PLAYER_DOWN1)

        self.down_texture_pair = []
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_DOWN1)
            self.down_texture_pair.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_DOWN2)
            self.down_texture_pair.append(texture)

        self.up_texture_pair = []
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_UP1)
            self.up_texture_pair.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_UP2)
            self.up_texture_pair.append(texture)

        self.walk_right_textures = []
        
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_RIGHT1)
            self.walk_right_textures.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_RIGHT2)
            self.walk_right_textures.append(texture)

        self.walk_left_textures = []
        
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_LEFT1)
            self.walk_left_textures.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_LEFT2)
            self.walk_left_textures.append(texture)

        self.sword_right_textures = []
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_RIGHT_1)
            self.sword_right_textures.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_RIGHT_2)
            self.sword_right_textures.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_RIGHT_3)
            self.sword_right_textures.append(texture)
        texture = arcade.load_texture(constants.PLAYER_RIGHT1)
        self.sword_right_textures.append(texture)

        self.sword_left_textures = []
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_LEFT_1)
            self.sword_left_textures.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_LEFT_2)
            self.sword_left_textures.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_LEFT_3)
            self.sword_left_textures.append(texture)
        texture = arcade.load_texture(constants.PLAYER_LEFT1)
        self.sword_left_textures.append(texture)

        self.sword_down_textures = []
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_DOWN_1)
            self.sword_down_textures.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_DOWN_2)
            self.sword_down_textures.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_DOWN_3)
            self.sword_down_textures.append(texture)
        texture = arcade.load_texture(constants.PLAYER_DOWN1)
        self.sword_down_textures.append(texture)

        self.sword_up_textures = []
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_UP_1)
            self.sword_up_textures.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_UP_2)
            self.sword_up_textures.append(texture)
        for x in range (0, constants.PLAYER_FRAMES):
            texture = arcade.load_texture(constants.PLAYER_SWORD_UP_3)
            self.sword_up_textures.append(texture)
        texture = arcade.load_texture(constants.PLAYER_UP1)
        self.sword_up_textures.append(texture)

        self.texture = self.idle_texture_pair

        #self.set_hit_box(self.texture.hit_box_points)
        self.set_hit_box(self.texture.hit_box_points)

    def get_health(self):
        return(self.cur_health)

    def sub_health(self):
        self.cur_health -= 1

    def get_game_over(self):
        return(self._game_over)

    def set_game_over(self):
        self._game_over = True

    def get_attack(self):
        return(self._attack)

    def set_attack(self, state):
        self._attack = state

    def get_attack2(self):
        return(self._attack2)

    def set_attack2(self, state):
        self._attack2 = state

#this is to help us make the player look like they are walking
    def update_animation(self, delta_time: float = 1/60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == constants.RIGHT_FACING:
            self.character_face_direction = constants.LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == constants.LEFT_FACING:
            self.character_face_direction = constants.RIGHT_FACING


        # Jumping animation
        if self.change_y > 0:
            self.cur_texture += 1
            if self.cur_texture > (len(self.up_texture_pair)-1):
                self.cur_texture = 0
            self.texture = self.up_texture_pair[self.cur_texture]#[self.character_face_direction]
            self.character_face_direction = constants.UP_FACING

            new_hit = self.up_texture_pair[self.cur_texture]
            self.set_hit_box(new_hit.hit_box_points)
            #return
        elif self.change_y < 0:
            self.cur_texture += 1
            if self.cur_texture > (len(self.down_texture_pair)-1):
                self.cur_texture = 0
            self.texture = self.down_texture_pair[self.cur_texture]#[self.character_face_direction]
            self.character_face_direction = constants.DOWN_FACING

            #new_hit = self.down_texture_pair[self.cur_texture]
            #self.set_hit_box(new_hit.hit_box_points)
            #return

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            #self.texture = self.idle_texture_pair[self.character_face_direction]
            #self.texture = self.idle_texture_pair
            self.texture = self.texture
            new_hit = self.texture
            self.set_hit_box(new_hit.hit_box_points)
            #return

        # Walking right animation
        if self.change_x > 0:
            self.cur_texture += 1
            if self.cur_texture > (len(self.walk_right_textures)-1):
                self.cur_texture = 0
            self.texture = self.walk_right_textures[self.cur_texture]#[self.character_face_direction]
            self.character_face_direction = constants.RIGHT_FACING

            new_hit = self.walk_right_textures[self.cur_texture]
            self.set_hit_box(new_hit.hit_box_points)
        elif self.change_x < 0:
            # Walking left animation
            self.cur_texture += 1
            if self.cur_texture > (len(self.walk_left_textures)-1):#3:
                self.cur_texture = 0
            self.texture = self.walk_left_textures[self.cur_texture]#[self.character_face_direction]
            self.character_face_direction = constants.LEFT_FACING

            new_hit = self.walk_left_textures[self.cur_texture]
            self.set_hit_box(new_hit.hit_box_points)

        if self._attack:
            if(self.character_face_direction == constants.RIGHT_FACING):
                self.cur_texture += 1
                if self.cur_texture > (len(self.sword_right_textures)-1):
                    self.cur_texture = 0
                self.texture = self.sword_right_textures[self.cur_texture]
                new_hit = self.sword_right_textures[self.cur_texture]
                self.set_hit_box(new_hit.hit_box_points)
                if(self.cur_texture == (len(self.sword_right_textures)-1)):
                    self._attack = False
            elif(self.character_face_direction == constants.LEFT_FACING):
                self.cur_texture += 1
                if self.cur_texture > (len(self.sword_left_textures)-1):
                    self.cur_texture = 0
                self.texture = self.sword_left_textures[self.cur_texture]
                new_hit = self.sword_left_textures[self.cur_texture]
                self.set_hit_box(new_hit.hit_box_points)
                if(self.cur_texture == (len(self.sword_left_textures)-1)):
                    self._attack = False
            elif(self.character_face_direction == constants.DOWN_FACING):
                self.cur_texture += 1
                if self.cur_texture > (len(self.sword_down_textures)-1):
                    self.cur_texture = 0
                self.texture = self.sword_down_textures[self.cur_texture]
                new_hit = self.sword_down_textures[self.cur_texture]
                self.set_hit_box(new_hit.hit_box_points)
                if(self.cur_texture == (len(self.sword_down_textures)-1)):
                    self._attack = False
            elif(self.character_face_direction == constants.UP_FACING):
                self.cur_texture += 1
                if self.cur_texture > (len(self.sword_up_textures)-1):
                    self.cur_texture = 0
                self.texture = self.sword_up_textures[self.cur_texture]
                new_hit = self.sword_up_textures[self.cur_texture]
                self.set_hit_box(new_hit.hit_box_points)
                if(self.cur_texture == (len(self.sword_up_textures)-1)):
                    self._attack = False


        """RIGHT_FACING = 0
        LEFT_FACING = 1
        UP_FACING = 2
        DOWN_FACING = 3"""

