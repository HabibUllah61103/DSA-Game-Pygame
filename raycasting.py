# Import pygame module
import pygame as pg
# Import math module
import math
# Import everything from setting module
from setting import *


class RayCasting:
    """Class to create the ray casting"""

    def __init__(self, game) -> None:
        """Initialize the ray casting"""

        # Set the game as an attribute of the ray casting
        self.game = game

    def ray_cast(self):
        """Method to cast the rays"""

        # Set the position of the player on the map by converting the player's position to integer
        ox, oy = self.game.player.pos
        # Set the position of the tile player is standing on by converting the player's position to integer
        x_map, y_map = self.game.player.map_pos
        # Calculate the angle of first ray by subtracting the half of the field of view from the player's angle
        # Add 0.0001 to avoid the division by zero error
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001

        # Loop through the number of rays
        for ray in range(NUM_RAYS):
            # Calculate the sine angle of the current ray
            sin_a = math.sin(ray_angle)
            # Calculate the cosine angle of the current ray
            cos_a = math.cos(ray_angle)

            # FOR HORIZONTAL INTERSECTION
            # Calculate the y position of the horizontal intersection and the change in y position of the ray
            # If the sine angle of the current ray is greater than 0, then the y position of the horizontal intersection is 1 greater than the y position of the tile player is standing on
            # If the sine angle of the current ray is less than 0, then the y position of the horizontal intersection is 1 less than the y position of the tile player is standing on
            # If the sine angle of the current ray is greater than 0, then the change in y position of the ray is 1
            # If the sine angle of the current ray is less than 0, then the change in y position of the ray is -1
            # For negative sine angle, subtract 0.0001 to avoid the division by zero error
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - (1e-6), -1)
            # Calculate the depth of the horizontal intersection by dividing the difference between the y position of the tile player is standing on and the y position of the horizontal intersection by the sine angle of the current ray
            depth_hor = (y_hor - oy) / sin_a
            # Calculate the x position of the horizontal intersection by multiplying the depth of the horizontal intersection to the cosine angle of the current ray and adding it to the x position of the tile player is standing on
            x_hor = ox + depth_hor * cos_a
            # Calculate the change in depth of the ray by dividing the change in y position of the ray by the sine angle of the current ray
            delta_depth = dy / sin_a
            # Calculate the change in x position of the ray by multiplying the change in depth of the ray to the cosine angle of the current ray
            dx = delta_depth * cos_a

            # Loop through the maximum depth of the ray
            for i in range(MAX_DEPTH):
                # Set the tile position of the horizontal intersection by converting the x position and y position of the horizontal intersection to integer
                tile_hor = int(x_hor), int(y_hor)
                # Check if the tile position of the horizontal intersection is in the world map
                if tile_hor in self.game.map.world_map:
                    # Break the loop
                    break
                # Add the change in x position of the ray to the x position of the horizontal intersection
                x_hor += dx
                # Add the change in y position of the ray to the y position of the horizontal intersection
                y_hor += dy
                # Add the change in depth of the ray to the depth of the horizontal intersection
                depth_hor += delta_depth

            # FOR VERTICAL INTERSECTION
            # Calculate the x position of the vertical intersection and the change in x position of the ray
            # If the cosine angle of the current ray is greater than 0, then the x position of the vertical intersection is 1 greater than the x position of the tile player is standing on
            # If the cosine angle of the current ray is less than 0, then the x position of the vertical intersection is 1 less than the x position of the tile player is standing on
            # If the cosine angle of the current ray is greater than 0, then the change in x position of the ray is 1
            # If the cosine angle of the current ray is less than 0, then the change in x position of the ray is -1
            # For negative cosine angle, subtract 0.0001 to avoid the division by zero error
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - (1e-6), -1)
            # Calculate the depth of the vertical intersection by dividing the difference between the x position of the vertical intersection and the x position of the player by the cosine angle of the current ray
            depth_vert = (x_vert - ox) / cos_a
            # Calculate the y position of the vertical intersection by multiplying the depth of the vertical intersection to the sine angle of the current ray and adding it to the y position of the player
            y_vert = oy + depth_vert * sin_a
            # Calculate the change in depth of the ray by dividing the change in x position of the ray by the cosine angle of the current ray
            delta_depth = dx / cos_a
            # Calculate the change in y position of the ray by multiplying the change in depth of the ray to the sine angle of the current ray
            dy = delta_depth * sin_a

            # Loop through the maximum depth of the ray
            for i in range(MAX_DEPTH):
                # Set the tile of the vertical intersection by converting the x and y position of the vertical intersection to integer
                tile_vert = int(x_vert), int(y_vert)
                # Check if the tile position of the vertical intersection is in the world map
                if tile_vert in self.game.map.world_map:
                    # Break the loop
                    break
                # Add the change in x position of the ray to the x position of the vertical intersection
                x_vert += dx
                # Add the change in y position of the ray to the y position of the vertical intersection
                y_vert += dy
                # Add the change in depth of the ray to the depth of the vertical intersection
                depth_vert += delta_depth

            # FOR DEPTH CALCULATION
            # Check if the depth of the horizontal intersection is less than the depth of the vertical intersection
            if depth_vert < depth_hor:
                # Set the depth of the ray to the depth of the horizontal intersection
                depth = depth_vert
            # Else
            else:
                # Set the depth of the ray to the depth of the vertical intersection
                depth = depth_hor

            # DRAW THE RAYS FOR THE PURPOSE OF DEBUGGING
            # Draw the ray from the player to the intersection point as a line
            pg.draw.line(self.game.screen, 'YELLOW', (ox * 100, oy * 100),
                         (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a), 2)
            # Increase the ray angle by the delta angle
            ray_angle += DELTA_ANGLE

    def update(self):
        """Method to update the ray casting"""

        # Call the ray_cast method to cast the rays
        self.ray_cast()
