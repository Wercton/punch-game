import pygame as pg

class HealthBar:
    def __init__(self, opponent_health):
        self.x = 150
        self.y = 25
        self.w = 500
        self.h = 20
        
        self.damage_per_hit = self.w // opponent_health
        self.width_current_health = self.w
        
        self.health_effect_lenght = self.width_current_health
        self.health_change_speed = 2
    
    def update(self):
        if self.health_effect_lenght > self.width_current_health:
            self.health_effect_lenght -= self.health_change_speed
    
    def draw(self, surface):
        pg.draw.rect(surface, (100, 0, 0), (self.x, self.y, self.health_effect_lenght, self.h))
        pg.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width_current_health, self.h))
        pg.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.w, self.h), 2)
    
    def subtract_damage(self):
        self.width_current_health -= self.damage_per_hit
        if self.width_current_health < self.damage_per_hit:
            self.width_current_health = 0