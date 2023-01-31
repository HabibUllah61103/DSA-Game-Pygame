# Import the pygame module
import pygame as pg
# Import the system module
import sys
# Import everything from setting.py file
from setting import *
# Import everything from maps.py file
from maps import *
# Import everything from player.py file
from player import *
# Import everything from raycasting.py file
from raycasting import *


class Game:
    """Main class of the game"""
    def __init__(self) -> None:
        """Initialize the game"""

        # Initialize pygame
        pg.init()
        # Create the screen of resolution described in setting.py
        self.screen = pg.display.set_mode(RES)
        # Create the clock to set frame rate
        self.clock = pg.time.Clock()
        # Set the delta time
        self.delta_time = 1
        # Call the new_game method
        self.new_game()

    def new_game(self):
        # Create the map
        self.map = Maps(self)
        # Create the player
        self.player = Player(self)
        # Create the ray casting
        self.ray_casting = RayCasting(self)

    def update(self):
        """Method to update the game"""

        # Call the update method to update the movement of the player
        self.player.update()
        # Call the update method to update the ray casting
        self.ray_casting.update()
        # Update the screen
        pg.display.flip()
        # Set the frame rate
        self.clock.tick(FPS)
        # Set the delta time using the frame rate
        self.delta_time = self.clock.tick(FPS)
        # Display the frame rate
        pg.display.set_caption(f"FPS: {self.clock.get_fps():.2f}") 

    def draw(self):
        """Method to draw the game"""

        # Fill the screen with black color at each frame
        self.screen.fill('BLACK')
        # Draw the map by calling the draw method of the map
        self.map.draw()
        # Draw the player by calling the draw method of the player
        self.player.draw()

    def check_events(self):
        """Method to check the events of the game"""

        # Check the events by looping through the event queue
        for event in pg.event.get():
            # Check if the event is QUIT or if the event is KEYDOWN and the key is ESCAPE
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                # Quit the game
                pg.quit()
                # Quit the program
                sys.exit()

    def run(self):
        """Method to run the game"""

        # Main loop of the game
        while True:
            # Check the events
            self.check_events()
            # Update the game
            self.update()
            # Draw the game
            self.draw()

# Check if the file is the main file
if __name__ == "__main__":
    # Create the game
    game = Game()
    # Run the game
    game.run()
