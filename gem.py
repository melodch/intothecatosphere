import pygame as pg
from OnBoard import OnBoard
from Constants import *


class Gem(OnBoard):
    """
    Defining all the gems in the game. This class inherits
    from the OnBoard class. The gems increase the player score.

    Attributes:
        position: A tuple representing the coordinates of a gem.
        image: A string representing the path to a png.
        rect: A tuple representing the dimensions of a rectangle.
        value: An integer representing the score value of a gem.
    """

    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes.

        Args:
            raw_image: A ladder image file.
            position: A tuple representing coordinates of
            the position.
        """
        # using super to call the attributes from the parent OnBoard class.
        # initializing the value attribute as some integer.
        pass

    def update_image(self, raw_image):
        """
        Update the gem image.

        Args:
            raw_image: A string representing the path to a png.
        """

        # Update the gem image from the raw image and scale it
        pass
