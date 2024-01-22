import pygame as pg
from classes.health_bar import HealthBar
from utils.utils import get_image
from utils.settings import SCREEN_SIZE
from random import randint

class FirstOponent(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = get_image('data/images/Bob.png', (180, 180), -1)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        
        self.speed = -5
        self.health = 5
        
        self.health_bar = HealthBar(self.health)
        
    def update(self):
        if self.health > 0:
            self.move()
        self.health_bar.update()
    
    def draw_health_bar(self, surface):
        self.health_bar.draw(surface)
        
    def move(self):
        if self.rect.right < 0 or self.rect.left > SCREEN_SIZE[0]:
            self.respawn()
        self.rect.x += self.speed
        
    def respawn(self):
        height = randint(0, SCREEN_SIZE[1] - 150)
        self.rect.y = height
        if randint(0, 1):
            if self.speed > 0:
                self.image = pg.transform.flip(self.image, True, False)
                self.speed *= -1
            self.rect.left = SCREEN_SIZE[0]
        else:
            if self.speed < 0:
                self.image = pg.transform.flip(self.image, True, False)
                self.speed *= -1
            self.rect.right = 0
            
    def hit(self):
        self.health -= 1
        self.health_bar.subtract_damage()
        self.move_faster()
        self.respawn()
        
    def move_faster(self):
        if self.speed > 0:
            self.speed += 2
        else:
            self.speed -= 2
