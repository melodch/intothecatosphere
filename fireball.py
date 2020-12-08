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
        super(Fireball,self).__init__(raw_image, position)
        self.index = index
        #The newly spawned fireball is not falling
        self._fall = 0
        #The speed of a fireball is set
        self._speed = speed
        pass


    # Getting and setting variables
    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_fall(self):
        return self._fall

    def update(self, raw_image, speed):
        """
        Moving the fireball downwards in the based on an input value.

        Attributes:
            raw_image: A fireball image file
            speed: The speed at which the fireball moves.
        """
        # Move the fireball in the required direction with
        # the required value and also set the image of the fireball        
        self.setPosition((self.getPosition()[0], self.getPosition()[1] + speed))
        self.rect.center = self.getPosition()

    def check_collision(self, collider_group):
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
        self.update(self.image, self.__speed)  # Bottom collision
        colliders = pg.sprite.spritecollide(self, collider_group, True)

    def continuous_update(self,collider_group):
        """
        Continously updating the fireball.
        """
        # Set the fireball as falling
        # Update the position of the fireball
        # If there is a colllision, then set the fireball as not colliding
        if self._fall == 1:
        #We move the fireball downwards with speed of self.__speed
            self.update(self.image, self.__speed)
            if self.check_collision(collider_group):
                #We have collided with a wall below, so the fireball can stop falling
                self._fall = 0
