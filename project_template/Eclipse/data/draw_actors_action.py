from data.action import Action
from data import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        #self._output_service.clear_screen()

        """bricks = cast["bricks"]

        for brick in bricks:
            self._output_service.draw_actor(brick)"""

        for enemy in cast["enemy"]:
            self._output_service.draw_actor(enemy)

        paddle = cast["player"][0] # there's only one
        self._output_service.draw_actor(paddle)

        self._output_service.flush_buffer()
