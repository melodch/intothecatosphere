import pygame as pg
import sys
from board import Board
from constants import *

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONUP,
)


class Game:
    """
    This class defines the logic of the game and how player input is taken etc
    We run one instance of this class at the start of the game, and this
    instance manages the game for us.

    Attributes:
        width: An integer that represents the width of the display screen.
        height: An integer that represents the height of the display screen.
        display_screen: A PyGame display to view the game.
        new_game: A new instance of the Board class.
        fps: 
        clock: 
        my_font: Loaded font used to display text on screen.
    """

    def __init__(self):
        """
        Set up a game that creates a new Board instance and assigns groups
        from this instance to the group attributes. Initialize the rest of the
        instance attributes.
        """
        self.width = WIDTH
        self.height = HEIGHT
        self.display_screen = pg.display.set_mode((self.width, self.height))
        self.new_game = Board()
        self.fps = FPS
        self.clock = pg.time.Clock()
        self.my_font = pg.font.Font('slkscr.ttf', 20)

    def runGame(self):
        """
        Run the main loop that displays the board, gets user input,
        and makes changes to the board.

        Since our game goes on infinitely, we have the code that runs the game
        in a while loop that exits only when the player dies.
        """
        

        # If game state is not 1 then don't run the game,
        # just display menu buttons
        # Check which button was clicked and change game state accordingly
        while True:

            self.clock.tick(self.fps)
            # Display the score and lives on the screen
            self.score_label = self.my_font.render("Score " + str(self.new_game.score), 1,
                                                    (0, 0, 0))
            self.lives_label = self.my_font.render("Lives: " + str(self.new_game.lives), 1,
                                                    (0, 0, 0))
            
            # If the game state is not 2 then redraw screen which will only display buttons
            if self.new_game.game_state != 2:

                self.new_game.redraw_screen(self.display_screen, self.score_label, self.lives_label, self.width,
                                          self.height)  # Redraws the buttons onto the screen
                self.new_game.check_button()  # Checks the buttons for hover effects

                for event in pg.event.get():
                    # Exit to desktop
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

                    if event.type == pg.MOUSEBUTTONUP:
                        # Check which button was clicked and change game state accordingly
                        if self.new_game.game_state == 1:
                            self.new_game.select_cat()
                        else:
                            self.new_game.process_button()
                        # Assign groups again

            # If game state is 2 then run the game:
            if self.new_game.game_state == 2:
                self.gem_group = self.new_game.gem_group

                # Get the appropriate groups
                # Create fireballs
                self.new_game.create_fireball(self.width)                
                #self.new_game.reference_cat_group.draw(display_screen)
                # Check for collisions below
                # Check for collisions above
                #self.new_game.Players[0].updateY(-2)
                self.wallsCollidedAbove = self.new_game.ReferenceCats.check_collision(self.new_game.platform_group)
                #self.new_game.Players[0].updateY(2)
                # Set the on_ladder state of the player

                # In a PyGame event loop, check which key is being pressed:
                for event in pg.event.get():
                    # Exit to desktop
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

                # If QUIT, exit to desktop

                # If KEYDOWN,
                # If quit key pressed:
                # We quit the game and go to the restart screen

                # If up key pressed and player is on a ladder:
                # Set the player to move up

                # Update the player's position
                #self.new_game.Players[0].continuousUpdate(self.new_game.platform_group, self.ladder_group)
                keys = pg.key.get_pressed()

                # put catfacefront here/ defualt image when no key is being pressed
                image = f'Cats/{self.new_game.Chosen_cat}front.png'
                image2 = 'Object Images/referencecat.png'
                #Change this
                if keys[K_RIGHT]:                   

                    reference_collided = self.new_game.ReferenceCats.check_collision(self.new_game.reference_platform_group) 
                    #print(reference_collided)                                      
                    reference_ladders_collided =  self.new_game.Players.check_collision(self.new_game.reference_ladder_group)
                    ladders_collided =  self.new_game.ReferenceCats.check_collision(self.new_game.ladder_group)
                    walls_collided = self.new_game.ReferenceCats.check_collision(self.new_game.platform_group)
                    image = f'Cats/{self.new_game.Chosen_cat}right.png'
                    if self.new_game.Players.get_position()[0] <= self.width - 5:
                        if reference_collided != []:
                            #print(reference_collided)
                            self.new_game.Players.update_position(pg.image.load(image), -self.new_game.Players.get_speed(), 'H')
                            # x= self.new_game.Players.get_position()
                            # print(x)                 
                            self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position()) 

                        if ladders_collided == [] and reference_ladders_collided != []:
                            self.new_game.Players.update_position(pg.image.load(image), -self.new_game.Players.get_speed(), 'H')
                            self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position()) 
                        
                        if walls_collided == [] and ladders_collided == []:
                            self.new_game.Players.update_position(pg.image.load(image), -self.new_game.Players.get_speed(), 'H')
                            self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position())  
                if keys[K_LEFT]:                 


                    reference_collided = self.new_game.ReferenceCats.check_collision(self.new_game.reference_platform_group)                 
                    reference_ladders_collided =  self.new_game.Players.check_collision(self.new_game.reference_ladder_group)
                    ladders_collided =  self.new_game.ReferenceCats.check_collision(self.new_game.ladder_group)
                    walls_collided = self.new_game.ReferenceCats.check_collision(self.new_game.platform_group)
                    
                    image = f'Cats/{self.new_game.Chosen_cat}left.png'
                    if reference_collided != [] and self.new_game.Players.get_position()[0] >= 5:                        
                        self.new_game.Players.update_position(pg.image.load(image), self.new_game.Players.get_speed(), 'H')
                        self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position())

                    if ladders_collided == [] and reference_ladders_collided != []:
                            self.new_game.Players.update_position(pg.image.load(image), self.new_game.Players.get_speed(), 'H')
                            self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position())  
                    
                    if walls_collided == [] and ladders_collided == [] and self.new_game.Players.get_position()[0] >= 5:
                            self.new_game.Players.update_position(pg.image.load(image), self.new_game.Players.get_speed(), 'H')
                            self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position()) 

                if keys[K_DOWN]:                   

                    image = f'Cats/{self.new_game.Chosen_cat}front.png'
                    self.new_game.Players.update_position(pg.image.load(image), -5,'V')
                    self.new_game.ReferenceCats.update_position(pg.image.load(image2), -5,'V')                    
                    references_collided_down = self.new_game.ReferenceCats.check_collision(self.new_game.reference_ladder_group)
                    self.new_game.Players.update_position(pg.image.load(image), 5,'V')
                    self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position()) 
                    
                    if references_collided_down != [] and self.new_game.Players.get_position()[1] <= self.height + 10:
                        self.new_game.Players.update_position(pg.image.load(image), -self.new_game.Players.get_speed(),'V')
                        self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position())           


                if keys[K_UP]:                    
                    image = f'Cats/{self.new_game.Chosen_cat}up.png'
                    reference_up_collided = self.new_game.ReferenceCats.check_collision(self.new_game.reference_ladder_group)
                    #print(reference_up_collided)
                    if reference_up_collided != []:# and self.new_game.Players.get_position()[1] >= 0:
                        #print('here')
                        self.new_game.Players.update_position(pg.image.load(image), self.new_game.Players.get_speed(),'V')
                        self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position()) 
                    # If the player has reached the tope of the screen, update level
                    if self.new_game.Players.get_position()[1] <= 30:
                        self.new_game.update_level(self.new_game.score, self.new_game.lives)

                               
                reference_ladders_collided = self.new_game.ReferenceCats.check_collision(self.new_game.ladder_group)
                #print(reference_ladders_collided)
                self.new_game.Players.update_position(pg.image.load(image), -5,'V')  
                self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position())               
                walls_collided_down = self.new_game.ReferenceCats.check_collision(self.new_game.platform_group)
                #print(walls_collided_down)
                self.new_game.Players.update_position(pg.image.load(image), 5,'V')
                self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position()) 
                reference_ends_collided = self.new_game.ReferenceCats.check_collision(self.new_game.reference_endcap_group)

                if reference_ladders_collided == [] and walls_collided_down == [] and self.new_game.Players.get_position()[1] <= self.height - 10:
                    #print('here')
                    self.new_game.Players.update_position(pg.image.load(image), -self.new_game.Players.get_speed()*1.2,'V')
                    self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position()) 
                if reference_ends_collided:
                    self.new_game.Players.update_position(pg.image.load(image), -2,'H')
                    self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position())                  
                    walls_collided_right = self.new_game.ReferenceCats.check_collision(self.new_game.platform_group)
                    self.new_game.Players.update_position(pg.image.load(image), 2,'H')
                    self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position())

                    self.new_game.Players.update_position(pg.image.load(image), 2,'H')
                    self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position())                   
                    walls_collided_left = self.new_game.ReferenceCats.check_collision(self.new_game.platform_group)
                    self.new_game.Players.update_position(pg.image.load(image), -2,'H')
                    self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position())

                    if walls_collided_right:
                        self.new_game.Players.update_position(pg.image.load(image), 10,'H')
                        self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position()) 
                    if walls_collided_left:
                        self.new_game.Players.update_position(pg.image.load(image), -10,'H')
                        self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),self.new_game.Players.get_position()) 
                
                # Use cycles to animate the stars
                # Decrease cycle_rate to decrease the speed of star animation
                cycle_rate = 48
                cycle = cycle_rate / 6
                self.new_game.cycles = (self.new_game.cycles + 1) % cycle_rate
                if self.new_game.cycles >= 1 and self.new_game.cycles <= cycle:
                    for gem in self.new_game.Gems:
                        gem.update_image(pg.image.load('Object Images/yellow star.png'))
                elif self.new_game.cycles >= cycle + 1 and self.new_game.cycles <= cycle * 2:
                    for gem in self.new_game.Gems:
                        gem.update_image(pg.image.load('Object Images/star_rot1.png'))
                elif self.new_game.cycles >= cycle * 2 + 1 and self.new_game.cycles <= cycle * 3:
                    for gem in self.new_game.Gems:
                        gem.update_image(pg.image.load('Object Images/star_rot2.png'))
                elif self.new_game.cycles >= cycle * 3 + 1 and self.new_game.cycles <= cycle * 4:
                    for gem in self.new_game.Gems:
                        gem.update_image(pg.image.load('Object Images/star_rot3.png'))
                elif self.new_game.cycles >= cycle * 4 + 1 and self.new_game.cycles <= cycle * 5:
                    for gem in self.new_game.Gems:
                        gem.update_image(pg.image.load('Object Images/star_rot4.png'))
                else:
                    for gem in self.new_game.Gems:
                        gem.update_image(pg.image.load('Object Images/star_rot5.png'))

                # Redraw all instances onto the screen
                self.new_game.redraw_screen(self.display_screen,
                                            self.score_label,self.lives_label,
                                            self.width, self.height)

                # Update the fireball and check for collisions with player.
                self.new_game.fireball_check()

                # Check for gem collection
                gems_collected = pg.sprite.spritecollide(self.new_game.Players,
                                                         self.gem_group, True)
                self.new_game.gem_check(gems_collected)
                #self.ReferenceCats = []
            # Update the display to view changes
            pg.display.update()
