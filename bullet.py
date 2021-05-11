import pygame
from character import Enemy
from abc import ABC, abstractmethod
import random
from math import cos, sin


class Bullet(ABC, Enemy):
    """
    A general bullet superclass that inherits ABC and Enemy class

    Attributes:
            pos_x: int representing location in x coordinate
            pos_y: int representing location in y coordinate
            speed: int representing change in location with respect to time
            sprite: string representing source image path
    """

    def __init__(self):
        """
        Initializes a Bullet instance
        """

        self.pos_x = None
        self.pos_y = None
        self.speed = None
        self.sprite = None

    @abstractmethod
    def update(self):
        """
        Update position of the instance
        """

        pass


class ReimBullet(Bullet):
    """
    User Bullet that inherits the Bullet class

    Attributes:
            pos_x: int representing location in x coordinate
            pos_y: int representing location in y coordinate
            speed: int representing change in location with respect to time
            sprite: string representing source image path
    """

    def __init__(self, pos_x, pos_y):
        """
        Initialzies the ReimBullet instance

        Args:
            pos_x: an int representing the x coordinate
            pos_y: an int representing the y coordinate
        """

        self._pos_x = pos_x
        self._pos_y = pos_y
        self._speed = 8
        self._sprite = pygame.image.load("bullet.png")

    def update(self):
        """
        Update position of the instance
        """

        self.set_pos_y(self._pos_y - self._speed)


class EnemyBullet(ReimBullet):
    """
    Enemy Bullet that inherits ReimBullet class

    Attributes:
            pos_x: int representing location in x coordinate
            pos_y: int representing location in y coordinate
            speed: int representing change in location with respect to time
            sprite: string representing source image path
            angle: int representing the angle that the bullet fires
    """

    def __init__(self, pos_x, pos_y):
        """
        Initialzies the ReimBullet instance

        Args:
            pos_x: an int representing the x coordinate
            pos_y: an int representing the y coordinate
        """

        self._pos_x = pos_x
        self._pos_y = pos_y
        self._speed = 2
        self._sprite = pygame.image.load("enemy_bullet.png")
        self._angle = random.randint(-30, 30)

    def update(self):
        """
        Update position of the instance with speed components in x and y

        To shoot downwards and in a certain angle, each of the components
        is calculated and then the y component is positive
        """

        speed_y = self._speed * sin(self._angle)
        speed_x = self._speed * cos(self._angle)
        self.set_pos_y(self._pos_y + abs(speed_y))
        self.set_pos_x(self._pos_x + speed_x)
