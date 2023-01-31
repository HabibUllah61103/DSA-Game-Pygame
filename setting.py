# Import the math module
import math

# Set the resolution of the game window
RES = WIDTH, HEIGHT = 1505, 825
# Set the Frame rate of the game
FPS = 60

# Set the initial position of the player in the mini_map
PLAYER_POS = 1.5, 5
# Set the initial angle of the player
PLAYER_ANGLE = 0
# Set the initial speed of the player
PLAYER_SPEED = 0.004
# Set the initial rotation of the player
PLAYER_ROTATION = 0.002

# Set the field of view of the player
FOV = math.pi / 3
# Set the half of the field of view of the player
HALF_FOV = FOV / 2
# Set the number of rays
NUM_RAYS = WIDTH // 2
# Set the half of the number of rays
HALF_NUM_RAYS = NUM_RAYS // 2
# Set the angle between each ray
DELTA_ANGLE = FOV / NUM_RAYS
# Set the maximum depth of the ray
MAX_DEPTH = 20
