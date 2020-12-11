from onboard import OnBoard
import pygame as pg


class Reference(OnBoard):
    """
    Defining all the platforms in the game.
    """
    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the platform.
        """
        # boundary problem will fix if the lines are bigger
        super(Reference, self).__init__(raw_image, position)
