from project_template.Eclipse.data import constants
import arcade

class GameOver(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.YELLOW)
        
    def on_draw(self):
        arcade.start_render()

        #To draw
        arcade.draw_text("Game Over", 250, 400, arcade.color.BLACK, 54)

