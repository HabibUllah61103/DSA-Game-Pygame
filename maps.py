# Import pygame module
import pygame as pg
# Import system module
import sys

# Set the value of _ as false
_ = False

# Create a matrix to represent the map
# 1 represents the wall
# _ represents the empty space
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 1, 1, 1, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, 1, 1, 1, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Maps:
    """Class to create the map"""
    def __init__(self, game) -> None:
        """Initialize the map"""

        # Set the game as an attribute of the map
        self.game = game
        # Set the mini_map as an attribute of the map
        self.mini_map = mini_map
        # Create a dictionary to create the map from the mini_map
        self.world_map = {}
        # Call the get_map method
        self.get_map()

    def get_map(self):
        """Method to create the map from the mini_map"""

        # Enumerate loop through the mini_map
        for j, row in enumerate(self.mini_map):
            # Enumerate loop through the row
            for i, value in enumerate(row):
                # If the value is not 0
                if value:
                    # Write the coordinates of the wall in the world_map
                    # Add the position and the value to the world_map
                    self.world_map[(i, j)] = value

    def draw(self):
        """Method to draw the map"""

        # Iterate over the world map, draw each element of the map as an unfilled element.
        [pg.draw.rect(self.game.screen, 'grey', (pos[0] * 100, pos[1] * 100, 100, 100), 2) for pos in
         self.world_map.keys()]
