import pygame as pg
import sys
from Board import Board
from Constants import *


class Game:
    """
    This class defines the logic of the game and how player input is taken etc
    We run one instance of this class at the start of the game, and this
    instance manages the game for us.

    Attributes:
        display_screen: PyGame display to view the game
        new_game: new instance of the Board class
        fireball_timer: timer that controls how fast fireballs are generated
        gem_group: group from the Board instance that represent
        gem instances on the screen
        platform_group: group from the Board instance that represent
        platform instances on the screen
        ladder_group: group from the Board instance that represent
        ladder instances on the screen
    """

    def __init__(self):
        """
        Set up a game that creates a new Board instance and assigns groups
        from this instance to the group attributes. Initialize the rest of the
        instance attributes.
        """
        pass

    def runGame(self):
        """
        Run the main loop that displays the board, gets user input,
        and makes changes to the board.

        Since our game goes on infinitely, we have the code that runs the game
        in a while loop that exits only when the player dies.
        """
        # Display the score on the screen

        # If game state is not 1 then don't run the game,
        # just display menu buttons
        # Check which button was clicked and change game state accordingly

        # If game state is 1 then run the game:
        # Get the appropriate groups
        # Create fireballs
        # Check for collisions below
        # Check for collisions above
        # Set the on_ladder state of the player

        # In a PyGame event loop, check which key is being pressed:

        # If QUIT, exit to desktop

        # If KEYDOWN,
        # If quit key pressed:
        # We quit the game and go to the restart screen

        # If up key pressed and player is on a ladder:
        # Set the player to move up

        # Update the player's position
        # Check which key is being pressed, update position accordingly
        # Redraw all instances onto the screen
        # Update the fireball and check for collisions with player
        # Check for coin collection
        # Update the display to view changes
        pass
