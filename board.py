import pygame as pg
import math
import random
import sys
from Constants import *
from OnBoard import OnBoard
from Gem import Gem
from Player import Player
from Fireball import Fireball
from Button import Button


class Board:
    """
    This class defines our gameboard.
    A gameboard contains everthing related to our game on it
    like our player, platforms, ladders, gems, etc.

    Attributes:
        score: An integer representing how many gems have been collected.
        game_state: An integer that represents the state of the game,
        where 0 is pre-game, 1 is game, and 2 is post-game.
        direction: An integer that represents the direction that the player is
        facing.
        map: A list of lists representing a 2D array with the positions of the
        game components on screen.
        players: A list of Player instances on screen.
        gems: A list of Gem instances on screen.
        platforms: A list of Platform instances on screen.
        ladders: A list of Ladder instances on screen.
        fireballs: A list of Fireball instances on screen.
        buttons: A list of Button instances that represent on-screen buttons
        to be pressed.
        active_buttons: A list of 0s and 1s that represent which buttons are
        being used on screen.
        fireball_group: A PyGame group that contains Fireball instances.
        player_group: A PyGame group that contains Player instances.
        platform_group: A PyGame group that contains Platform instances.
        ladder_group: A PyGame group that contains Ladder instances.
        gem_group: A PyGame group that contains Gem instances to be displayed.
    """

    def __init__(self):
        """
        Set up a board that connects and initializes all aspects of our game
        as instance variables.
        """
        # Things that are initialized here include:
        # dimensions of board (height and width)
        # score
        # game state
        # direction of playerf

        # Create an array map where we can store and keep track of what each
        # block is where 1 represents a platform, 2 ladder, and 3 gem.

        # Initialize empty lists in which we store instances of different game
        # components. Call reset_groups method to reset the above groups and
        # initialize the game.

        # Create the buttons used in the pregame and postgame screens.
        # Initialize font and background for those screens.

        # Initialize instance groups that are used to display instances on
        # the screen.
        pass

    def reset_groups(self):
        """
        Reset game component groups that tie their respective instances
        together. Component groups include platforms, ladders, gems,
        player and fireballs.
        """
        # Reset score
        # Empty map
        # Populate lists with instances of game components
        # Call initialize_game() method to initialize the game and generate map
        # Call create_groups() method to create instance groups
        pass

    def create_fireball(self):
        """
        Randomly generate fireballs.
        """
        pass

    def generate_gems(self):
        """
        Randomly generate gems (where there is a platform below the coin so
        the player can reach it). Add the coin to map and update coin list.
        """
        pass

    def check_map_for_match(self, x_pos, y_pos, check_no):
        """
        Given a position and check_no (1 for platform, 2 for ladder, 3 for gem),
        return if it's a valid position to place or not.

        Args:
            x_pos: An integer representing the x coordinate.
            y_pos: An integer representing the y coordinate.
            check_no: An integer representing the index of a game component.
        """
        pass

    def make_map(self):
        """
        Create an empty map.
        """
        # Make 2D array filled with zeros
        pass

    def make_boundaries(self):
        """
        Add walls to our map boundaries and also the floor.
        """
        # Update map to have 1s where there are boundaries
        pass

    def make_ladders(self):
        """
        Generate ladders randomly such that they are not
        too close to each other.
        """
        # Update map to have 2s where there are ladders
        pass

    def populate_instance_groups(self):
        """
        Use the 2D map to add instances to the component lists. This is called
        once you have finished making platforms, ladders, and gems on the map.
        """
        # Loop through map
        # Where there is a 1, add platform instance to platform list
        # Where there is a 2, add ladder instance to ladder list
        # Where there is a 3, add gem instance to gem list
        pass

    def ladder_check(self, ladders_collided_below, platforms_collided_below):
        """
        Check if the player is on a ladder or not.

        Args:
            ladders_collided_below: A list of Ladder instances a player
            is in collision with.
            platforms_collided_below: A list of Platform instances a player
            is in collision with.
        """
        pass

    def fireball_check(self):
        """
        Update all the fireball positions and check for collisions with player.
        """
        # Loop through all fireballs
        # Call continuous_update method in Fireball class to
        # updatetheir position
        # Call check_collision method in Fireball class to
        # check for collisions with player
        # If it has hit the player, game over
        pass

    def gem_check(self, gems_collected):
        """
        Perform gem collection by updating score, gem list, and map.
        This method is called if player has collided with a gem.

        Args:
            gems_collected: A list of gem instances that a player has
            collided with.
        """
        # loop through gems in gems_collected
        # call collect_gem method from Gem class
        # update map, gem list, gem group
        pass

    def process_button(self):
        """
        Perform needed actions when a button is clicked.
        """
        pass

    def redraw_screen(self, display_screen, score_label, width, height):
        """
        Redraws the entire game screen.

        Args:
            display_screen: PyGame display.
            score_label: rendering of the score.
            width: An integer representing the width of the screen.
            height: An integer representing the height of the screen.
        """
        # Fill display screen with black
        # Update screen depending on whether we are in pregame, game,
        # or postgame state
        # If we are in the game state, draw the background first
        # Then draw all our game component groups on the background
        pass

    def createGroups(self):
        """
        Update all the game component groups from their corresponding lists.
        """
        # Here, we use the PyGame Sprite RenderPlain method
        pass

    def initializeGame(self):
        """
        Initialize the game by calling the methods to make the map, generate
        platforms, ladders, and gems randomly, populating the map with our
        game components, then creating the groups of those game components.
        """
        pass
