import pygame as pg
from onboard import OnBoard
from constants import *


class Ladder(OnBoard):
    """
    Defining all the ladders in the game.
    """
    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the ladder.
        """
        # Using super to call the attributes from the parent OnBoard class.
        pass

    def update_image(self, raw_image):
        """
        Update the ladder image.

        Args:
            raw_image: A string representing the path to a png.
        """
        # Update the ladder image from the raw image and scale it
        pass
