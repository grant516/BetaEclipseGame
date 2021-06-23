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

        balls_to_remove = []

        for ball in cast["balls"]:
            self._enemy_collision(ball, player)

            """self._handle_wall_bounce(ball)
            self._handle_paddle_bounce(ball, paddle)

            bricks = cast["bricks"]
            self._handle_brick_collision(ball, bricks)

            if constants.BALLS_CAN_DIE and self._is_off_screen(ball):
                balls_to_remove.append(ball)"""

        for ball in balls_to_remove:
            cast["balls"].remove(ball)

    def _handle_wall_bounce(self, ball):
        ball_x = ball.center_x
        ball_y = ball.center_y

        # Check for bounce on walls
        if ball_x <= 0 or ball_x >= constants.MAX_X:
            ball.bounce_vertical()

        if ball_y >= constants.MAX_Y:
            ball.bounce_horizontal()
        
        if not constants.BALLS_CAN_DIE and ball_y <= 0:
            ball.bounce_horizontal()
    
    def _handle_paddle_bounce(self, ball, paddle):
        # This makes use of the `Sprite` functionality
        if paddle.collides_with_sprite(ball):
            # Ball and paddle collide!
            ball.bounce_horizontal()

    def _handle_brick_collision(self, ball, bricks):
        brick_to_remove = None

        for brick in bricks:
            # This makes use of the `Sprite` functionality
            if ball.collides_with_sprite(brick):
                ball.bounce_horizontal()
                brick_to_remove = brick
        
        if brick_to_remove != None:
            bricks.remove(brick_to_remove)

    def _is_off_screen(self, ball):
        return ball.center_y < 0

    def _enemy_collision(self, ball, player):
        ball_x = ball.center_x
        ball_y = ball.center_y
        player_x = player.center_x
        player_y = player.center_y

        if ball.collides_with_sprite(player):
                ball.bounce_horizontal()
                brick_to_remove = player
        else:
            if ball_x > player_x:
                ball.change_x_neg()
            elif ball_x < player_x:
                ball.change_x_pos()

            if ball_y > player_y:
                ball.change_y_neg()
            elif ball_y < player_y:
                ball.change_y_pos()
