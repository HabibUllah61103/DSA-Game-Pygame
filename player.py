from settings import *
import pygame as pg
import math


class Player:
    '''Player class
    Set game, x, y, angle, shot, health, rel, health recovery delay, time prev'''

    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.health = PLAYER_MAX_HEALTH
        self.rel = 0
        self.health_recovery_delay = 700
        self.time_prev = pg.time.get_ticks()

    def recover_health(self):
        '''Recover health
        If check health recovery delay and health is less than player max health
        Health plus 1'''

        if self.check_health_recovery_delay() and self.health < PLAYER_MAX_HEALTH:
            self.health += 1

    def check_health_recovery_delay(self):
        '''Check health recovery delay
        Time now is pygame time get ticks
        If time now minus time prev is greater than health recovery delay
        Time prev is time now
        Return true'''

        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True

    def check_game_over(self):
        '''Check game over
        If health is less than 1
        Game object renderer game over
        Display flip
        Time delay 1500'''

        if self.health < 1:
            self.game.object_renderer.game_over()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def get_damage(self, damage):
        '''Get damage
        Health minus damage
        Game object renderer player damage
        Game sound player pain play
        Check game over'''

        self.health -= damage
        self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over()

    def single_fire_event(self, event):
        '''Single fire event
        If event type is pygame mouse button down
        If event button is 1 and not shot and not game weapon reloading
        Game sound single fire play'''

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True

    def movement(self):
        '''Movement
        Speed is player speed times game delta time
        Speed sin is speed times sin a
        Speed cos is speed times cos a
        Keys is pygame key get pressed
        '''

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)   # check wall collision

        self.angle %= math.tau  

    def check_wall(self, x, y):
        '''Check wall
        If (x, y) not in game map world map
        Return true'''

        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        '''Check wall collision
        Scale is player size scale times game delta time'''

        scale = PLAYER_SIZE_SCALE / self.game.delta_time    # scale
        if self.check_wall(int(self.x + dx * scale), int(self.y)):  # check wall
            self.x += dx    # x plus dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):  # check wall
            self.y += dy    # y plus dy

    def draw(self): # draw
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100), 
                    (self.x * 100 + WIDTH * math.cos(self.angle),   
                     self.y * 100 + WIDTH * math. sin(self.angle)), 2)  # draw line
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15) # draw circle

    def mouse_control(self):
        '''Mouse control
        Mx, my is pygame mouse get pos'''

        mx, my = pg.mouse.get_pos() # mx, my
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:   # if mx less than mouse border left or mx greater than mouse border right
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])   # set mouse pos
        self.rel = pg.mouse.get_rel()[0]    # rel is pygame mouse get rel
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))    # rel is max mouse max rel, min mouse max rel, rel
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time   # angle plus rel times mouse sensitivity times game delta time

    def update(self):
        self.movement()
        self.mouse_control()
        self.recover_health()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)