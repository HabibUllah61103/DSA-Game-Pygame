import pygame as pg
import math
from settings import *


class RayCasting:
    '''Ray casting class
    Get ray casting result and objects to render
    Set game, ray casting result, objects to render and textures
    Get objects to render'''
    
    def __init__(self, game):
        self.game = game    
        self.ray_casting_result = []    # (depth, proj_height, texture, offset)
        self.objects_to_render = []   # (depth, image, pos)
        self.textures = self.game.object_renderer.wall_textures # (texture, offset)

    def get_objects_to_render(self):
        '''Get objects to render
        Set objects to render
        Set wall column, wall pos and append to objects to render
        Set wall column, wall pos and append to objects to render'''

        self.objects_to_render = [] # (depth, image, pos)
        for ray, values in enumerate(self.ray_casting_result):  #Loop through ray casting result
            depth, proj_height, texture, offset = values    #Set depth, proj_height, texture, offset

            if proj_height < HEIGHT:    #If projection height is less than height
                wall_column = self.textures[texture].subsurface(offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE)   
                #Set wall column
                wall_column = pg.transform.scale(wall_column, (SCALE, proj_height)) #Set wall column
                wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)    #Set wall pos
            else:   
                texture_height = TEXTURE_SIZE * HEIGHT / proj_height    #Set texture height
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - texture_height // 2,
                    SCALE, texture_height
                )   #Set wall column
                wall_column = pg.transform.scale(wall_column, (SCALE, HEIGHT))  #Set wall column
                wall_pos = (ray * SCALE, 0) #Set wall pos

            self.objects_to_render.append((depth, wall_column, wall_pos))   #Append to objects to render

    def ray_cast(self):
        '''Ray cast
        Set ray casting result
        Set texture vert, texture hor, ox, oy, x map, y map
        Set ray angle'''

        self.ray_casting_result = []    #Set ray casting result
        texture_vert, texture_hor = 1, 1    #Set texture vert, texture hor
        ox, oy = self.game.player.pos   #Set ox, oy
        x_map, y_map = self.game.player.map_pos #Set x map, y map

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001  #Set ray angle
        for ray in range(NUM_RAYS): #Loop through number of rays
            sin_a = math.sin(ray_angle) #Set sin a
            cos_a = math.cos(ray_angle) #Set cos a

            # horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1) #Set y hor, dy

            depth_hor = (y_hor - oy) / sin_a    #Set depth hor
            x_hor = ox + depth_hor * cos_a  #Set x hor

            delta_depth = dy / sin_a    #Set delta depth
            dx = delta_depth * cos_a    #Set dx

            for i in range(MAX_DEPTH):  #Loop through max depth
                tile_hor = int(x_hor), int(y_hor)   #Set tile hor
                if tile_hor in self.game.map.world_map: #If tile hor in world map
                    texture_hor = self.game.map.world_map[tile_hor] #Set texture hor
                    break   
                x_hor += dx   #Set x hor
                y_hor += dy  #Set y hor
                depth_hor += delta_depth    #Set depth hor

            # verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)    #Set x vert, dx

            depth_vert = (x_vert - ox) / cos_a  #Set depth vert
            y_vert = oy + depth_vert * sin_a    #Set y vert

            delta_depth = dx / cos_a    #Set delta depth
            dy = delta_depth * sin_a    #Set dy

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)    #Set tile vert
                if tile_vert in self.game.map.world_map:    #If tile vert in world map
                    texture_vert = self.game.map.world_map[tile_vert]   #Set texture vert
                    break   
                x_vert += dx    #Set x vert
                y_vert += dy    #Set y vert
                depth_vert += delta_depth   #Set depth vert

            # depth, texture offset
            if depth_vert < depth_hor:  #If depth vert is less than depth hor
                depth, texture = depth_vert, texture_vert   #Set depth, texture
                y_vert %= 1 #Set y vert
                offset = y_vert if cos_a > 0 else (1 - y_vert)  #Set offset
            else:
                depth, texture = depth_hor, texture_hor  #Set depth, texture
                x_hor %= 1  #Set x hor
                offset = (1 - x_hor) if sin_a > 0 else x_hor    #Set offset

            # remove fishbowl effect
            depth *= math.cos(self.game.player.angle - ray_angle)   #Set depth

            # projection
            proj_height = SCREEN_DIST / (depth + 0.0001)    #Set proj height

            # ray casting result
            self.ray_casting_result.append((depth, proj_height, texture, offset))   #Append to ray casting result

            ray_angle += DELTA_ANGLE    #Set ray angle

    def update(self):
        self.ray_cast() #Ray cast
        self.get_objects_to_render()    #Get objects to render
