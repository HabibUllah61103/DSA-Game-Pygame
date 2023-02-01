import pygame as pg
from settings import *
import os
from collections import deque


class SpriteObject:
    '''Sprite object class
    Load image, set position, scale, shift, game, player, x, y, image, image width, image half width,
    image ratio, dx, dy, theta, screen x, dist, norm dist, sprite half width, sprite scale and sprite height shift'''

    def __init__(self, game, path='resources/sprites/static_sprites/candlebra.png',
                 pos=(10.5, 3.5), scale=0.7, shift=0.27):   
        self.game = game
        self.player = game.player 
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()    
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

    def get_sprite_projection(self):
        '''Get sprite projection
        Set projection, projection width, projection height, image, sprite half width, height shift and pos
        Append to objects to render'''

        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE 
        # Projection
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj 
        # Projection width, projection height

        image = pg.transform.scale(self.image, (proj_width, proj_height))   
        # Set image

        self.sprite_half_width = proj_width // 2    
        # Set sprite half width
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT   
        # Set height shift
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift  
        # Set pos

        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))   
        # Append to objects to render

    def get_sprite(self):
        '''Get sprite
        Set dx, dy, theta, screen x, dist, norm dist and get sprite projection'''

        dx = self.x - self.player.x   
        # Set dx
        dy = self.y - self.player.y  
        # Set dy
        self.dx, self.dy = dx, dy   
        # Set dx, dy
        self.theta = math.atan2(dy, dx) 
        # Set theta

        delta = self.theta - self.player.angle  
        # Set delta
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0): 
            # If dx > 0 and self.player.angle > math.pi or dx < 0 and dy < 0
            delta += math.tau   
            # Add math.tau to delta

        delta_rays = delta / DELTA_ANGLE    
        # Set delta rays
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE    
        # Set screen x

        self.dist = math.hypot(dx, dy)  
        # Set dist
        self.norm_dist = self.dist * math.cos(delta)    
        # Set norm dist
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()    
            # Get sprite projection

    def update(self):
        self.get_sprite()   
        # Get sprite


class AnimatedSprite(SpriteObject):
    '''Animated sprite class
    Set animation time, path, images, animation time prev, animation trigger and call super init'''

    def __init__(self, game, path='resources/sprites/animated_sprites/green_light/0.png',
                 pos=(11.5, 3.5), scale=0.8, shift=0.16, animation_time=120):
        '''Set animation time, path, images, animation time prev, animation trigger and call super init'''
        super().__init__(game, path, pos, scale, shift) # Call super init
        self.animation_time = animation_time    # Set animation time
        self.path = path.rsplit('/', 1)[0]  # Set path
        self.images = self.get_images(self.path)    # Set images
        self.animation_time_prev = pg.time.get_ticks()  # Set animation time prev
        self.animation_trigger = False  # Set animation trigger

    def update(self):
        '''Call super update, check animation time and animate'''

        super().update()    # Call super update
        self.check_animation_time() # Check animation time
        self.animate(self.images)   # Animate

    def animate(self, images):
        if self.animation_trigger:  # If self.animation_trigger
            images.rotate(-1)   # Rotate images
            self.image = images[0]  # Set image

    def check_animation_time(self):
        '''Check animation time
        Set animation trigger, time now and if time now - self.animation_time_prev > self.animation_time'''

        self.animation_trigger = False  # Set animation trigger
        time_now = pg.time.get_ticks()  # Set time now
        if time_now - self.animation_time_prev > self.animation_time:   # If time now - self.animation_time_prev > self.animation_time
            self.animation_time_prev = time_now # Set self.animation_time_prev
            self.animation_trigger = True   # Set self.animation_trigger

    def get_images(self, path):
        images = deque()    # Set images
        for file_name in os.listdir(path):  # Loop through os.listdir(path)
            if os.path.isfile(os.path.join(path, file_name)):   # If os.path.isfile(os.path.join(path, file_name))
                img = pg.image.load(path + '/' + file_name).convert_alpha() # Set img
                images.append(img)  # Append img to images
        return images   # Return images
