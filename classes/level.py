import pygame as pg
from classes.player.fist import Fist
from classes.opponents.first_opponent import FirstOpponent

class Level:
    def __init__(self):
        self.screen = pg.display.get_surface()
        
        self.visible_sprites = pg.sprite.Group()
        self.hostile_sprites = pg.sprite.Group()
        
        self.init_sprites()
    
    def init_sprites(self):
        self.fist = Fist([self.visible_sprites])
        self.opponent = FirstOpponent([self.visible_sprites, self.hostile_sprites])
    
    def update(self):
        self.visible_sprites.update()
    
    def draw(self):
        self.visible_sprites.draw(self.screen)
        
