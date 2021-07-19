import arcade
from arcade import sprite_list
from data import constants
from data.director import Director

class Instruction_view(arcade.View):
    def __init__(self, cast, script, input_service, output_service):
        super().__init__()

        self._cast = cast
        self._script = script
        self._input_service = input_service
        self._output_service = output_service

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("ECLIPSE", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+200,
                         arcade.color.WHITE_SMOKE, font_size=35, anchor_x="center")
        arcade.draw_text("GOAL: GET THOSE KEYS AND BEAT THE FINAL BOSS... AND UHMM DON'T DIE ", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+150,
                         arcade.color.GOLD, font_size=17, anchor_x="center")
        arcade.draw_text("Attack Enemies: Space bar", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+100,
                         arcade.color.WHITE, font_size=15, anchor_x="center")
        arcade.draw_text("Left/right Arrow: Move Left and Right", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+50,
                         arcade.color.WHITE, font_size=15, anchor_x="center")
        arcade.draw_text("Top/bottom Arrow: Move Forward and Backward", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=15, anchor_x="center")
        arcade.draw_text("Click to advance", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-50,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Director(self._cast, self._script, self._input_service, self._output_service)
        game_view.setup()
        self.window.show_view(game_view)