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
from reference import ReferencePlatform
from reference import ReferenceLadder
from reference import ReferenceEndcap
from player import ReferenceCat



class Board:
    """
    This class defines our gameboard.
    A gameboard contains everthing related to our game on it
    like our player, platforms, ladders, gems, etc.

    Attributes:
        score: An integer representing how many gems have been collected.
        game_state: An integer that represents the state of the game,
        where 0 is pre-game, 1 is game, and 2 is post-game.
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

        # Create an array map where we can store and keep track of what each
        # block is where 1 represents a platform, 2 ladder, and 3 gem.

        # Initialize empty lists in which we store instances of different game
        # components. Call reset_groups method to reset the above groups and
        # initialize the game.

        # Create the buttons used in the pregame and postgame screens.
        # Initialize font and background for those screens.
        # The buttons used in the pregame and postgame screens
        self.Buttons = [Button(pg.image.load('Object Images/start_meow.png'), (140, 320), "start"),
                        Button(pg.image.load('Object Images/exit_game.png'), (360, 320), "exit"),
                        Button(pg.image.load('Object Images/restart.png'), (250, 343), "Object Images/restart.png"), ]
        self.Active_buttons = [1, 1, 0]  # Pregame screen uses first 2 buttons
        self.myfont = pg.font.Font('slkscr.ttf', 50)

        self.Cat_buttons = [Button(pg.image.load('Cat Images/orangeright.png'), (90, 310), "cat1"),
                        Button(pg.image.load('Cat Images/greyright.png'), (250, 310), "cat2"),
                        Button(pg.image.load('Cat Images/blueright.png'), (410, 310), "cat3"), ]
        self.Chosen_cat = ""

        # Initialize instance groups that are used to display instances on
        # the screen.
        self._width = WIDTH
        self._height = HEIGHT
        self.score = 0
        self.lives = 9
        self.game_state = 0
        self.white = (255, 255, 255)

        # Arrays in which we store our instances of different classes
        self.Players = self.ReferenceLadders = []
        self.Fireballs = self.Gems = self.Platforms = []
        self.Ladders = self.ReferencePlatforms = []
        self.ReferenceEndcaps = []
        self.ReferenceCats = []

        # Initialize instance groups which we use to display instances on screen
        self.player_group = pg.sprite.RenderPlain(self.Players)
        self.platform_group = pg.sprite.RenderPlain(self.Platforms)
        self.gem_group = pg.sprite.RenderPlain(self.Gems)
        #self.board_group = pg.sprite.RenderPlain(self.Boards)
        self.fireball_group = pg.sprite.RenderPlain(self.Fireballs)
        self.ladder_group = pg.sprite.RenderPlain(self.Ladders)
        self.reference_platform_group = pg.sprite.RenderPlain(self.ReferencePlatforms)
        self.reference_ladder_group = pg.sprite.RenderPlain(self.ReferenceLadders)
        self.reference_endcap_group = pg.sprite.RenderPlain(self.ReferenceEndcaps)
        self.reference_cat_group = pg.sprite.RenderPlain(self.ReferenceCats)

        # Resets the above groups and initializes the game for us
        self.reset_groups(0, 9)

        self.background = pg.image.load('Background Images/purplebg.png')  # added image
        self.background = pg.transform.scale(self.background, (WIDTH, HEIGHT))
        self.start_background = pg.image.load('Background Images/startscreen.png')
        self.choose_cat_background = pg.image.load('Background Images/pickcat1.png')
        self.end_background = pg.image.load('Background Images/endscreen.png')
        self.start_background = pg.transform.scale(self.start_background, (WIDTH, HEIGHT))
        self.choose_cat_background = pg.transform.scale(self.choose_cat_background, (WIDTH, HEIGHT))
        self.end_background = pg.transform.scale(self.end_background, (WIDTH, HEIGHT))

    def reset_groups(self, score, lives):
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
        self.score = score
        self.lives = lives
        self.map = []  # We will create the map again when we reset the game
        self.Players = Player(pg.image.load('Cat Images/orangefront.png'),
                              (self._width // 2, self._height - 35))
        self.Gems = []
        self.Platforms = []
        self.Fireballs = []
        self.Ladders = []
        self.ReferencePlatforms = []
        self.ReferenceLadders = []
        self.ReferenceEndcaps = []
        self.ReferenceCats =  ReferenceCat(pg.image.load('Object Images/reference.png'),
                              (self._width // 2, self._height - 35))
        #self.Boards = [OnBoard(pg.image.load('purplebg.png'), (0, 0))]
                       #OnBoard(pg.image.load('purplebg.png'), (685, 480))]
        
        #self.Boards[0].modify_size(self.Boards[0].image, 40, 150)  # Do this on purpose to get a pixelated image
        #self.Boards[0].modify_size(self.Boards[0].image, 500, 500)
        self.initialize_game()  # Initialize game and generate map
        self.create_groups()  # Creates instance groups

    def initialize_game(self):
        """
        Initialize the game by calling the methods to make the map, generate
        platforms, ladders, and gems randomly, populating the map with our
        game components, then creating the groups of those game components.
        """
        while True:
            self.map = []
            self.make_map()
            self.Ladders = self.Platforms = []
            self.ReferenceEndcaps = []
            #self.ReferenceCats = []
            self.generate_platforms()
            self.create_endcap_reference_lines()
            self.generate_ladders()
            if self.are_platforms_reachable(0, 0) is True:
                break
        self.make_boundaries()
        self.create_reference_lines()
        self.generate_gems()
        self.create_groups()

    def create_groups(self):
        """
        Update all the game component groups from their corresponding lists.
        """
        # Here, we use the PyGame Sprite RenderPlain method
        self.reference_cat_group = pg.sprite.RenderPlain(self.ReferenceCats)
        self.platform_group = pg.sprite.RenderPlain(self.Platforms)
        self.gem_group = pg.sprite.RenderPlain(self.Gems)
        #self.board_group = pg.sprite.RenderPlain(self.Boards)
        self.ladder_group = pg.sprite.RenderPlain(self.Ladders)
        self.fireball_group = pg.sprite.RenderPlain(self.Fireballs)
        self.reference_ladder_group = pg.sprite.RenderPlain(self.ReferenceLadders)
        self.reference_platform_group = pg.sprite.RenderPlain(self.ReferencePlatforms)
        self.reference_endcap_group = pg.sprite.RenderPlain(self.ReferenceEndcaps)
        self.player_group = pg.sprite.RenderPlain(self.Players)
        #self.reference_cat_group = pg.sprite.RenderPlain(self.ReferenceCats)

    def create_fireball(self, width):
        """
        Randomly generate fireballs.
        """
        if len(self.Fireballs) < 3:
            #time.sleep(0.5)
            location = (random.randint(5, width),random.randint(-1000,0))
            self.Fireballs.append(Fireball(pg.image.load('fireball2.png'),
                                  location, len(self.Fireballs), -3))
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
                self.game_state = 3
                self.Active_buttons[0] = 0
                self.Active_buttons[1] = 0
                self.Active_buttons[2] = 1
            if fireball.get_position()[1] >= 490:
                self.Fireballs.remove(fireball)
                    # self.Hearts.pop(len(self.Hearts) - 1)

    def generate_gems(self):
        """
        Randomly generate gems (where there is a platform below the gem so
        the player can reach it). Add the gem to map and update gem list.
        """
        width = len(self.map)
        height = len(self.map[0])
        h_spacing = 10
        w_spacing = 5
        offset = -8
        # Traverse the platforms
        for y in range(h_spacing, height, h_spacing):
            for x in range(w_spacing, width, w_spacing):
                rand_gem = random.randint(1, 5)
                if self.map[x][y] == 1 and rand_gem == 1 and \
                   self.map[x - w_spacing][y - 3] != 3:
                    self.map[x][y - 1] = 3
                    self.Gems.append(Gem(pg.image.load('Object Images/yellow star.png'),
                                     (x * 10, (y - 1) * 10 + offset)))
        if len(self.Gems) < 3:  # If less than 3 gems, call function again
            self.generate_gems()

    def generate_platforms(self):
        """
        Randomly generate platforms.
        Add the platform to map and update platforms list.
        """
        height = len(self.map)
        width = len(self.map[0])
        
        # Generate platforms at all levels but the ground
        # Vertically spaced out by 10
        h_spacing = 10

        for i in range(0, width):
            self.map[i][height - 1] = 1
            self.Platforms.append(Platform(pg.image.load('Object Images/platform28.png'), (i * 10 + 10 / 2, (height - 1) * 10 + 10 / 2)))
        
        for y in range(0, height - h_spacing, h_spacing):
            x = 1
            while x < width:
                rand_platform_size = random.randint(7, 15)
                for i in range(rand_platform_size):
                    self.map[x][y] = 1
                    self.Platforms.append(Platform(pg.image.load('Object Images/platform28.png'), (x * 10 + 5, y * 10 + 5)))
                    #self.Platforms[i].modify_size(self.Platforms[i].image, 2, 2)
                    x += 1
                    if x >= width - 1:
                        break
                rand_space = random.randint(7, 15)
                if random.randint(0, 1) == 0:
                    x += rand_space
    
    def generate_ladders(self):
        """
        Randomly generate ladders between two platforms.
        Add the ladder to map and update ladders list.
        """
        height = len(self.map) - 1
        width = len(self.map[0]) - 1
        h_spacing = 10
        w_spacing = 5

        # Loop through each platform level
        for y in range(0, height, h_spacing):
            num_on_this_lvl = 0
            rand_num = random.randint(1, 2)
            while num_on_this_lvl < rand_num:
                for x in range(w_spacing, width, w_spacing):
                    rand_ladder = random.randint(1, 7)
                    if num_on_this_lvl == rand_num:
                        break
                    # If there hasn't already been a ladder placed on this level
                    # If there is a platform on this level and one level lower
                    # Chance of a ladder being placed is 1/5
                    elif self.map[x][y] == self.map[x][y + h_spacing] == rand_ladder == 1 and \
                          self.map[x - w_spacing][y] != 2 and self.map[x + w_spacing][y] != 2:
                        # Call helper method to create a ladder to connect between upper and lower platform
                        self.create_ladder(x, y, y + h_spacing)
                        num_on_this_lvl += 1

    def create_ladder(self, x, upper_y, lower_y):
        """
        Helper method to create a ladder between two platforms.
        """
        for y in range(upper_y, lower_y - 1, 3):
            self.map[x][y] = 2
            self.Ladders.append(Ladder(pg.image.load('Object Images/ladder figure.png'),
                                (x * 10 + 10 / 2, y * 10 + 10)))
        self.map[x][lower_y - 1] = 2
        self.Ladders.append(Ladder(pg.image.load('Object Images/ladder figure.png'),
                            (x * 10 + 10 / 2, (upper_y - 1) * 10 + 10)))

    def are_platforms_reachable(self, x, y):
        height = len(self.map)
        width = len(self.map[0])
        # Base case
        # If reached the other end of the board
        if y == height - 1:
            return True
        next_ladder = self.help_function(x, y)
        if next_ladder[0] != 0 and self.map[next_ladder[0]][y] == 2:
            return self.are_platforms_reachable(next_ladder[0], y + 10)
        if next_ladder[1] != 49 and self.map[next_ladder[1]][y] == 2:
            return self.are_platforms_reachable(next_ladder[1], y + 10)
        else:
            return False
    
    def help_function(self, x, y):
        left = right = x
        while left > 0:
            if self.map[left][y] == 2 or (y > 0 and self.map[left][y] == 0):
                break
            left -= 1
        height = len(self.map)
        while right < height - 2:
            if self.map[right][y] == 2 or (y > 0 and self.map[right][y] == 0):
                break
            right += 1
        return (left, right)

    def create_reference_lines(self):
        ref_image = 'Object Images/reference.png'
        ref_ladder_image = 'Object Images/referenceladder.png'
        for j in range(len(self.map)):
            # print(self.map[j])
            # if 1 in self.map[j]:
            #     for i in range(len(self.map[j])):
            #         self.References.append(Reference(pg.image.load(ref_image),(i* 10, (j - 2) * 10 )))
            for i in range(len(self.map)):
               # for platforms
                if self.map[j][i] == 1:
                    #position = [i,j]                  
                    self.ReferencePlatforms.append(ReferencePlatform(pg.image.load(ref_image),(j* 10, (i-3) * 10 + 2 )))
                    if j != len(self.map) - 1:
                        if self.map[j+1][i] == 0 or self.map[j+1][i] == 4:
                            #for k in range(i, i+6):
                            self.ReferencePlatforms.append(ReferencePlatform(pg.image.load(ref_image),((j+1)* 10, (i - 3) * 10 +5 )))
                            self.ReferencePlatforms.append(ReferencePlatform(pg.image.load(ref_image),((j+2)* 10, (i - 3) * 10 + 5)))
                        if self.map[j-1][i] == 0 or self.map[j-1][i] == 4:
                            self.ReferencePlatforms.append(ReferencePlatform(pg.image.load(ref_image),((j-1)* 10, (i - 3) * 10 +5)))
                            self.ReferencePlatforms.append(ReferencePlatform(pg.image.load(ref_image),((j-2)* 10, (i - 3) * 10 +5)))
                #for ladders
                if self.map[j][i] == 2:
                    self.ReferenceLadders.append(ReferenceLadder(pg.image.load(ref_ladder_image),((j * 10) + 5, ((i+1) * 10) - 30)))

                
    def create_endcap_reference_lines(self):
        ref_ladder_image = 'Object Images/referenceladder.png'
        for j in range(len(self.map)):
            for i in range(len(self.map)):
                if self.map[j][i] == 1:           
                    if j != len(self.map) - 1:
                        if self.map[j+1][i] == 0:
                            for k in range(i + 2, i + 6):
                                self.ReferenceEndcaps.append(ReferenceEndcap(pg.image.load(ref_ladder_image),((j+2)* 10, (k - 3) * 10 + 5 )))
                        if self.map[j-1][i] == 0:
                            for k in range(i + 2, i + 6):
                                self.ReferenceEndcaps.append(ReferenceEndcap(pg.image.load(ref_ladder_image),((j-1)* 10, (k - 3) * 10 + 5 )))
                                #self.ReferencePlatforms.append(ReferencePlatform(pg.image.load('reference.png'),((j+2)* 10, (k - 3) * 10 + 5)))

    # def create_cat_reference_point(self,position):
    #     ref_image = 'Object Images/reference.png'
    #    #position[1] = position[1] + 3
    #     self.ReferenceCats = ReferenceCat(pg.image.load(ref_image),position)

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
        # for i in range(0, width):
        #     self.map[i][height - 1] = 1
        #     self.Platforms.append(Platform(pg.image.load('platform28.png'), (i * 10 + 10 / 2, (height - 1) * 10 + 10 / 2)))
        # Left and right sides
        for j in range(0, height):
            self.map[0][j] = 4
            self.map[width - 1][j] = 4
            # self.Platforms.append(Platform(pg.image.load('lightblueplatform.png'), (- 20, j * 10 + 10 / 2)))
            # self.Platforms.append(Platform(pg.image.load('lightblueplatform.png'), (width * 10 + 20, j * 10 + 10 / 2)))

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
            self.score += 10
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
        if self.Active_buttons[0] == 1 and \
           self.Buttons[0].rect.collidepoint(pg.mouse.get_pos()):
            self.reset_groups(0, 3)
            self.game_state = 1
            self.Active_buttons = [0, 0, 0]
        # If the exit button is pressed
        if self.Active_buttons[1] == 1 and \
           self.Buttons[1].rect.collidepoint(pg.mouse.get_pos()):
            pg.quit()
            sys.exit()
        # If the restart button is pressed
        if self.Active_buttons[2] == 1 and \
           self.Buttons[2].rect.collidepoint(pg.mouse.get_pos()):
            self.game_state = 1

    def select_cat(self):
        if self.Cat_buttons[0].rect.collidepoint(pg.mouse.get_pos()):
            self.Chosen_cat = "orange"
            self.game_state = 2
        if self.Cat_buttons[1].rect.collidepoint(pg.mouse.get_pos()):
            self.Chosen_cat = "grey"
            self.game_state = 2
        if self.Cat_buttons[2].rect.collidepoint(pg.mouse.get_pos()):
            self.Chosen_cat = "blue"
            self.game_state = 2

    def check_button(self):
        """
        Check for mouse hovering over buttons to change their images
        giving a hover button effect.
        """
        mouse_pos = pg.mouse.get_pos()
        for button in range(len(self.Buttons)):
            # Active button
            if self.Active_buttons[button] == 1 and \
               self.Buttons[button].rect.collidepoint(mouse_pos):
                if button == 0:
                    self.Buttons[button].change_image(pg.image.load('Object Images/hov_start_meow.png'))
                elif button == 1:
                    self.Buttons[button].change_image(pg.image.load('Object Images/hov_exit_game.png'))
                elif button == 2:
                    self.Buttons[button].change_image(pg.image.load('Object Images/hov_restart.png'))
            # Inactive button
            else:
                if button == 0:
                    self.Buttons[button].change_image(pg.image.load('Object Images/start_meow.png'))
                elif button == 1:
                    self.Buttons[button].change_image(pg.image.load('Object Images/exit_game.png'))
                elif button == 2:
                    self.Buttons[button].change_image(pg.image.load('Object Images/restart.png'))
        
        for button in range(len(self.Cat_buttons)):
            # Active button
            if self.Cat_buttons[button].rect.collidepoint(mouse_pos):
                if button == 0:
                    self.Cat_buttons[button].change_image(pg.image.load('Cat Images/orangefront.png'))
                elif button == 1:
                    self.Cat_buttons[button].change_image(pg.image.load('Cat Images/greyfront.png'))
                elif button == 2:
                    self.Cat_buttons[button].change_image(pg.image.load('Cat Images/bluefront.png'))
            # Inactive button
            else:
                if button == 0:
                    self.Cat_buttons[button].change_image(pg.image.load('Cat Images/orangeright.png'))
                elif button == 1:
                    self.Cat_buttons[button].change_image(pg.image.load('Cat Images/greyright.png'))
                elif button == 2:
                    self.Cat_buttons[button].change_image(pg.image.load('Cat Images/blueright.png'))

    # changed the syntax of the display screen thing
    def redraw_screen(self, display_screen, score_label, lives_label, width, height):
        """
        Redraws the entire game screen.

        Game states:
        0 Game lobby
        1 Choose cat
        2 Gameplay
        3 End screen

        Args:
            display_screen: PyGame display.
            score_label: rendering of the score.
            width: An integer representing the width of the screen.
            height: An integer representing the height of the screen.
        """
        # Fill display screen with black
        display_screen.fill((0, 0, 0))  # Fill it with black
        # If we are in either pregame or postgame states
        if self.game_state == 0 or self.game_state == 3:
            if self.game_state == 0:
                # Game lobby
                display_screen.blit(self.start_background, self.start_background.get_rect())
            if self.game_state == 3:
                # Post game state
                display_screen.blit(self.end_background, self.end_background.get_rect())
                label = self.myfont.render(str(self.score), 10, (255, 255, 255))
                display_screen.blit(label, (285, 255))

            for button in range(len(self.Active_buttons)):
                if self.Active_buttons[button] == 1:
                    display_screen.blit(self.Buttons[button].image,
                                        self.Buttons[button].get_top_left_pos())

        # If we are choosing a cat
        if self.game_state == 1:
            # Choose cat
            display_screen.blit(self.choose_cat_background, self.choose_cat_background.get_rect())
            for button in range(len(self.Cat_buttons)):
                display_screen.blit(self.Cat_buttons[button].image,
                                     self.Cat_buttons[button].get_top_left_pos())
        
        # If we are in the game state,
        if self.game_state == 2:
            # Draw the background first
            display_screen.blit(self.background, self.background.get_rect())
            # Draw all our groups on the background
            #self.board_group.draw(display_screen)
            self.platform_group.draw(display_screen)
            self.ladder_group.draw(display_screen)
            self.gem_group.draw(display_screen)
            self.player_group.draw(display_screen)
            self.reference_cat_group.draw(display_screen)
            self.fireball_group.draw(display_screen)
            self.reference_platform_group.draw(display_screen)
            self.reference_ladder_group.draw(display_screen)
            self.reference_endcap_group.draw(display_screen)
            

            # Center text on the board
            score_width = score_label.get_width()
            display_screen.blit(score_label, (20, 470))      
            display_screen.blit(lives_label, (400, 470))

    def update_level(self, current_score, current_lives):
        """
        Initialize the game by calling the methods to make the map, generate
        platforms, ladders, and gems randomly, populating the map with our
        game components, then creating the groups of those game components.
        """
        self.reset_groups(current_score, current_lives)
