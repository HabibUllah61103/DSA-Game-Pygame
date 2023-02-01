import pygame as pg


class Sound:
    '''Sound class
    Initialize pygame mixer, set path, load sounds and set volume'''

    def __init__(self, game):
        '''Initialize pygame mixer, set path, load sounds and set volume
        Set game'''
        self.game = game    
        # Set game
        pg.mixer.init() 
        # Initialize pygame mixer
        self.path = 'resources/sound/'  
        # Set path
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')    
        # Load shotgun sound
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')  
        # Load npc pain sound
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')    
        # Load npc death sound
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')    
        # Load npc shot sound
        self.npc_shot.set_volume(0.2)   
        # Set npc shot volume
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')    
        # Load player pain sound
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')   
        # Load theme sound
        pg.mixer.music.set_volume(0.4)  
        # Set theme volume