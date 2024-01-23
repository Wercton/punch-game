import pygame as pg
from utils.settings import SCREEN_SIZE, TITLE
from classes.fist import Fist
from classes.opponents import FirstOpponent

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        # pg.mouse.set_visible(0)
        pg.font.init()
        
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.font_game = pg.font.SysFont('Comic Sans MS', 60)
        
        self.exit = False
        self.is_left_clicked = False
        self.level = 0
        
        self.fist = Fist()
        self.main_sprite = pg.sprite.RenderPlain((self.fist))

    def run(self):
        self.running = True
        while self.running:
            pg.mouse.set_visible(0)
            self.start_level()
            while self.running_level:
                self.clock.tick(60)
                self.events()
                self.update()
                self.draw()

    def start_level(self):
        self.fist.health = 3
        self.running_level = True
        if self.level == 0:
            self.opponent = FirstOpponent()
            self.sprites = pg.sprite.RenderPlain((self.opponent))
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running_level = False
                self.running = False
                self.exit = True
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
                    self.running_level = False
                    self.running = False

    def check_combat(self):
        if self.fist.punch_target(self.opponent):
            if pg.sprite.spritecollide(self.opponent, [self.fist], False, pg.sprite.collide_mask):
                self.opponent.hit()
            else:
                self.fist.miss_target()
        else:
            self.fist.miss_target()

    def update(self):
        self.main_sprite.update()
        self.sprites.update()
        if self.fist.health == 0 or self.opponent.health == 0:
            self.running_level = False
            self.running = False

    def draw(self):
        self.screen.fill(0)
        self.opponent.draw_health_bar(self.screen)
        self.sprites.draw(self.screen)
        self.main_sprite.draw(self.screen)
        pg.display.flip()
    
    def quit(self):
        pg.quit()