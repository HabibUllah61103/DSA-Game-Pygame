import math

RES = WIDTH, HEIGHT = 1505,825
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

Player_pos = 1.5,1
Player_angle = 0
Player_speed = 0.004
Player_rotation = 0.002

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH //2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH  / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS