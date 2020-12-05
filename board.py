import pygame as pg
import math
import random
import sys
from constants import *
from onboard import OnBoard
from gem import Gem
from player import Player
from fireball import Fireball
from button import Button
from platform import Platform

class Board:
    """
    This class defines our gameboard.
    A gameboard contains everthing related to our game on it
    like our player, platforms, ladders, gems, etc.

    Attributes:
        score: An integer representing how many gems have been collected.
        game_state: An integer that represents the state of the game,
        where 0 is pre-game, 1 is game, and 2 is post-game.
        direction: An integer that represents the direction that the player is
        facing.
        map: A list of lists representing a 2D array with the positions of the
        game components on screen.
        players: A list of Player instances on screen.
        gems: A list of Gem instances on screen.
        platforms: A list of Platform instances on screen.
        ladders: A list of Ladder instances on screen.
        fireballs: A list of Fireball instances on screen.
        buttons: A list of Button instances that represent on-screen buttons
        to be pressed.
        active_buttons: A list of 0s and 1s that represent which buttons are
        being used on screen.
        fireball_group: A PyGame group that contains Fireball instances.
        player_group: A PyGame group that contains Player instances.
        platform_group: A PyGame group that contains Platform instances.
        ladder_group: A PyGame group that contains Ladder instances.
        gem_group: A PyGame group that contains Gem instances to be displayed.
    """

    def __init__(self):
        """
        Set up a board that connects and initializes all aspects of our game
        as instance variables.
        """
        # Things that are initialized here include:
        # dimensions of board (height and width)
        # score
        # game state
        # direction of playerf

        # Create an array map where we can store and keep track of what each
        # block is where 1 represents a platform, 2 ladder, and 3 gem.

        # Initialize empty lists in which we store instances of different game
        # components. Call reset_groups method to reset the above groups and
        # initialize the game.

        # Create the buttons used in the pregame and postgame screens.
        # Initialize font and background for those screens.

        # Initialize instance groups that are used to display instances on
        # the screen.
        self.__width = 500 #constants.width
        self.__height = 500 #constants.height
        self.score = 0
        self.direction = 0
        self.white = (255, 255, 255)
        

        self.map = []
        # These are the arrays in which we store our instances of different classes
        self.Players = self.Gems = self.Platforms = self.Boards = []

        # Resets the above groups and initializes the game for us
        self.reset_groups()

        self.background = pg.image.load('board.png') #added image
        self.background = pg.transform.scale(self.background, (width, height))

        # Initialize the instance groups which we use to display our instances on the screen
        self.player_group = pg.sprite.RenderPlain(self.Players)
        self.platform_group = pg.sprite.RenderPlain(self.Platforms)
        self.gem_group = pg.sprite.RenderPlain(self.Gems)
        self.board_group = pg.sprite.RenderPlain(self.Boards)

    def reset_groups(self):
        """
        Reset game component groups that tie their respective instances
        together. Component groups include platforms, ladders, gems,
        player and fireballs.
        """
        # Reset score
        # Empty map
        # Populate lists with instances of game components
        # Call initialize_game() method to initialize the game and generate map
        # Call create_groups() method to create instance groups
        self.score = 0
        self.map = []  # We will create the map again when we reset the game
        self.Players = [Player(pg.image.load('player.png'), (self.__width // 2, self.__height - 20))]
        self.Gems = []
        self.Platforms = []
        self.Boards = [OnBoard(pg.image.load('board.png'), (200, 480)),
                       OnBoard(pg.image.load('board.png'), (685, 480))]
        #self.Boards[0].modifySize(self.Boards[0].image, 40, 150)  # Do this on purpose to get a pixelated image
        #self.Boards[1].modifySize(self.Boards[1].image, 40, 150)
        self.initialize_game()  # This initializes the game and generates our map
        self.create_groups()  # This creates the instance groups

    def create_fireball(self):
        """
        Randomly generate fireballs.
        """
        pass

    def generate_gems(self):
        """
        Randomly generate gems (where there is a platform below the coin so
        the player can reach it). Add the coin to map and update coin list.
        """
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 0 and ((i + 1 < len(self.map) and self.map[i + 1][j] == 1) or (
                            i + 2 < len(self.map) and self.map[i + 2][j] == 1)):
                    randNumber = math.floor(random.random() * 1000)
                    if randNumber % 35 == 0 and len(self.Gems) <= 9:  # At max there will be 10 gems in map
                        self.map[i][j] = 3
                        # Check if there is a platform below where the gem is to be placed
                        if j - 1 >= 0 and self.map[i][j - 1] == 3:
                            self.map[i][j] = 0
                        if self.map[i][j] == 3:
                            # Add the gem to our gem list
                            self.Gems.append(Gem(pg.image.load('gem.png'), (j * 10 + 10 / 2, i * 10 + 10 / 2)))
        if len(self.Gems) <= 5:  # If there are less than 6 gem, we call the function again
            self.generate_gems()
    
    def generate_platforms(self):
        """
        Randomly generate platforms. Add the platform to map and update platforms list.
        """
        height = self.__height // 10
        width = self.__width // 10
        for y in range(5, height, 10):
            x = 1
            while x < width - 1:
                rand_platform_size = random.randint(4, 7)
                for _ in range(rand_platform_size):
                    self.map[x][y] = 3
                    self.Platforms.append(Platform(pg.image.load('platform.png'), (x * 10 + 10 / 2, y * 10 + 10 / 2)))
                    x += 1
                    if x == width - 1:
                        break
                rand_space = random.randint(10, 15)
                x += rand_space

    def check_map_for_match(self, x_pos, y_pos, check_no):
        """
        Given a position and check_no (1 for platform, 2 for ladder, 3 for gem),
        return if it's a valid position to place or not.

        Args:
            x_pos: An integer representing the x coordinate.
            y_pos: An integer representing the y coordinate.
            check_no: An integer representing the index of a game component.
        """
        pass

    def make_map(self):
        """
        Create an empty map.
        """
        # Make 2D array filled with zeros
        for _ in range(0, self.__height // 10 + 1):
            row = []
            for _ in range(0, self.__width // 10):
                row.append(0)
            self.map.append(row)

    def make_boundaries(self):
        """
        Add boundaries to the four sides of our map.
        """
        # Update map to have 1s where there are boundaries
        # Left and right sides
        for row in range(self.__height // 10):
            self.map[row][0] = 1
            self.map[row][(self.__width// 10) -1 ] = 1
        # Top and bottom sides
        for col in range(self.__width // 10):
            self.map[0][col] = 1
            self.map[(self.__height// 10) -1][col] = 1

    def make_ladders(self):
        """
        Generate ladders randomly such that they are not
        too close to each other.
        """
        # Update map to have 2s where there are ladders
        pass

    def populate_instance_groups(self):
        """
        Use the 2D map to add instances to the component lists. This is called
        once you have finished making platforms, ladders, and gems on the map.
        """
        # Loop through map
        # Where there is a 1, add platform instance to platform list
        # Where there is a 2, add ladder instance to ladder list
        # for x in range(len(self.map)):
        #     for y in range(len(self.map[x])):
                # if self.map[x][y] == 2:
                #     # Add a ladder at that position
                #     self.Ladders.append(OnBoard(pygame.image.load('Assets/ladder.png'), (y * 15 + 15 / 2, x * 15 + 15 / 2)))
        pass

    def ladder_check(self, ladders_collided_below, platforms_collided_below):
        """
        Check if the player is on a ladder or not.

        Args:
            ladders_collided_below: A list of Ladder instances a player
            is in collision with.
            platforms_collided_below: A list of Platform instances a player
            is in collision with.
        """
        pass

    def fireball_check(self):
        """
        Update all the fireball positions and check for collisions with player.
        """
        # Loop through all fireballs
        # Call continuous_update method in Fireball class to
        # updatetheir position
        # Call check_collision method in Fireball class to
        # check for collisions with player
        # If it has hit the player, game over
        pass

    def gem_check(self, gems_collected):
        """
        Perform gem collection by updating score, gem list, and map.
        This method is called if player has collided with a gem.

        Args:
            gems_collected: A list of gem instances that a player has
            collided with.
        """
        # loop through gems in gems_collected
        # call collect_gem method from Gem class
        # update map, gem list, gem group
        for gem in gems_collected:
            self.score += 1
            # We also remove the coin entry from our map
            #self.map[(gem.get_position()[1]) // 10][(gem.get_position()[0]) // 10] = 0
            # Remove the coin entry from our list
            self.Gems.remove(gem)
            # Update the coin group since we modified the coin list
            self.create_groups()

    def process_button(self):
        """
        Perform needed actions when a button is clicked.
        """
        pass
    # changed the syntax of the display screen thing
    def redraw_screen(self, displayScreen, score_label, width, height):
        """
        Redraws the entire game screen.

        Args:
            display_screen: PyGame display.
            score_label: rendering of the score.
            width: An integer representing the width of the screen.
            height: An integer representing the height of the screen.
        """
        # Fill display screen with black
        # Update screen depending on whether we are in pregame, game,
        # or postgame state
        # If we are in the game state, draw the background first
        # Then draw all our game component groups on the background
        displayScreen.fill((0, 0, 0))  # Fill it with black
        # Draw the background first
        displayScreen.blit(self.background, self.background.get_rect())
        # Draw all our groups on the background
        self.board_group.draw(displayScreen)
        self.platform_group.draw(displayScreen)
        self.gem_group.draw(displayScreen)
        self.player_group.draw(displayScreen)
        
        
        
        displayScreen.blit(score_label, (265-score_label.get_width()/2, 470)) #Center the text on the board

    def create_groups(self):
        """
        Update all the game component groups from their corresponding lists.
        """
        # Here, we use the PyGame Sprite RenderPlain method
        self.player_group = pg.sprite.RenderPlain(self.Players)
        self.platform_group = pg.sprite.RenderPlain(self.Platforms)
        self.gem_group = pg.sprite.RenderPlain(self.Gems)
        self.board_group = pg.sprite.RenderPlain(self.Boards)

    def initialize_game(self):
        """
        Initialize the game by calling the methods to make the map, generate
        platforms, ladders, and gems randomly, populating the map with our
        game components, then creating the groups of those game components.
        """
        self.make_map()
        self.make_boundaries()
        self.generate_platforms()
        self.generate_gems()
        self.populate_instance_groups()
        self.create_groups()
