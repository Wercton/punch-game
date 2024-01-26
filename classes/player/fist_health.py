import pygame as pg
from utils.functions.utils import get_image
from utils.constants.settings import SCREEN_SIZE

class FistHealth(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = get_image('data/images/heart2.png', (60, 60), -1)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_SIZE[0] - 30, SCREEN_SIZE[1] - 30)
