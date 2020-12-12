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
        super(Platform, self).__init__(raw_image, position)
        self.image = raw_image
        #self.image = pg.transform.scale(self.image, (20, 20))

    
    # def modify_size(self, raw_image, height, width):
    #     """
    #     Scale the raw image.

    #     Args:
    #         raw_image: A string representing the path to a png.
    #         height: An integer representing the height of the object.
    #         width: An integer representing the width o the object.
    #     """   
    #     self.image = raw_image
    #     self.image = pg.transform.scale(self.image, (width, height))

    # def update_image(self, raw_image):
    #     """
    #     Update the platform image.

    #     Args:
    #         raw_image: A string representing the path to a png.
    #     """
    #     # Update the platform image from the raw image and scale it
    #     self.image = raw_image
    #     self.image = pg.transform.scale(self.image, (15, 15))
