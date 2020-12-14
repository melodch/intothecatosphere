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
        display_screen: PyGame display to view the game
        new_game: new instance of the Board class
        fireball_timer: timer that controls how fast fireballs are generated
        gem_group: group from the Board instance that represent
        gem instances on the screen
        platform_group: group from the Board instance that represent
        platform instances on the screen
        ladder_group: group from the Board instance that represent
        ladder instances on the screen
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
        # constants
        self.FPS = 150
        self.clock = pg.time.Clock()
        self.myFont = pg.font.Font('slkscr.ttf', 20)
        

    def runGame(self):
        """
        Run the main loop that displays the board, gets user input,
        and makes changes to the board.

        Since our game goes on infinitely, we have the code that runs the game
        in a while loop that exits only when the player dies.
        """
        # Display the score on the screen

        # If game state is not 1 then don't run the game,
        # just display menu buttons
        # Check which button was clicked and change game state accordingly
        while True:

            self.clock.tick(self.FPS)
            self.score_label = self.myFont.render("Score " + str(self.new_game.score), 1,
                                                    (0, 0, 0))
            self.lives_label = self.myFont.render("Lives: " + str(self.new_game.lives), 1,
                                                    (0, 0, 0))
            # If the game state is not 2 then we will not have to run the game,
            # we just need to display buttons
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
                self.wallsCollidedAbove = self.new_game.Players.check_collision(self.new_game.platform_group)
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
                image = f'Cat Images/{self.new_game.Chosen_cat}front.png'
                image2 = 'Object Images/referencecat.png'
                #Change this
                if keys[K_RIGHT]:                   

                    reference_collided = self.new_game.Players.check_collision(self.new_game.reference_platform_group)                                       
                    ladders_collided =  self.new_game.Players.check_collision(self.new_game.ladder_group)
                    walls_collided = self.new_game.Players.check_collision(self.new_game.platform_group)
                    image = f'Cat Images/{self.new_game.Chosen_cat}right.png'
                    if self.new_game.Players.get_position()[0] <= self.width:
                        if reference_collided != []:
                            self.new_game.Players.update_position(pg.image.load(image), -self.new_game.Players.get_speed(), 'H')
                            x= self.new_game.Players.get_position()
                            # print(x)                 
                            self.new_game.ReferenceCats.update_position_cat(pg.image.load(image2),x) 
                        
                        if walls_collided == [] and ladders_collided == []:
                            self.new_game.Players.update_position(pg.image.load(image), -self.new_game.Players.get_speed(), 'H')
                            self.new_game.ReferenceCats.update_position(pg.image.load(image2), -self.new_game.Players.get_speed(), 'H') 
                if keys[K_LEFT]:                 


                    reference_collided = self.new_game.Players.check_collision(self.new_game.reference_platform_group)                 
                    ladders_collided =  self.new_game.Players.check_collision(self.new_game.ladder_group)
                    walls_collided = self.new_game.Players.check_collision(self.new_game.platform_group)
                    
                    image = f'Cat Images/{self.new_game.Chosen_cat}left.png'
                    if reference_collided != [] and self.new_game.Players.get_position()[0] >= 0:                        
                        self.new_game.Players.update_position(pg.image.load(image), self.new_game.Players.get_speed(), 'H')
                        self.new_game.ReferenceCats.update_position(pg.image.load(image2), self.new_game.Players.get_speed(), 'H')
                    
                    if walls_collided == [] and ladders_collided == [] and self.new_game.Players.get_position()[0] >= 0:
                            self.new_game.Players.update_position(pg.image.load(image), self.new_game.Players.get_speed(), 'H')
                            self.new_game.ReferenceCats.update_position(pg.image.load(image2), self.new_game.Players.get_speed(), 'H')

                if keys[K_DOWN]:                   

                    image = f'Cat Images/{self.new_game.Chosen_cat}front.png'
                    self.new_game.Players.update_position(pg.image.load(image), -5,'V')
                    self.new_game.ReferenceCats.update_position(pg.image.load(image2), -5,'V')                    
                    references_collided_down = self.new_game.Players.check_collision(self.new_game.reference_ladder_group)
                    self.new_game.Players.update_position(pg.image.load(image), 5,'V')
                    self.new_game.ReferenceCats.update_position(pg.image.load(image2), 5,'V')
                    
                    if references_collided_down != [] and self.new_game.Players.get_position()[1] <= self.height + 10:
                        self.new_game.Players.update_position(pg.image.load(image), -self.new_game.Players.get_speed(),'V')
                        self.new_game.ReferenceCats.update_position(pg.image.load(image2), -self.new_game.Players.get_speed(),'V')           


                if keys[K_UP]:                    
                    image = f'Cat Images/{self.new_game.Chosen_cat}up.png'
                    references_collided = self.new_game.Players.check_collision(self.new_game.reference_ladder_group)
                    if references_collided != [] and self.new_game.Players.get_position()[1] >= 0:
                        self.new_game.Players.update_position(pg.image.load(image), self.new_game.Players.get_speed(),'V')
                        self.new_game.ReferenceCats.update_position(pg.image.load(image2), self.new_game.Players.get_speed(),'V')
                    # If the player has reached the tope of the screen, update level
                    if self.new_game.Players.get_position()[1] <= 30:
                        self.new_game.update_level(self.new_game.score, self.new_game.lives)

                               
                reference_ladders_collided = self.new_game.Players.check_collision(self.new_game.reference_ladder_group)
                self.new_game.Players.update_position(pg.image.load(image), -5,'V')    
                self.new_game.ReferenceCats.update_position(pg.image.load(image2), -5,'V')               
                walls_collided_down = self.new_game.Players.check_collision(self.new_game.platform_group)
                self.new_game.Players.update_position(pg.image.load(image), 5,'V')
                self.new_game.ReferenceCats.update_position(pg.image.load(image2), 5,'V')
                reference_ends_collided = self.new_game.Players.check_collision(self.new_game.reference_endcap_group)

                if reference_ladders_collided == [] and walls_collided_down == [] and self.new_game.Players.get_position()[1] <= self.height - 10:
                    self.new_game.Players.update_position(pg.image.load(image), -self.new_game.Players.get_speed()*1.2,'V')
                    self.new_game.ReferenceCats.update_position(pg.image.load(image2), -self.new_game.Players.get_speed()*1.2,'V')
                    if reference_ends_collided:
                        self.new_game.Players.update_position(pg.image.load(image), -2,'H')                    
                        walls_collided_right = self.new_game.Players.check_collision(self.new_game.platform_group)
                        self.new_game.Players.update_position(pg.image.load(image), 2,'H')

                        self.new_game.Players.update_position(pg.image.load(image), 2,'H')                    
                        walls_collided_left = self.new_game.Players.check_collision(self.new_game.platform_group)
                        self.new_game.Players.update_position(pg.image.load(image), -2,'H')

                        if walls_collided_right:
                            self.new_game.Players.update_position(pg.image.load(image), 10,'H')
                            self.new_game.ReferenceCats.update_position(pg.image.load(image2), 10,'H')
                        if walls_collided_left:
                            self.new_game.Players.update_position(pg.image.load(image), -10,'H')
                            self.new_game.ReferenceCats.update_position(pg.image.load(image2), -10,'H')
                
                # Use cycles to animate the stars
                self.new_game.cycles = (self.new_game.cycles + 1) % 48
                if self.new_game.cycles >= 1 and self.new_game.cycles <= 8:
                    for gem in self.new_game.Gems:
                        gem.update_image(pg.image.load('Object Images/yellow star.png'))
                elif self.new_game.cycles >= 9 and self.new_game.cycles <= 16:
                    for gem in self.new_game.Gems:
                        gem.update_image(pg.image.load('Object Images/star_rot1.png'))
                elif self.new_game.cycles >= 17 and self.new_game.cycles <= 24:
                    for gem in self.new_game.Gems:
                        gem.update_image(pg.image.load('Object Images/star_rot2.png'))
                elif self.new_game.cycles >= 25 and self.new_game.cycles <= 32:
                    for gem in self.new_game.Gems:
                        gem.update_image(pg.image.load('Object Images/star_rot3.png'))
                elif self.new_game.cycles >= 33 and self.new_game.cycles <= 40:
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
