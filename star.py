import pygame as pg
from onboard import OnBoard
from constants import *


class Star(OnBoard):
    """
    Defining all the stars in the game. This class inherits
    from the OnBoard class. The stars increase the player score. SImrun is here.

    Attributes:
        position: A tuple representing the coordinates of a star.
        image: A string representing the path to a png.
        rect: A tuple representing the dimensions of a rectangle.
        value: An integer representing the score value of a star.
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
        super().__init__(raw_image, position)
        self.image = raw_image
        self.image = pg.transform.scale(self.image, (20,20))

    def update_image(self, raw_image):
        """
        Update the star image.

        Args:
            raw_image: A string representing the path to a png.
        """
        self.image = raw_image
        self.image = pg.transform.scale(self.image, (20,20))
