import pygame
from th_controller import ThController
from th_view import ThView
from th_model import ThGame


def main():
    game = ThGame()
    view = ThView(game)
    controller = ThController(game)
    view.initialize()
    ticks = 0
    while game.running:
        if ticks % 5 == 0:
            game.reim_keep_firing()
        if ticks % 7 == 0:
            game.enemy_move()

        game.enemy_keep_firing()
        game.check_win_condition()
        controller.event_listener()
        game.reim.update()
        for bullet in game.enemy_bullets:
            bullet.update()
        game.check_boundary()
        view.update()
        ticks += 1


if __name__ == "__main__":
    main()
