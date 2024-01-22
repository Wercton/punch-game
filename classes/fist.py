import pygame as pg
from utils.utils import get_image

class Fist(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = get_image('data/images/fist.png', (60, 60), -1)
        self.image = pg.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.health = 3

    def update(self):
        if self.health > 0:
            pos = pg.mouse.get_pos()
            self.rect.center = pos

    def punch_target(self, target):
        return self.rect.colliderect(target)
    
    def miss_target(self):
        self.health -= 1