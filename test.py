from collections import Counter
import pytest
from board import Board

from board import (
    reset_groups,
    initialize_game,
    make_map,           # check is emtpy 2D list
    create_fireball,    # maybe check that there are three fireball objects in Fireballs
    generate_stars,     # maybe check that there are more than two star objects in Stars
    make_boundaries,    # check that map sides are 4
    generate_platforms,     # check levels
    generate_ladders,       # check that there isn't more than two ladders on one level
    create_ladder,          # check spacing
    is_top_reachable,       # check with True board and False board
    traverse_left_right,    # check that it gives the right left right values
    update_level,           # check that things are reset and then score, lives stay the same
)

# ????
test_game = Board()
test_game._width = 50
test_game._height = 50

'''
self.score = score
self.lives = lives
self.map = []
self.Players = Player(pg.image.load('Cat Images/orangefront.png'),
                        (self._width // 2, self._height - 25))
self.Stars = []
self.Platforms = []
self.Fireballs = []
self.Ladders = []
self.ReferencePlatforms = []
self.ReferenceLadders = []
self.ReferenceEndcaps = []
self.ReferenceCats
'''
# Define sets of test cases.
reset_groups = [
    # Check that the complement of A is T.
    (score, []),
    # Check that the complement of C is G.
    ("C", "G"),
    # Check that the complement of G is C.
    ("G", "C"),
    # Check that the complement of T is A.
    ("T", "A")
]

rest_of_orf_cases = [
    # Check a start followed by a stop.
    ("ATGTGA", "ATG"),
    # Check a case without a stop codon.
    ("ATGAAA", "ATGAAA"),
    # Check a case with a stop codon where length is a multiple of 3.
    ("ATGAACGATCCATGA", "ATGAACGATCCA"),
    # Check a case without a stop codon where the length is not a multiple of 3.
    ("ATGA", "ATGA"),
    # Check a case with a stop codon where the length is not a multiple of 3.
    ("ATGAATGA", "ATGAATGA"),
]

find_all_orfs_cases = [
    # This case from find_all_orfs has no ORFs in other frames, so it should
    # return the same result as in the one_frame case.
    ("ATGTAAATGAAATAA", ["ATG", "ATGAAA"]),
    # Check case with ORFs in every frame
    ("ATGGATGCCTGATTGAAATGTGA", ["ATGGATGCC", "ATGCCTGAT", "ATG"]),
]


# Define additional testing lists and functions that check other properties of
# functions in gene_finder.py.
@pytest.mark.parametrize("nucleotide", ["A", "T", "C", "G"])
def test_double_complement(nucleotide):
    """
    Check that taking the complement of a complement of a nucleotide produces
    the original nucleotide.
    Args:
        nucleotide: A single-character string representing one of the four DNA
            nucleotides.
    """
    assert get_complement(get_complement(nucleotide)) == nucleotide


################################################################################
# Don't change anything below these lines.
################################################################################


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("attribute,value", reset_groups)
def test_get_complement(attribute, value):
    test_game.reset_groups(0, 9)
    assert test_game.attribute == value // ??????????


@pytest.mark.parametrize("strand,reverse_complement",
                         get_reverse_complement_cases)
def test_get_reverse_complement(strand, reverse_complement):
    assert get_reverse_complement(strand) == reverse_complement


@pytest.mark.parametrize("strand,rest", rest_of_orf_cases)
def test_rest_of_orf(strand, rest):
    assert rest_of_orf(strand) == rest


@pytest.mark.parametrize("strand,orfs", find_all_orfs_one_frame_cases)
def test_find_all_orfs_oneframe(strand, orfs):
    assert Counter(find_all_orfs_one_frame(strand)) == Counter(orfs)


@pytest.mark.parametrize("strand,orfs", find_all_orfs_cases)
def test_find_all_orfs(strand, orfs):
    assert Counter(find_all_orfs(strand)) == Counter(orfs)


@pytest.mark.parametrize("strand,orfs", find_all_orfs_both_strands_cases)
def test_find_all_orfs_both_strands(strand, orfs):
    assert Counter(find_all_orfs_both_strands(strand)) == Counter(orfs)


@pytest.mark.parametrize("strand,orf", get_longest_orf_cases)
def test_get_longest_orf(strand, orf):
    assert find_longest_orf(strand) == orf


@pytest.mark.parametrize("strand,protein", coding_strand_to_aa_cases)
def test_coding_strand_to_aa(strand, protein):
    assert encode_amino_acids(strand) == protein