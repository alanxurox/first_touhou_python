import pytest
import th_controller
import th_model
import character
import bullet
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

# Initialization for testing
test_game = th_model.ThGame()

# Check game status


@pytest.mark.parametrize("actual,expected", [
    (test_game._running, True)
])
def test_game_status(actual, expected):
    assert actual == expected

# Check find_distance function


@pytest.mark.parametrize("actual,expected", [
    (th_model.find_distance(1, 1, 5, 4), 5.0),
    (th_model.find_distance(0, 1, 0, -1), 2.0),
    (th_model.find_distance(123, 123, 153, 163), 50.0),
    (th_model.find_distance(-15, -8, 0, 0), 17.0)
])
def test_distance(actual, expected):
    assert actual == expected
