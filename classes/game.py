import pygame as pg
from utils.settings import SCREEN_SIZE, TITLE
from classes.fist import Fist
from classes.opponents import FirstOponent

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.mouse.set_visible(0)
        pg.font.init()
        
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.font_game = pg.font.SysFont('Comic Sans MS', 30)
        
        self.running = True
        self.is_left_clicked = False
        
        self.fist = Fist()
        self.opponent = FirstOponent()
        self.sprites = pg.sprite.RenderPlain((self.opponent, self.fist))

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
                if click[0]:
                    self.is_left_clicked = True
                    self.check_combat()
                elif click[2]:
                    self.isPressed = True
            elif event.type == pg.MOUSEBUTTONUP:
                if self.is_left_clicked:
                    self.is_left_clicked = False
                    self.fist.unpunch_effect()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False

    def check_combat(self):
        if self.fist.punch_target(self.opponent):
            self.opponent.hit()
        else:
            self.fist.miss_target()

    def update(self):
        self.sprites.update()

    def draw(self):
        self.screen.fill(0)
        self.opponent.draw_health_bar(self.screen)
        self.sprites.draw(self.screen)
        pg.display.flip()

    def quit(self):
        pg.quit()