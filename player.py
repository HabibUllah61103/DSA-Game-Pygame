# Import everything from the setting module
from setting import *
# Import pygame module
import pygame as pg
# Import math module
import math


class Player:
    """Class to create the player"""

    def __init__(self, game) -> None:
        """Initialize the player"""

        # Set the game as an attribute of the player
        self.game = game
        # Set the initial position of the player
        self.x, self.y = PLAYER_POS
        # Set the initial angle of the player
        self.angle = PLAYER_ANGLE

    def move(self):
        """Method to move the player"""

        # Calculate the sine angle from the player's direction
        sin_a = math.sin(self.angle)
        # Calculate the cosine angle from the player's direction
        cos_a = math.cos(self.angle)
        # Set the change in x and y direction to 0
        dx, dy = 0, 0
        # Set the speed of the player which is independent of the frame rate
        speed = PLAYER_SPEED * self.game.delta_time
        # Set the speed of the player in the x direction
        speed_sin = speed * sin_a
        # Set the speed of the player in the y direction
        speed_cos = speed * cos_a

        # Get the information of the keys pressed
        keys = pg.key.get_pressed()
        # Check if the "w" key is pressed
        if keys[pg.K_w]:
            # Increase the change in x direction of the player
            dx += speed_cos
            # Increase the change in y direction of the player
            dy += speed_sin
        # Check if the "s" key is pressed
        if keys[pg.K_s]:
            # Decrease the change in x direction of the player
            dx -= speed_cos
            # Decrease the change in y direction of the player
            dy -= speed_sin
        # Check if the "a" key is pressed
        if keys[pg.K_a]:
            # Increase the change in x direction of the player
            dx += speed_sin
            # Decrease the change in y direction of the player
            dy -= speed_cos
        # Check if the "d" key is pressed
        if keys[pg.K_d]:
            # Decrease the change in x direction of the player
            dx -= speed_sin
            # Increase the change in y direction of the player
            dy += speed_cos

        # Call the check_collision method to check if the player is colliding with a wall
        self.check_collision(dx, dy)

        # Check if the "left" key is pressed
        if keys[pg.K_LEFT]:
            # Decrease the direction of the player
            self.angle -= PLAYER_ROTATION * self.game.delta_time
        # Check if the "right" key is pressed
        if keys[pg.K_RIGHT]:
            # Increase the direction of the player
            self.angle += PLAYER_ROTATION * self.game.delta_time
        # Set the angle of the player between 0 and 360
        self.angle %= math.tau

    def draw(self):
        """Test method to draw the player"""

        # Draw the player's movement direction as a line
        pg.draw.line(self.game.screen, 'RED', (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH * math.cos(self.angle), self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        # Draw the player as a circle
        pg.draw.circle(self.game.screen, 'Green', (int(self.x * 100), int(self.y * 100)), 15)

    def check_walls(self, x, y):
        """Check if the coordinates are colliding with the walls"""

        # Check if the coordinates are in the map
        if (x, y) in self.game.map.world_map:
            # Return False if the coordinates are colliding with the walls
            return False
        # Return True if the coordinates are not colliding with the walls
        return True

    def check_collision(self, dx, dy):
        """Check if the player is colliding with the walls"""

        # Check if the player is colliding with the walls by passing the change in x and y direction of the player
        # First check the x direction
        if self.check_walls(int(self.x + dx), int(self.y)):
            # If the player is not colliding with the walls then update the x direction of the player
            self.x += dx
        # Then check the y direction
        if self.check_walls(int(self.x), int(self.y + dy)):
            # If the player is not colliding with the walls then update the y direction of the player
            self.y += dy

    def update(self):
        """Update the player"""

        # Update the movement of the player
        self.move()

    @property
    def pos(self):
        """Return the position of the player"""

        # Return the position of the player
        return self.x, self.y

    @property
    def map_pos(self):
        """Return the position of the player in the map"""

        # Return the position of the player in the map
        return int(self.x), int(self.y)
