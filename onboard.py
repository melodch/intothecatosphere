import pygame as pg
from constants import *


class OnBoard(pg.sprite.Sprite):
    """
    Creating an overarching class that defines all the inanimate
    objects in the game like the ladder and the gems. This class
    will set up the position and image from all the inherited
    classes.

    Attributes:
        position: A tuple representing coordinates.
        image: A string representing the path to a png.
        rect: A tuple representing the dimensions of an image.
    """

    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes.

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing coordinates of the position.
        """

        # create attributes for the image and the position
        # sets the rect attribute to be the image
        # sets the center of the rect atrribute as the position
        super(OnBoard, self).__init__()
        self._position = position
        self.image = raw_image
        self.rect = self.image.get_rect()
        self.rect.center = self._position
        


    # def modify_size(self, raw_image, height, width):
    #     """
    #     Scale the raw image.

    #     Args:
    #         raw_image: A string representing the path to a png.
    #         height: An integer representing the height of the object.
    #         width: An integer representing the width o the object.
    #     """

    #     # Scale the raw image to a standard size.
    #     pass

    # Getters and Setters
    def set_center(self, position):
        """
        Set the center of the object.
        """
        self.rect.center = position

    def get_position(self):
        """
        Get the position of the object.
        """
        return self._position

    def set_position(self, position):
        """
        Set the position of the object.
        """
        self._position = position
