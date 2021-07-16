import random
from data import constants
import arcade
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

        walls = cast["wall"]

        enemy_to_remove = []

        for enemy in cast["enemy"]:
            self._enemy_collision(enemy, player, walls)
            self._player_attack(enemy, player)

            """self._handle_wall_bounce(ball)
            self._handle_paddle_bounce(ball, paddle)

            bricks = cast["bricks"]
            self._handle_brick_collision(ball, bricks)
            """
            if player.collides_with_sprite(enemy) and player.get_health() <= 0:
                print("you dead")
                player.set_game_over()
            if enemy.collides_with_sprite(player) and enemy.get_health() <= 0:
                enemy_to_remove.append(enemy)

        for enemy in enemy_to_remove:
            cast["enemy"].remove(enemy)

    def _handle_wall_bounce(self, enemy):
        enemy_x = enemy.center_x
        enemy_y = enemy.center_y

    def _is_off_screen(self, enemy):
        return enemy.center_y < 0

    def _player_attack(self, enemy, player):
        enemy_x = enemy.center_x
        enemy_y = enemy.center_y
        player_x = player.center_x
        player_y = player.center_y

        #if(player.get_attack()):
        #    print("hi")

        if(player.get_attack2()):
            if(player.get_attack() and abs(enemy_x - player_x) < constants.RANGE and abs(enemy_y - player_y) < constants.RANGE):
            #if(player.get_attack() and player.collides_with_sprite(enemy)):
                enemy.sub_health()
                print("attack")
                player.set_attack2(False)

                #designed to make the enemy sort of bounce back after getting hit
                """if(enemy.change_x < 0):
                    enemy.change_x = 0
                    enemy.center_x += 20
                elif(enemy.change_x > 0):
                    enemy.change_x = 0
                    enemy.center_x -= 20

                if(enemy.change_y < 0):
                    enemy.change_y = 0
                    enemy.center_y += 20
                elif(enemy.change_y > 0):
                    enemy.change_y = 0
                    enemy.center_y -= 20"""
               
    def _enemy_collision(self, enemy, player, walls):
        enemy_x = enemy.center_x
        enemy_y = enemy.center_y
        player_x = player.center_x
        player_y = player.center_y

        if (enemy.collides_with_sprite(player) and player.get_attack() != True):
            player.sub_health()
        elif len(arcade.check_for_collision_with_list(enemy, walls)) > 0:
                if(enemy.change_x < 0):
                    enemy.change_x = 0
                    enemy.center_x += 10
                elif(enemy.change_x > 0):
                    enemy.change_x = 0
                    enemy.center_x -= 10

                if(enemy.change_y < 0):
                    enemy.change_y = 0
                    enemy.center_y += 10
                elif(enemy.change_y > 0):
                    enemy.change_y = 0
                    enemy.center_y -= 10
        else:
            if enemy_x > player_x and abs(enemy_x - player_x) < constants.TRACKING and abs(enemy_y - player_y) < constants.TRACKING:
                enemy.change_x_neg()
            elif enemy_x < player_x and abs(enemy_x - player_x) < constants.TRACKING and abs(enemy_y - player_y) < constants.TRACKING:
                enemy.change_x_pos()
            else:
                enemy.change_x = 0

            if enemy_y > player_y and abs(enemy_y - player_y) < constants.TRACKING and abs(enemy_x - player_x) < constants.TRACKING:
                enemy.change_y_neg()
            elif enemy_y < player_y and abs(enemy_y - player_y) < constants.TRACKING and abs(enemy_x - player_x) < constants.TRACKING:
                enemy.change_y_pos()
            else:
                enemy.change_y = 0
        
        
        
    