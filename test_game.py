import pygame as pg
from collections import Counter
import pytest
from board import Board
from game import Game

pg.init()

test_game = Board()
test_game.reset_groups(0, 9)  # Resets the above groups
test_game.initialize_game()  # Initialize game and generate map
test_game.create_groups()
collisions = test_game.Players.check_collision(
    test_game.ref_platform_group)

check_collision = [
    # checking to see that the cat is colliding with
    # the platform when the game starts
    (collisions, 0),
]

# negative value moves the player to the right
test_game.Players.update_position(
    pg.image.load('Cat Images/orangefront.png'), -10, 'H')
position = test_game.Players.get_position()

update_position_right = [
    # checking to see that the update position method moves
    # the player to the right position
    (position, ((test_game.width // 2) + 10, test_game.height - 25)),
]

test_game.reset_groups(0, 9)  # Resets the above groups
test_game.initialize_game()  # Initialize game and generate map
test_game.create_groups()
test_game.Players.update_position(
    pg.image.load('Cat Images/orangefront.png'), 10, 'V')
position = test_game.Players.get_position()

update_position_up = [
    # checking to see that the update position method moves
    # the player to the right position
    (position, ((test_game.width // 2), test_game.height - 35)),
]


@pytest.mark.parametrize("collision,value",
                         check_collision)
def test_check_collision(collision, value):
    assert len(collisions) > value


@pytest.mark.parametrize("position,value",
                         update_position_right)
def test_update_position_right(position, value):
    assert position == value


@pytest.mark.parametrize("position,value",
                         update_position_up)
def test_update_position_up(position, value):
    assert position == value
