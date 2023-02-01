import math


RES = WIDTH, HEIGHT = 1500, 850 
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0 
# 0 = unlimited

PLAYER_POS = 1.5, 5   
# x, y
PLAYER_ANGLE = 0    
# in radians
PLAYER_SPEED = 0.004    
# in units per frame
PLAYER_ROT_SPEED = 0.002    
# in radians per frame
PLAYER_SIZE_SCALE = 60  
# in pixels
PLAYER_MAX_HEALTH = 100 
# in health points

MOUSE_SENSITIVITY = 0.0003  
# in radians per pixel
MOUSE_MAX_REL = 40  
# in pixels
MOUSE_BORDER_LEFT = 100 
# in pixels
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT  
# in pixels

FLOOR_COLOR = (30, 30, 30)  
# in RGB

FOV = math.pi / 3   
# in radians
HALF_FOV = FOV / 2  
# in radians
NUM_RAYS = WIDTH // 2   
# in pixels
HALF_NUM_RAYS = NUM_RAYS // 2   
# in pixels
DELTA_ANGLE = FOV / NUM_RAYS    
# in radians
MAX_DEPTH = 20 
# in units

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)   
# in pixels
SCALE = WIDTH // NUM_RAYS  
# in pixels

TEXTURE_SIZE = 256  
# in pixels
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2   
# in pixels
