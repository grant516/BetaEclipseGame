import arcade
from arcade import sprite_list
from data import constants

from data.player import Player
from data.enemy import Enemy
#from data.boss import Boss
#from data.director import Director


class GameOverView(arcade.View):
    def __init__(self, cast, script, input_service, output_service, view_left, view_bottom):
        super().__init__()

        self._cast = cast
        self._script = script
        self._input_service = input_service
        self._output_service = output_service

        self.view_left = view_left
        self.view_bottom = view_bottom
       

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        if(self._cast["player"][0].get_game_over()):
            arcade.draw_text("Game Over", (self.view_left + constants.SCREEN_WIDTH/2), (self.view_bottom + constants.SCREEN_HEIGHT/2), arcade.color.WHITE, 54, anchor_x='center' )
            arcade.draw_text("You were Defeated",(self.view_left + constants.SCREEN_WIDTH/2), (self.view_bottom + constants.SCREEN_HEIGHT/2 -100), arcade.color.WHITE, 24, anchor_x='center' )
        elif(self._cast["boss"][0].get_game_over()):
            arcade.draw_text("You Win!!!", (self.view_left + constants.SCREEN_WIDTH/2), (self.view_bottom + constants.SCREEN_HEIGHT/2), arcade.color.WHITE, 54, anchor_x='center' )
            arcade.draw_text("You Defeated the Boss!",(self.view_left + constants.SCREEN_WIDTH/2), (self.view_bottom + constants.SCREEN_HEIGHT/2 -100), arcade.color.WHITE, 24, anchor_x='center' )

       

    """def on_mouse_press(self, _x, _y, _button, _modifiers):
        player = Player()
        self._cast["player"] = [player]
        self._cast["enemy"] = []

        for i in range(constants.NUM_ENEMY):
            enemy = Enemy()
            self._cast["enemy"].append(enemy)
            while len(arcade.check_for_collision_with_list(enemy, self._cast["wall"])) > 0:
                enemy.change_center_x()
                enemy.change_center_y()
            pass  
"""

        #director = Director(self._cast, self._script, self._input_service, self._output_service)
        #director.setup()
        #self.window.show_view(director)