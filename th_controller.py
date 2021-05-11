import pygame
from th_model import ThGame


class ThController:
    """
    Input controller for the game

    Attributes:
        game: a ThGame instance for game status
    """

    def __init__(self, ThGame):
        """
        Initialize ThController instance

        Args:
            ThGame: a ThGame instance for game status
        """
        self._game = ThGame

    @property
    def game(self):
        """
        Returns the ThGame instance

        Returns:
            a ThGame instance
        """
        return self._game

    def event_listener(self):
        """
        Event manager that listens to the user inputs with keyboard
        """

        # If the pygame window is closed, shut down pygame and prevent
        # infinite loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._game.set_running(False)

            # Check if keys are pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    # Show slow sprite if LShift
                    self._game.reim.set_sprite("reim_slow.png")
                    self._game.reim.set_speed(5)
                if event.key == pygame.K_LEFT:
                    self._game.reim.set_left_pressed(True)
                if event.key == pygame.K_RIGHT:
                    self._game.reim.set_right_pressed(True)
                if event.key == pygame.K_UP:
                    self._game.reim.set_up_pressed(True)
                if event.key == pygame.K_DOWN:
                    self._game.reim.set_down_pressed(True)
                if event.key == pygame.K_z:
                    self._game.reim.set_z_pressed(True)

            # Check if keys are released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    # Show normal sprite of no LShift
                    self._game.reim.set_sprite("reim.png")
                    self._game.reim.set_speed(10)
                if event.key == pygame.K_LEFT:
                    self._game.reim.set_left_pressed(False)
                if event.key == pygame.K_RIGHT:
                    self._game.reim.set_right_pressed(False)
                if event.key == pygame.K_UP:
                    self._game.reim.set_up_pressed(False)
                if event.key == pygame.K_DOWN:
                    self._game.reim.set_down_pressed(False)
                if event.key == pygame.K_z:
                    self._game.reim.set_z_pressed(False)
