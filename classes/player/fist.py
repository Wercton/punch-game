import pygame as pg
from utils.functions.utils import get_image

class Fist(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.init_images()
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.health = 10

    def init_images(self):
        self.image = get_image('data/images/fist.png', (60, 60), -1)
        self.image_normal = pg.transform.rotate(self.image, 90)
        self.image_punching = pg.transform.scale(self.image_normal, (50, 50))
        self.image = self.image_normal
    
    def update(self):
        self.input()
        if self.health > 0:
            pos = pg.mouse.get_pos()
            self.rect.center = pos
            
    def input(self):
        click = pg.mouse.get_pressed()
        if not click[0]:
            self.is_left_clicked = False
        else:
            self.is_left_clicked = True

    def check_combat(self):
        pass
    
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
