
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

        boss = cast["boss"][0]

        walls = cast["wall"]

        enemy_to_remove = []

        for enemy in cast["enemy"]:
            self._enemy_collision(enemy, player, walls, constants.TRACKING)
            self._player_attack(enemy, player)


            if player.collides_with_sprite(enemy) and player.get_health() <= 0:    
                #game_view = GameOverView()
                #self.window.show_view(game_view)
                player.set_game_over()


            if player.collides_with_sprite(enemy) and enemy.get_health() <= 0:
                enemy_to_remove.append(enemy)


        key_hit_list = []
        for key in cast["key"]:
            key_hit_list = arcade.check_for_collision_with_list(player,key)
            print("key found")

        for key in key_hit_list:
            key.remove_from_sprite_lists()

        for enemy in enemy_to_remove:
            cast["enemy"].remove(enemy)

        #Everything in this method beyond this point is for the boss
        if player.collides_with_sprite(boss) and player.get_health() <= 0:    
                #game_view = GameOverView()
                #self.window.show_view(game_view)
                player.set_game_over()

        self._enemy_collision(boss, player, walls, constants.BOSS_TRACKING)
        #self._player_attack(boss, player)
        if(player.get_attack2()):
            if player.collides_with_sprite(boss) and player.get_attack():
                boss.sub_health()
                player.set_attack2(False)

        if player.collides_with_sprite(boss) and boss.get_health() <= 0:
                boss.set_game_over()


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


        if(player.get_attack2()):
            if(player.get_attack() and abs(enemy_x - player_x) < constants.RANGE and abs(enemy_y - player_y) < constants.RANGE):
                enemy.sub_health()
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
               
    def _enemy_collision(self, enemy, player, walls, tracking):
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
            if enemy_x > player_x and abs(enemy_x - player_x) < tracking and abs(enemy_y - player_y) < tracking:
                enemy.change_x_neg()
            elif enemy_x < player_x and abs(enemy_x - player_x) < tracking and abs(enemy_y - player_y) < tracking:
                enemy.change_x_pos()
            else:
                enemy.change_x = 0

            if enemy_y > player_y and abs(enemy_y - player_y) < tracking and abs(enemy_x - player_x) < tracking:
                enemy.change_y_neg()
            elif enemy_y < player_y and abs(enemy_y - player_y) < tracking and abs(enemy_x - player_x) < tracking:
                enemy.change_y_pos()
            else:
                enemy.change_y = 0
        
   
        
    