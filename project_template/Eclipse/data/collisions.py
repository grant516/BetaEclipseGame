import random
from data import constants
from data.action import Action

class Collisions(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        player = cast["player"][0]

        enemy_to_remove = []

        for enemy in cast["enemy"]:
            self._enemy_collision(enemy, player)
            self._player_attack(enemy, player)

            """self._handle_wall_bounce(ball)
            self._handle_paddle_bounce(ball, paddle)

            bricks = cast["bricks"]
            self._handle_brick_collision(ball, bricks)
            """
            if player.collides_with_sprite(enemy) and player.get_health() <= 0:
                print("you dead")
                #player.set_game_over()
            if enemy.collides_with_sprite(player) and enemy.get_health() <= 0:
                enemy_to_remove.append(enemy)

        for enemy in enemy_to_remove:
            cast["enemy"].remove(enemy)

    def _handle_wall_bounce(self, enemy):
        enemy_x = enemy.center_x
        enemy_y = enemy.center_y

        # Check for bounce on walls
        # if enemy_x <= 0 or enemy_x >= constants.MAX_X:
        #     enemy.bounce_vertical()

        # if enemy_y >= constants.MAX_Y:
        #     enemy.bounce_horizontal()
        
        # if not constants.ENEMY_CAN_DIE and enemy_y <= 0:
        #     enemy.bounce_horizontal()
    
    #def _handle_paddle_bounce(self, enemy, paddle):
        # This makes use of the `Sprite` functionality
        # if paddle.collides_with_sprite(enemy):
        #     # Ball and paddle collide!
        #     enemy.bounce_horizontal()

    # def _handle_brick_collision(self, enemy, bricks):
    #     brick_to_remove = None

    #     #for brick in bricks:
    #         # This makes use of the `Sprite` functionality
    #         # if enemy.collides_with_sprite(brick):
    #         #     #enemy.bounce_horizontal()
    #         #     brick_to_remove = brick
        
    #     if brick_to_remove != None:
    #         bricks.remove(brick_to_remove)

    def _is_off_screen(self, enemy):
        return enemy.center_y < 0

    def _player_attack(self, enemy, player):
        enemy_x = enemy.center_x
        enemy_y = enemy.center_y
        player_x = player.center_x
        player_y = player.center_y

        if(player.get_attack() and abs(enemy_x - player_x) < constants.RANGE and abs(enemy_y - player_y) < constants.RANGE):
               enemy.sub_health()
               print("attack")
               
    def _enemy_collision(self, enemy, player):
        enemy_x = enemy.center_x
        enemy_y = enemy.center_y
        player_x = player.center_x
        player_y = player.center_y

        if enemy.collides_with_sprite(player):
            player.sub_health()
        else:
            if enemy_x > player_x and abs(enemy_x - player_x) < constants.TRACKING and abs(enemy_y - player_y) < constants.TRACKING:
                enemy.change_x_neg()
            elif enemy_x < player_x and abs(enemy_x - player_x) < constants.TRACKING and abs(enemy_y - player_y) < constants.TRACKING:
                enemy.change_x_pos()

            if enemy_y > player_y and abs(enemy_y - player_y) < constants.TRACKING and abs(enemy_x - player_x) < constants.TRACKING:
                enemy.change_y_neg()
            elif enemy_y < player_y and abs(enemy_y - player_y) < constants.TRACKING and abs(enemy_x - player_x) < constants.TRACKING:
                enemy.change_y_pos()
        
        
    