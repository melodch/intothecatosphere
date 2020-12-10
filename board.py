import pygame as pg
import math
import random
import sys
import time
from constants import *
from onboard import OnBoard
from gem import Gem
from player import Player
from fireball import Fireball
from button import Button
from platform import Platform
from ladder import Ladder


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
        # The buttons used in the pregame and postgame screens
        self.Buttons = [Button(pg.image.load('start.png'), (150, 300), "start"),
                        Button(pg.image.load('exit.png'), (350, 300), "exit"),
                        Button(pg.image.load('restart.png'), (150, 300), "restart"), ]
        self.ActiveButtons = [1, 1, 0]  # Pregame screen uses first 2 buttons
        self.myfont = pg.font.SysFont("comicsansms", 50)

        # Initialize instance groups that are used to display instances on
        # the screen.
        self._width = WIDTH
        self._height = HEIGHT
        self.score = 0
        self.lives = 3
        self.gameState = 0
        self.direction = 0
        self.white = (255, 255, 255)

        self.map = []
        # Arrays in which we store our instances of different classes
        self.Players = None
        self.Fireballs = self.Gems = self.Platforms = []
        self.Boards = self.Ladders = self.References = []

        # Resets the above groups and initializes the game for us
        self.reset_groups()

        self.background = pg.image.load('board.png')  # added image
        self.background = pg.transform.scale(self.background, (WIDTH, HEIGHT))
        self.startbackground = pg.image.load('start_bg.png')
        self.startbackground = pg.transform.scale(self.startbackground,
                                                  (WIDTH, HEIGHT))

        # Initialize instance groups which we use to display instances on screen
        self.player_group = pg.sprite.RenderPlain(self.Players)
        self.platform_group = pg.sprite.RenderPlain(self.Platforms)
        self.gem_group = pg.sprite.RenderPlain(self.Gems)
        self.board_group = pg.sprite.RenderPlain(self.Boards)
        self.fireball_group = pg.sprite.RenderPlain(self.Fireballs)
        self.ladder_group = pg.sprite.RenderPlain(self.Ladders)
        self.reference_group = pg.sprite.RenderPlain(self.References)

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
        self.lives = 3
        self.map = []  # We will create the map again when we reset the game
        self.Players = Player(pg.image.load('player.png'),
                              (self._width // 2, self._height - 5))
        self.Gems = []
        self.Platforms = []
        self.Fireballs = []
        self.Ladders = []
        self.Refereces = []
        self.Boards = [OnBoard(pg.image.load('board.png'), (200, 480)),
                       OnBoard(pg.image.load('board.png'), (685, 480))]
        # self.Boards[0].modifySize(self.Boards[0].image, 40, 150)  # Do this on purpose to get a pixelated image
        # self.Boards[1].modifySize(self.Boards[1].image, 40, 150)
        self.initialize_game()  # Initialize game and generate map
        self.create_groups()  # Creates instance groups

    def create_fireball(self, width):
        """
        Randomly generate fireballs.
        """

        if len(self.Fireballs) < 3:
            #time.sleep(0.5)
            location = (random.randint(5, width),random.randint(-1000,0))
            self.Fireballs.append(Fireball(pg.image.load('fireball.png'),
                                  location, len(self.Fireballs), -1))
            self.create_groups()

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
        for fireball in self.fireball_group:
            fireball.continuous_update(self.player_group)
            if fireball.check_collision(self.player_group):
                # if len(self.Hearts) >= 2:  # Reduce the player's life by 1
                self.Fireballs.remove(fireball)
                self.lives -= 1
                self.create_groups()
            if self.lives == 0:
                self.gameState = 2
            if fireball.get_position()[1] >= 490:
                self.Fireballs.remove(fireball)
                    # self.Hearts.pop(len(self.Hearts) - 1)

    # def render_fog(self, display_screen):
    #     """
    #     Render the fog around the player. There will be a gradient circle
    #     around the Sprite that the player will be able to see.
    #     """
    #     # Draw circles around the Sprite that get darker as they get further away.
    #     # for i in range(1000, 1, -1):
    #     #    pg.draw.circle(display_screen, (0, 0, 0, 0), self.Players.get_position(), i+100, width=2)

    #     # screen = pg.display.set_mode(display_screen, 0, 32)
    #     screen = pg.display.set_mode((self._width, self._height), 0, 32)
    #     # Fill the screen with white
    #     screen.fill((255, 255, 255))
    #     # Make a black surface the size of the display
    #     fog_of_war = pg.Surface(display_screen) UNCOMMENT LATER
    #     fog_of_war.fill((0, 0, 0))
    #     # Make a gray circle on top of the black surface
    #     pg.draw.circle(fog_of_war, (60, 60, 60), self.Players.get_position(), 100, 0)
    #     # Set the transparent colorkey to gray
    #     # Using this method (if it works), we can a
    #     # gradient using different grays
    #     fog_of_war.set_colorkey((60, 60, 60))
    #     screen.blit(fog_of_war, (0, 0))
    #     pg.display.update()

    def generate_gems(self):
        """
        Randomly generate gems (where there is a platform below the gem so
        the player can reach it). Add the gem to map and update gem list.
        """
        width = len(self.map)
        height = len(self.map[0])
        h_spacing = 5
        # Traverse the platforms
        for y in range(10, height, 10):
            for x in range(h_spacing, width, h_spacing):
                rand_gem = random.randint(1, 5)
                if self.map[x][y] == 1 and rand_gem == 1 and \
                   self.map[x - h_spacing][y - 3] != 3:
                    # print("x,y check: ", x - h_spacing, y - 3)
                    self.map[x][y - 3] = 3
                    # print("x, y: ", x, y - 3)
                    self.Gems.append(Gem(pg.image.load('gem.png'),
                                     (x * 10 + 10 / 2, (y - 3) * 10 + 10 / 2)))
        if len(self.Gems) <= 3:  # If less than 3 gems, call function again
            self.generate_gems()

    def generate_platforms(self):
        """
        Randomly generate platforms.
        Add the platform to map and update platforms list.
        """
        width = len(self.map)
        height = len(self.map[0])
        # Generate platforms at all levels but the ground
        # Vertically spaced out by 10
        for y in range(0, height - 10, 10):
            x = 1
            while x < width:
                rand_platform_size = random.randint(7, 15)
                for _ in range(rand_platform_size):
                    self.map[x][y] = 1
                    self.Platforms.append(Platform(pg.image.load('platform.png'), (x * 10 + 5, y * 10 + 5)))
                    x += 1
                    if x >= width - 1:
                        break
                rand_space = random.randint(7, 15)
                if random.randint(0, 1) == 0:
                    x += rand_space
    
    def generate_reference_lines(self):
        for platform in self.platform_group:
            position = platform.get_position()
            

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
        for _ in range(0, self._height // 10 + 1):
            row = []
            for _ in range(0, self._width // 10 + 1):
                row.append(0)
            self.map.append(row)

    def make_boundaries(self):
        """
        Add boundaries to the four sides of our map.
        """
        height = len(self.map)
        width = len(self.map[0])
        
        # Bottom floor
        for i in range(0, height):
            self.map[i][width - 1] = 1
            self.Platforms.append(Platform(pg.image.load('platform.png'), (i * 10 + 10 / 2, width * 10 + 10 / 2)))
        # Left and right sides
        for j in range(0, width):
            self.map[0][j] = 1
            self.map[height - 1][j] = 1
            self.Platforms.append(Platform(pg.image.load('platform.png'), (- 20, j * 10 + 10 / 2)))
            self.Platforms.append(Platform(pg.image.load('platform.png'), (height * 10 + 15, j * 10 + 10 / 2)))
    
    def generate_ladders(self):
        height = len(self.map) - 1
        width = len(self.map[0]) - 1
        print("gen ladd height: ", height)
        h_spacing = 5
        # Loop through each platform level
        for y in range(0, height, 10):
            num_on_this_lvl = 0
            rand_num = random.randint(1, 2)
            print('ran')
            while num_on_this_lvl < rand_num:
                for x in range(5, width, h_spacing):
                    rand_ladder = random.randint(1, 5)
                    if num_on_this_lvl == rand_num:
                        break
                    # If there hasn't already been a ladder placed on this level
                    # If there is a platform on this level and one level lower
                    # Chance of a ladder being placed is 1/5
                    elif self.map[x][y] == 1 and self.map[x][y + 10] == 1 and rand_ladder == 1 and \
                    self.map[x - h_spacing][y] != 2 and self.map[x + h_spacing][y] != 2:
                        # Call helper method to create a ladder to connect between upper and lower platform
                        print("x, y: ", x, y, height)
                        self.create_ladder(x, y, y + 10)
                        print('here')
                        num_on_this_lvl += 1

                
    # def place_ladder(self, x, y, h_spacing, rand_ladder):
    #     if self.map[x][y] == self.map[x][y + 10] == rand_ladder == 1 and self.map[x - h_spacing][y] != 2 and self.map[x + h_spacing][y] != 2:
    #         # if self.map[x][y - 10] != 2 and self.map[x][y + 10] != 2:
    #         return True
    #     return False

    def create_ladder(self, x, upper_y, lower_y):
        for y in range(upper_y, lower_y, 2):
            self.map[x][y] = 2
            self.Ladders.append(Ladder(pg.image.load('ladder.png'),
                                (x * 10 + 10 / 2, y * 10 + 10 / 2)))

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
                #     Add a ladder at that position
                #     self.Ladders.append(OnBoard(pygame.image.load('ladder.png'), (y * 15 + 15 / 2, x * 15 + 15 / 2)))
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
            # self.map[(gem.get_position()[1]) // 10][(gem.get_position()[0]) // 10] = 0
            # Remove the coin entry from our list
            self.Gems.remove(gem)
            # Update the coin group since we modified the coin list
            self.create_groups()

    def process_button(self):
        """
        Perform needed actions when a button is clicked.
        """
        # If the start button is pressed
        if self.ActiveButtons[0] == 1 and \
           self.Buttons[0].rect.collidepoint(pg.mouse.get_pos()):
            self.reset_groups()
            self.gameState = 1
            self.ActiveButtons[0] = 0
            self.ActiveButtons[1] = 0
            self.ActiveButtons[2] = 0
        # If the exit button is pressed
        if self.ActiveButtons[1] == 1 and \
           self.Buttons[1].rect.collidepoint(pg.mouse.get_pos()):
            pg.quit()
            sys.exit()
        # If the restart button is pressed
        if self.ActiveButtons[2] == 1 and \
           self.Buttons[2].rect.collidepoint(pg.mouse.get_pos()):
            self.gameState = 0
            self.ActiveButtons[0] = 1
            self.ActiveButtons[1] = 1
            self.ActiveButtons[2] = 0

    def check_button(self):
        """
        Check for mouse hovering over buttons to change their images
        giving a hover button effect.
        """
        mouse_pos = pg.mouse.get_pos()
        for button in range(len(self.Buttons)):
            # Active button
            if self.ActiveButtons[button] == 1 and \
               self.Buttons[button].rect.collidepoint(mouse_pos):
                if button == 0:
                    self.Buttons[button].change_image(pg.image.load('start1.png'))
                elif button == 1:
                    self.Buttons[button].change_image(pg.image.load('exit1.png'))
                elif button == 2:
                    self.Buttons[button].change_image(pg.image.load('restart1.png'))
            # Inactive button
            else:
                if button == 0:
                    self.Buttons[button].change_image(pg.image.load('start.png'))
                elif button == 1:
                    self.Buttons[button].change_image(pg.image.load('exit.png'))
                elif button == 2:
                    self.Buttons[button].change_image(pg.image.load('restart.png'))

    # changed the syntax of the display screen thing
    def redraw_screen(self, display_screen, score_label, lives_label, width, height):
        """
        Redraws the entire game screen.

        Args:
            display_screen: PyGame display.
            score_label: rendering of the score.
            width: An integer representing the width of the screen.
            height: An integer representing the height of the screen.
        """
        # Fill display screen with black
        display_screen.fill((0, 0, 0))  # Fill it with black
        # If we are in either pregame or postgame states
        if self.gameState != 1:
            display_screen.blit(self.startbackground, self.startbackground.get_rect())
            if self.gameState == 0:
                # Pregame state
                # display_screen.blit(pg.image.load('Assets/donkeykongtext.png'), (340, 50))
                pass
            if self.gameState == 2:
                # Post game state
                label = self.myfont.render("Your score is " + str(self.score),
                                           1, (255, 255, 255))
                display_screen.blit(label, (410, 70))
            for button in range(len(self.ActiveButtons)):
                if self.ActiveButtons[button] == 1:
                    display_screen.blit(self.Buttons[button].image,
                                        self.Buttons[button].get_top_left_pos())
        # If we are in the game state,
        if self.gameState == 1:
            # Draw the background first
            display_screen.blit(self.background, self.background.get_rect())
            # Draw all our groups on the background
            self.board_group.draw(display_screen)
            self.platform_group.draw(display_screen)
            self.gem_group.draw(display_screen)
            self.player_group.draw(display_screen)
            self.ladder_group.draw(display_screen)
            self.fireball_group.draw(display_screen)
            # Fill the screen with a fog
            #self.render_fog(display_screen)

            # Center text on the board
            score_width = score_label.get_width()
            display_screen.blit(score_label, (265 - score_width / 2, 470))      
            display_screen.blit(lives_label, (470, 470))

    def create_groups(self):
        """
        Update all the game component groups from their corresponding lists.
        """
        # Here, we use the PyGame Sprite RenderPlain method
        self.player_group = pg.sprite.RenderPlain(self.Players)
        self.platform_group = pg.sprite.RenderPlain(self.Platforms)
        self.gem_group = pg.sprite.RenderPlain(self.Gems)
        self.board_group = pg.sprite.RenderPlain(self.Boards)
        self.ladder_group = pg.sprite.RenderPlain(self.Ladders)
        self.fireball_group = pg.sprite.RenderPlain(self.Fireballs)

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
        self.generate_ladders()
        self.create_groups()
