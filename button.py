from constants import *


class Button:
    """
    Creating a class that defines all the buttons that will
    be used in the game. Each button has a position and an
    image.

    Attributes:
        position: A tuple representing coordinates.
        image: A string representing the path to a png.
        rect: A tuple representing the dimensions of an image.
        name: A string that represents the name of a button
    """

    def __init__(self, raw_image, position, name):
        """
        Initialize the image, position, name and rect instance attributes.

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing coordinates of the position.
            name: A string representing the name of the button.

        """
        # Initialize attributes for the image, position and name
        # Sets the rect attribute to be the image
        # Sets the center of the rect atrribute as the position
        self.image = raw_image
        self._position = position
        self.rect = self.image.get_rect()
        self.rect.center = self._position
        self.name = name  # Set the name of the button with a string

    def changeImage(self, raw_image):
        """
        Updating the buttons image as the input image

        Args:
            raw_image: A string representing the path to a png.
        """
        self.image = raw_image

    def get_top_left_pos(self):
        """
        Return a tuple representing the coordinates of the top left
        corner of a button.
        """
        return (self._position[0] - self.rect.width / 2, self._position[1] - self.rect.height / 2)

    # Getters and Setters
    def get_position(self):
        """
        Get the position of a button.
        """
        return self._position

    def set_position(self, position):
        """
        Set the position of a button.
        """
        self._position = position
