from onboard import OnBoard
import pygame as pg


class Platform(OnBoard):
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
        # Using super to call the attributes from the parent OnBoard class.
        pass

    def update_image(self, raw_image):
        """
        Update the platform image.

        Args:
            raw_image: A string representing the path to a png.
        """
        # Update the platform image from the raw image and scale it
        pass
