import pygame as pg
from utils import colors

class Bar:
    def __init__(self, amount, type=0):
        if type == 0:
            # defense bar
            self.color1 = colors.BLUE
            self.color2 = colors.BLUE_DARK
            self.y = 15
        else:
            # health bar
            self.color1 = colors.RED
            self.color2 = colors.RED_DARK
            self.y = 40
        self.x = 150
        self.w = 500
        self.h = 20
        
        self.damage_per_hit = self.w // amount
        self.width_current_amount = self.w
        
        self.amount_effect_lenght = self.width_current_amount
        self.amount_change_speed = 2
    
    def update(self):
        if self.amount_effect_lenght > self.width_current_amount:
            self.amount_effect_lenght -= self.amount_change_speed
    
    def draw(self, surface, color):
        pg.draw.rect(surface, self.color2, (self.x, self.y, self.amount_effect_lenght, self.h))
        pg.draw.rect(surface, self.color1, (self.x, self.y, self.width_current_amount, self.h))
        pg.draw.rect(surface, color, (self.x, self.y, self.w, self.h), 2)
    
    def subtract_damage(self):
        self.width_current_amount -= self.damage_per_hit
        if self.width_current_amount < self.damage_per_hit:
            self.width_current_amount = 0
            
    def increase_status_back(self):
        self.width_current_amount = self.w
