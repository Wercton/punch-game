import pygame as pg
from utils.settings import *
from fist import Fist

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("PUNCH GAME")
        pg.mouse.set_visible(0)
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        
        self.running = True
        self.isPressed = False
        
        self.fist = Fist()
        self.sprites = pg.sprite.RenderPlain((self.fist))
        
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
        self.quit()
            
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                click = pg.mouse.get_pressed()
                if click[2]:
                    self.isPressed = True
                    self.paint_magic_powerup()
            elif event.type == pg.MOUSEBUTTONUP:
                self.isPressed = False
                self.clean_magic_powerup()
                
    def paint_magic_powerup(self):
        if self.isPressed:
            print('hi')
            pg.draw.circle(self.screen, (250, 0, 0), pg.mouse.get_pos(), 40)
            
    def clean_magic_powerup(self):
        print("cleaned")
    
    def update(self):
        self.sprites.update()
    
    def draw(self):
        self.screen.fill(0)
        self.paint_magic_powerup()
        self.sprites.draw(self.screen)
        pg.display.flip()
    
    def quit(self):
        pg.quit()