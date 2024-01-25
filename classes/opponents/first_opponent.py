import pygame as pg
from classes.opponents.health_bar import Bar
from utils.constants import opponents_status as ops
from utils.functions.utils import get_image
from utils.constants.settings import SCREEN_SIZE
from utils.constants import colors
from random import randint

class FirstOpponent(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = get_image('data/images/Bob.png', (180, 180), -1)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.mask = pg.mask.from_surface(self.image)
        
        self.speed = ops.START_SPEED
        self.speed_up = ops.INCREASE_SPEED_RATE
        self.health = ops.MAX_HEALTH
        self.defense = ops.MAX_DEFENSE
        self.stage = 0
        
        self.health_bar = Bar(self.health, 1)
        self.defense_bar = Bar(self.defense, 0)
        self.respawn()
        
    def update(self):
        if self.health > 0:
            self.move()
        else:
            self.stop()
        self.health_bar.update()
    
    def draw_health_bar(self, surface):
        if self.defense > 0:
            self.health_bar.draw(surface, colors.BLACK)
            self.defense_bar.draw(surface, colors.WHITE)
        else:
            self.health_bar.draw(surface, colors.WHITE)
            self.defense_bar.draw(surface, colors.BLACK)
        
    def move(self):
        if self.stage == 0:
            if self.rect.right < 0 or self.rect.left > SCREEN_SIZE[0]:
                self.first_respawn_pattern()
            self.rect.x += self.speed
        elif self.stage > 0:
            if self.rect.bottom < 0 or self.rect.top > SCREEN_SIZE[1]:
                self.second_respawn_pattern()
            self.rect.y += self.speed
        # elif self.stage == 2:
        #     if self.rect.right < 0 or self.rect.left > SCREEN_SIZE[0] or self.rect.bottom < 0 or self.rect.top > SCREEN_SIZE[1]:
        #         if randint(0, 1):
        #             self.first_respawn_pattern()
        #         else:
        #             self.second_respawn_pattern()
        #     print(self.rect.x, end=" - ")
        #     print(self.rect.y)

    def stop(self):
        self.speed = 0
    
    def respawn(self):
        if self.stage == 0:
            self.first_respawn_pattern()
        elif self.stage > 0:
            self.second_respawn_pattern()
        # elif self.stage == 2:
        #     # self.rect.x = 130
        #     # self.rect.y = 130
        #     if randint(0, 1):
        #         self.first_respawn_pattern()
        #     else:
        #         self.second_respawn_pattern()
            
    def first_respawn_pattern(self):
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
            
    def second_respawn_pattern(self):
        width = randint(100, SCREEN_SIZE[0] - 150)
        self.rect.x = width
        if randint(0, 1):
            if self.speed > 0:
                self.image = pg.transform.flip(self.image, True, False)
                self.speed *= -1
            self.rect.top = SCREEN_SIZE[1]
        else:
            if self.speed < 0:
                self.image = pg.transform.flip(self.image, True, False)
                self.speed *= -1
            self.rect.bottom = 0
            
    def hit(self):
        if self.defense == 0:
            self.health -= 1
            self.health_bar.subtract_damage()
            self.move_faster()
            if self.health > 0:
                self.stage += 1
                self.defense = ops.MAX_DEFENSE
                self.defense_bar.increase_status_back()
                self.respawn()
        else:
            self.defense -= 1
            self.defense_bar.subtract_damage()
            self.move_faster()
            self.respawn()
        
    def move_faster(self):
        if self.speed > 0:
            self.speed += self.speed_up
        else:
            self.speed -= self.speed_up
