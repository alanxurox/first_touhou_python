import pygame
import random
from character import Reim, Enemy
from bullet import ReimBullet, EnemyBullet
from math import sqrt, cos, sin


class ThGame:
    """
    Game state
    """

    def __init__(self):
        """
        Attributes:
            running: a boolean representing the game status
            reim: a Reim instance
            enemies: a list of Enemy instances
            enemy_bullets: a list of EnemyBullets
            bullets: a list of ReimBullets
            ENEMY_BULLETS_MAX: a int representing a constant max of bullets
        """
        self._running = True
        self._reim = Reim()
        self._bullets = []
        self._enemy_bullets = []
        self._enemies = []
        for enemy_count in range(6):
            self._enemies.append(Enemy())
            self._enemy_bullets.append(EnemyBullet(
                self._enemies[enemy_count]._pos_x, self._enemies[enemy_count]._pos_y))
        self.ENEMY_BULLETS_MAX = 100

    def set_running(self, running):
        """
        Setter for running

        Args:
            running: a boolean representing the new status
        """
        self._running = running

    @property
    def running(self):
        """
        Returns running

        Returns:
            a boolean representing 
        """
        return self._running

    @property
    def reim(self):
        """
        Returns the reim instance

        Returns:
            a Reim instance
        """
        return self._reim

    @property
    def enemies(self):
        """
        Returns the enemies list

        Returns:
            a list of Enemy instances
        """
        return self._enemies

    @property
    def bullets(self):
        """
        Returns the bullets list

        Returns:
            a list of ReimBullet instances
        """
        return self._bullets

    @property
    def enemy_bullets(self):
        """
        Returns the enemy_bullets list

        Returns:
            a list of EnemyBullet instances
        """
        return self._enemy_bullets

    def check_boundary(self):
        """
        Check if character hits the boundary
        """

        if self._reim.pos_x > 468:
            self._reim.set_pos_x(468)
        if self._reim.pos_x < 50:
            self._reim.set_pos_x(50)
        if self._reim.pos_y > 528:
            self._reim.set_pos_y(528)
        if self._reim.pos_y < 20:
            self._reim.set_pos_y(20)
        for enemy in self._enemies:
            # Allow enemies to go back and forth through edges
            if enemy.pos_x > 468:
                enemy.set_pos_x(50)
            if enemy.pos_x < 50:
                enemy.set_pos_x(468)
            if enemy.pos_y > 528:
                enemy.set_pos_y(528)
            if enemy.pos_y < 20:
                enemy.set_pos_y(20)

        # Catch occasional ValueError where a bullet has already been deleted
        try:
            # Remove bullets off screen
            for enemy_bullets in self._enemy_bullets:
                if enemy_bullets.pos_y > 534:
                    self._enemy_bullets.remove(enemy_bullets)
                if enemy_bullets.pos_x > 484:
                    self._enemy_bullets.remove(enemy_bullets)
                if enemy_bullets.pos_x < 50:
                    self._enemy_bullets.remove(enemy_bullets)
        except ValueError:
            print("bullet not in list, ignored")
        except:
            print("what else could happen?")

    def enemy_move(self):
        """
        Make the Enemy move in random directions
        """

        for enemy in self._enemies:
            angle = enemy.angle + 1
            speed_y = enemy.speed * sin(angle) * random.randint(30, 40)
            speed_x = enemy.speed * cos(angle) * random.randint(-30, 40)
            enemy.set_pos_y(enemy.pos_y + speed_y)
            enemy.set_pos_x(enemy.pos_x + speed_x)
            enemy.set_angle(angle)

    def enemy_keep_firing(self):
        """
        Make the Enemy keep firing if the game has less than 100 bullets
        """

        if self.running and len(self.enemy_bullets) < self.ENEMY_BULLETS_MAX:
            for enemy in self._enemies:
                temp_bullet = EnemyBullet(enemy._pos_x, enemy._pos_y)
                temp_bullet.update()
                self._enemy_bullets.append(temp_bullet)

    def reim_keep_firing(self):
        """
        Make Reim keep firing
        """
        if self.running and self.reim.z_pressed:
            temp_bullet = ReimBullet(
                # Center bullets
                self._reim._pos_x + 12, self._reim._pos_y + 10)
            temp_bullet.update()
            self._bullets.append(temp_bullet)

    def check_win_condition(self):
        """
        Check if the game ends with a win or loss

        Checks the amount of enemies left in the enemies list and if the player
        has been hit by a bullet
        """
        for bullet in self.bullets:
            for enemy in self._enemies:
                if(find_distance(enemy._pos_x, enemy._pos_y,
                                 bullet._pos_x, bullet._pos_y) < 30):
                    self._enemies.remove(enemy)

        # Win condition
        if len(self._enemies) == 0:
            print("You Won!")
            self.set_running(False)

        # Lose condition
        for enemy_bullet in self._enemy_bullets:
            if(find_distance(self._reim._pos_x, self._reim._pos_y,
                             enemy_bullet._pos_x, enemy_bullet._pos_y) < 8):
                print("You Lost!")
                self.set_running(False)


def find_distance(pos_x_1, pos_y_1, pos_x_2, pos_y_2):
    """
    Find distance between two coordinate sets with euler's

    Args:
        pos_x_1: an int representing the set 1 x coordinate
        pos_y_1: an int representing the set 1 y coordinate
        pos_x_2: an int representing the set 2 x coordinate
        pos_y_2: an int representing the set 2 y coordinate

    Returns:
        a float representing the distance
    """
    delta_x = pos_x_1 - pos_x_2
    delta_y = pos_y_1 - pos_y_2
    return sqrt(delta_x ** 2 + delta_y ** 2)
