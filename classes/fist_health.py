import pygame as pg
from utils.utils import get_image
from utils.settings import SCREEN_SIZE

class FistHealth(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = get_image('data/images/heart2.png', (60, 60), -1)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_SIZE[0] - 30, SCREEN_SIZE[1] - 30)
