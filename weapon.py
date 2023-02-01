from sprite_object import *


class Weapon(AnimatedSprite):
    '''Weapon class
    Inherits from AnimatedSprite class'''

    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.png', scale=0.4, animation_time=90):
        '''Initialize weapon
        Set game, path, scale, animation time, images, weapon position, reloading, number of images, frame counter and damage
        Inherit from AnimatedSprite class'''

        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])   
        # Set images
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())  
        # Set weapon position
        self.reloading = False  
        # Set reloading
        self.num_images = len(self.images) 
        # Set number of images
        self.frame_counter = 0  
        # Set frame counter
        self.damage = 50    
        # Set damage

    def animate_shot(self):
        '''Animate shot
        If reloading, set shot to false, rotate images, set image, increase frame counter and if frame counter is equal to number of images, set reloading to false, set frame counter to 0
        Inherit from AnimatedSprite class'''

        if self.reloading:     
            # If reloading
            self.game.player.shot = False   
            # Set shot to false
            if self.animation_trigger:  
                # If animation trigger
                self.images.rotate(-1)  
                # Rotate images
                self.image = self.images[0] 
                # Set image
                self.frame_counter += 1 
                # Increase frame counter
                if self.frame_counter == self.num_images:   
                    # If frame counter is equal to number of images
                    self.reloading = False  
                    # Set reloading to false
                    self.frame_counter = 0  
                    # Set frame counter to 0

    def draw(self):
        '''Draw weapon'''
        self.game.screen.blit(self.images[0], self.weapon_pos)  
        # Draw weapon

    def update(self):
        '''Update weapon'''
        self.check_animation_time() 
        # Check animation time
        self.animate_shot() 
        # Animate shot