import pygame as pg
import random
import math
from onboard import OnBoard
from constants import *


class Fireball(OnBoard):
    """
    Creates all the fireballs for the board that
        fall down the screen. Checks whether the player collides
        with these fireballs or not. This class inherits from the
        OnBoard parent class.

        Attributes:
            position: The position of the image
            image: The image file for that object
            index: A number that uniquely identifies every fireball
            speed: The speed of the fireball
            fall: A 0 for if the fireball is not falling and a 1 if it is.
    """

    def __init__(self, raw_image, position, index, speed):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing coordinates of
            the position.
            index: An integer that uniquely identifies each fireball
            speed: An integer that sets the speed of the fireball.
        """
        # Using super to get the image and position attributes from the
        # parent OnBoard class
        # Initializing an attribute for index based on the input argument
        # Initializing the attribute for fall to be at 0 so the fireball
        # is not falling initially.
        # Initializing the attribute for speed as the input argument.
        pass

    def update_image(self, raw_image):
        """Updating the fireball image

        Args:
            raw_image: A fireball image file

        """
        # Update the fireball image from the raw image and scale it.
        pass

    # Getting and setting variables
    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_fall(self):
        return self.fall

    def update(self, raw_image, speed):
        """
        Moving the fireball downwards in the based on an input value.

        Attributes:
            raw_image: A fireball image file
            speed: The speed at which the fireball moves.
        """
        # Move the fireball in the required direction with
        # the required value and also set the image of the fireball
        pass

    def check_collision(self, colliderGroup):
        """
        Checking to see if the fireball collides with the player.

        Args:
            The group that the fireball is colliding with

        Returns:
            Colliders: True or False based on whether the fireball collides with
            the colliderGroup or not.
        """
        # uses the pygame sprite collider to check if there is a collison
        # between the sprite and the player.

        # return Colliders
        pass

    def continuous_update(self):
        """
        Continously updating the fireball.
        """
        # Set the fireball as falling
        # Update the position of the fireball
        # If there is a colllision, then set the fireball as not colliding
        pass
