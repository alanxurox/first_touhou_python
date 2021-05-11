import pygame
from th_model import ThGame


class ThView:
    """
    Graphics updator for the game

    Attributes:
        game: a ThGame instance for game status
        screen: a pygame surface for the graphics to be updated on
    """

    def __init__(self, ThGame):
        """
        Initializes an instance of ThView

        Args:
            ThGame: a ThGame instance for game status
        """
        self._game = ThGame
        self._screen = None

    @property
    def game(self):
        """
        Returns the ThGame instance

        Returns:
            a ThGame instance
        """
        return self._game

    def initialize(self):
        """
        Initialize the game graphics
        """
        pygame.init()
        self._screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Touhou Softdes")

        # Initialize reim sprite
        self._screen.blit(self._game._reim.sprite,
                          (self._game._reim.pos_x, self._game._reim.pos_y))

        # Initialize enemy spirtes
        for enemy in self._game._enemies:
            self._screen.blit(enemy.sprite,
                              (enemy.pos_x, enemy.pos_y))
        pygame.display.flip()

    def update(self):
        """
        Update the game graphics
        """
        bg = pygame.image.load("bg.png")
        self._screen.blit(bg, (0, 0))

        # The game scene where actions are played
        game_bg = pygame.image.load("game_bg.png")
        game_bg.set_alpha(200)
        self._screen.blit(game_bg, (50, 20))

        # Update reim, enemy, and bullet sprites
        self._screen.blit(self._game._reim.sprite,
                          (self._game._reim.pos_x, self._game._reim.pos_y))

        for enemy in self._game._enemies:
            self._screen.blit(enemy.sprite,
                              (enemy.pos_x, enemy.pos_y))

        for bullet in self.game._bullets:
            bullet.update()
            self._screen.blit(pygame.transform.scale(bullet.sprite, (8, 8)),
                              (bullet.pos_x, bullet.pos_y))

        for enemy_bullet in self.game._enemy_bullets:
            self._screen.blit(pygame.transform.scale(enemy_bullet.sprite, (16, 16)),
                              (enemy_bullet.pos_x, enemy_bullet.pos_y))

        pygame.display.flip()
