import pygame as pg
import pytest
from board import Board
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

test_game.reset_groups(0, 9)
reset_groups = [
    # Check that score is set to int given.
    (test_game.score, 0),
    # Check that lives is set to int given.
    (test_game.lives, 9),
    # Check that the star list is empty.
    (test_game.Stars, []),
    # Check that the fireball is empty.
    (test_game.Fireballs, []),
    # Check that the platform list is empty.
    (test_game.Platforms, []),
    # Check that the Ladders list is empty.
    (test_game.Ladders, []),
    # Check that the endcaps list is empty.
    (test_game.ReferenceEndcaps, []),
    # Check that the platform references list is empty.
    (test_game.ReferencePlatforms, []),
    # Check that the ladder references list is empty.
    (test_game.ReferenceLadders, []),
]

test_game._make_map()
make_map = [
    # Check that the map height is correct.
    (len(test_game.map), 51),
    # Check that the map width is correct.
    (len(test_game.map[0]), 51),
]

test_game._make_boundaries()
height = len(test_game.map)
width = len(test_game.map[0])
make_boundaries = [
    # Check that the left side of the map is a boundary.
    (0, 4),
    # Check that the right side of the map is a boundary.
    (width - 1, 4),
]

create_fireball = [
    # Check that no more than 3 fireballs are inside
    # that the list is not empty
    (len(test_game.Fireballs), 3),
]

# Set up a new Board instance for testing
test_game2 = Board()
test_game2.update_level(100, 5)
# Define sets of test cases.
update_level = [
    # Check that score is set to int given.
    (test_game2.score, 100),
    # Check that lives is set to int given.
    (test_game2.lives, 5),
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

# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("attribute,value", reset_groups)
def test_reset_groups(attribute, value):
    assert attribute == value


@pytest.mark.parametrize("attribute,length", make_map)
def test_make_map(attribute, length):
    assert attribute == length


@pytest.mark.parametrize("col,value", make_boundaries)
def test_make_boundaries(col, value):
    for j in range(0, height):
        assert test_game.map[col][j] == value


@pytest.mark.parametrize("fireball,value",
                         create_fireball)
def test_create_fireball(fireball, value):
    assert fireball <= value


@pytest.mark.parametrize("attribute,value", update_level)
def test_update_level(attribute, value):
    assert attribute == value


def test_platform_generation():
    for _ in range(10):
        test_game.update_level(0, 0)
        assert test_game.map is not None