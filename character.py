import pygame
import random
from math import sqrt


class Character:
    """
    A general character superclass


        Attributes:
            pos_x: int representing location in x coordinate
            pos_y: int representing location in y coordinate
            speed: int representing change in location with respect to time
            sprite: string representing source image path
    """

    def __init__(self):
        """
        Initializes a Character instance
        """

        self.pos_x = None
        self.pos_y = None
        self.speed = None
        self.sprite = None

    @property
    def pos_x(self):
        """
        Returns pos_x

        Returns:
            an int representing location in x coordinate
        """
        return self._pos_x

    @property
    def speed(self):
        """
        Returns speed

        Returns:
            an int representing speed
        """
        return self._speed

    def set_sprite(self, sprite):
        """
        Setter for sprite path

        Args:
            sprite: a string representing the sprite to change to
        """
        self._sprite = pygame.image.load(sprite)

    @property
    def pos_y(self):
        """
        Returns pos_y

        Returns:
            an int representing location in y coordinate
        """
        return self._pos_y

    @property
    def sprite(self):
        """
        Returns sprite

        Returns:
            the pygame image of sprite
        """
        return self._sprite

    def set_pos_x(self, pos_x):
        """
        Setter for pos_x

        Args:
            pos_x: an int for the new pos
        """
        self._pos_x = pos_x

    def set_pos_y(self, pos_y):
        """
        Setter for pos_y

        Args:
            pos_y: an int for the new pos
        """
        self._pos_y = pos_y

    def set_speed(self, speed):
        """
        Setter for speed

        Args:
            speed: an int for the new speed
        """
        self._speed = speed


class Reim(Character):
    """
    User character that inherits the Character class

    Attributes:
            pos_x: int representing location in x coordinate
            pos_y: int representing location in y coordinate
            speed: int representing change in location with respect to time
            speed_slow: int representing a slower change in location
            sprite: string representing source image path
            left_pressed: a boolean representing the state of left button
            right_pressed: a boolean representing the state of right button
            up_pressed: a boolean representing the state of up button
            down_pressed: a boolean representing the state of down button
            z_pressed: a boolean representing the state of z button
    """

    def __init__(self):
        """
        Initializes a Reim instance
        """

        self._pos_x = 380
        self._pos_y = 500
        self._speed = 10
        self._sprite = pygame.image.load("reim.png")
        self._left_pressed = False
        self._right_pressed = False
        self._up_pressed = False
        self._down_pressed = False
        self._z_pressed = False

    def set_left_pressed(self, left_pressed):
        """
        Setter for left_pressed

        Args:
            left_pressed: a boolean representing the new left_pressed
        """
        self._left_pressed = left_pressed

    def set_right_pressed(self, right_pressed):
        """
        Setter for right_pressed

        Args:
            right_pressed: a boolean representing the new right_pressed
        """
        self._right_pressed = right_pressed

    def set_up_pressed(self, up_pressed):
        """
        Setter for up_pressed

        Args:
            up_pressed: a boolean representing the new up_pressed
        """
        self._up_pressed = up_pressed

    def set_down_pressed(self, down_pressed):
        """
        Setter for down_pressed

        Args:
            down_pressed: a boolean representing the new down_pressed
        """
        self._down_pressed = down_pressed

    def set_z_pressed(self, z_pressed):
        """
        Setter for z_pressed

        Args:
            down_pressed: a boolean representing the new z_pressed
        """
        self._z_pressed = z_pressed

    @property
    def z_pressed(self):
        """
        Returns z_pressed

        Returns:
            a boolean representing z_pressed
        """
        return self._z_pressed

    @property
    def left_pressed(self):
        """
        Returns left_pressed

        Returns:
            a boolean representing left_pressed
        """
        return self._left_pressed

    @property
    def right_pressed(self):
        """
        Returns right_pressed

        Returns:
            a boolean representing right_pressed
        """
        return self._right_pressed

    @property
    def down_pressed(self):
        """
        Returns down_pressed

        Returns:
            a boolean representing down_pressed
        """
        return self._down_pressed

    @property
    def up_pressed(self):
        """
        Returns up_pressed

        Returns:
            a boolean representing up_pressed
        """
        return self._up_pressed

    def update(self):
        """
        Updates the location of Reim
        """
        speed_x = 0
        speed_y = 0

        if self.left_pressed and not self.right_pressed:
            speed_x += -self.speed
        if self.right_pressed and not self.left_pressed:
            speed_x += self.speed
        if self.up_pressed and not self.down_pressed:
            speed_y += -self.speed
        if self.down_pressed and not self.up_pressed:
            speed_y += self.speed

        # Make moving diagonally smoother
        if self.left_pressed or self.right_pressed and self.up_pressed \
                or self.down_pressed:
            speed_x /= sqrt(2)

        self.set_pos_x(speed_x + self._pos_x)
        self.set_pos_y(speed_y + self._pos_y)


class Enemy(Character):
    """
    Enemy instance that inherits the Character class

    Attributes:
        angle: int representing the initial angle of movement
        pos_x: int representing location in x coordinate
        pos_y: int representing location in y coordinate
        speed: int representing change in location with respect to time
        sprite: string representing source image path
    """

    def __init__(self):
        """
        Initializes an Enemy instance
        """

        # Randomizes the location and move speed
        self._angle = random.randint(-90, 90)
        self._pos_x = random.randint(50, 468)
        self._pos_y = random.randint(20, 150)
        self._speed = 1
        self._sprite = pygame.image.load("enemy.png")

    @property
    def angle(self):
        """
        Return the angle

        Returns:
            an int representing the angle
        """

        return self._angle

    def set_angle(self, angle):
        """
        Setter for angle

        Args:
            angle: an int representing the new angle
        """
        self._angle = angle
