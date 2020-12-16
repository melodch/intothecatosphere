import pygame as pg
from collections import Counter
import pytest
from board import Board
pg.init() 
# from board import (
#     reset_groups,
#     initialize_game,
#     make_map,           # check is emtpy 2D list
#     create_fireball,    # maybe check that there are three fireball objects in Fireballs
#     generate_stars,     # maybe check that there are more than two star objects in Stars
#     make_boundaries,    # check that map sides are 4
#     generate_platforms,     # check levels
#     generate_ladders,       # check that there isn't more than two ladders on one level
#     create_ladder,          # check spacing
#     is_top_reachable,       # check with True board and False board
#     traverse_left_right,    # check that it gives the right left right values
#     update_level,           # check that things are reset and then score, lives stay the same
# )

# Set up a Board instance for testing
test_game = Board()
# test_game._width = 50
# test_game._height = 50
# test_game.h_spacing = 3

# Define sets of test cases.
reset_groups = [
    # Check that score is set to int given.
    (test_game.score, 0),
    # Check that lives is set to int given.
    (test_game.lives, 9),
    # Check that the map is empty.
    (test_game.map, []),
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

# rest_of_orf_cases = [
#     # Check a start followed by a stop.
#     ("ATGTGA", "ATG"),
#     # Check a case without a stop codon.
#     ("ATGAAA", "ATGAAA"),
#     # Check a case with a stop codon where length is a multiple of 3.
#     ("ATGAACGATCCATGA", "ATGAACGATCCA"),
#     # Check a case without a stop codon where the length is not a multiple of 3.
#     ("ATGA", "ATGA"),
#     # Check a case with a stop codon where the length is not a multiple of 3.
#     ("ATGAATGA", "ATGAATGA"),
# ]

# is_top_reachable = [
#     # This case from find_all_orfs has no ORFs in other frames, so it should
#     # return the same result as in the one_frame case.
#     ([[]], True),
#     # Check case with ORFs in every frame
#     ("ATGGATGCCTGATTGAAATGTGA", False),
# ]



################################################################################
# Don't change anything below these lines.
################################################################################


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("attribute,value", reset_groups)
def test_reset_groups(attribute, value):
    test_game.reset_groups(0, 9)
    assert attribute == value


# @pytest.mark.parametrize("attribute,value",
#                          initialize_game)
# def test_initialize_game(attribute, value):
#     test_game.initialize_game()
#     assert initialize_game == value


# @pytest.mark.parametrize("strand,rest", rest_of_orf_cases)
# def test_rest_of_orf(strand, rest):
#     assert rest_of_orf(strand) == rest


# @pytest.mark.parametrize("strand,orfs", find_all_orfs_one_frame_cases)
# def test_find_all_orfs_oneframe(strand, orfs):
#     assert Counter(find_all_orfs_one_frame(strand)) == Counter(orfs)


# @pytest.mark.parametrize("strand,orfs", find_all_orfs_cases)
# def test_find_all_orfs(strand, orfs):
#     assert Counter(find_all_orfs(strand)) == Counter(orfs)


# @pytest.mark.parametrize("strand,orfs", find_all_orfs_both_strands_cases)
# def test_find_all_orfs_both_strands(strand, orfs):
#     assert Counter(find_all_orfs_both_strands(strand)) == Counter(orfs)


# @pytest.mark.parametrize("strand,orf", get_longest_orf_cases)
# def test_get_longest_orf(strand, orf):
#     assert find_longest_orf(strand) == orf


# @pytest.mark.parametrize("strand,protein", coding_strand_to_aa_cases)
# def test_coding_strand_to_aa(strand, protein):
#     assert encode_amino_acids(strand) == protein