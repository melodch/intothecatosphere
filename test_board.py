import pygame as pg
from collections import Counter
import pytest
from board import Board
pg.init()

# Set up a Board instance for testing
test_board = Board()

test_board.reset_groups(0, 9)
# Define sets of test cases.
reset_groups = [
    # Check that score is set to int given.
    (test_board.score, 0),
    # Check that lives is set to int given.
    (test_board.lives, 9),
    # Check that the star list is empty.
    (test_board.Stars, []),
    # Check that the fireball is empty.
    (test_board.Fireballs, []),
    # Check that the platform list is empty.
    (test_board.Platforms, []),
    # Check that the Ladders list is empty.
    (test_board.Ladders, []),
    # Check that the endcaps list is empty.
    (test_board.ReferenceEndcaps, []),
    # Check that the platform references list is empty.
    (test_board.ReferencePlatforms, []),
    # Check that the ladder references list is empty.
    (test_board.ReferenceLadders, []),
]

test_board._make_map()
make_map = [
    # Check that the map height is correct.
    (len(test_board.map), 51),
    # Check that the map width is correct.
    (len(test_board.map[0]), 51),
]

test_board._make_boundaries()
height = len(test_board.map)
width = len(test_board.map[0])
make_boundaries = [
    # Check that the left side of the map is a boundary.
    (0, 4),
    # Check that the right side of the map is a boundary.
    (width - 1, 4),
]

create_fireball = [
    # Check that no more than 3 fireballs are inside
    # that the list is not empty
    (len(test_board.Fireballs), 3),
]

# Set up a new Board instance for testing
test_board2 = Board()
test_board2.update_level(100, 5)
# Define sets of test cases.
update_level = [
    # Check that score is set to int given.
    (test_board2.score, 100),
    # Check that lives is set to int given.
    (test_board2.lives, 5),
]

################################################################################
# Don't change anything below these lines.
################################################################################


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
        assert test_board.map[col][j] == value


@pytest.mark.parametrize("fireball,value",
                         create_fireball)
def test_create_fireball(fireball, value):
    assert fireball <= value


@pytest.mark.parametrize("attribute,value", update_level)
def test_update_level(attribute, value):
    assert attribute == value
