import pygame as pg
from utils.utils import get_image

class Fist(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.init_images()
        self.rect = self.image.get_rect()
        self.health = 10

    def init_images(self):
        self.image = get_image('data/images/fist.png', (60, 60), -1)
        self.image_normal = pg.transform.rotate(self.image, 90)
        self.image_punching = pg.transform.scale(self.image_normal, (50, 50))
        self.image = self.image_normal
    
    def update(self):
        if self.health > 0:
            pos = pg.mouse.get_pos()
            self.rect.center = pos

    def punch_target(self, target):
        self.punch_effect()
        return self.rect.colliderect(target)
    
    def miss_target(self):
        self.health -= 1
    
    def punch_effect(self):
        center = self.rect.center
        self.image = self.image_punching
        self.rect.center = center
        
    def unpunch_effect(self):
        center = self.rect.center
        self.image = self.image_normal
        self.rect.center = center
