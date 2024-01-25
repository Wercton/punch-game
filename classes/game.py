import pygame as pg
from utils.constants.settings import SCREEN_SIZE, TITLE
from classes.player.fist import Fist
from classes.opponents import FirstOpponent
from classes.player.fist_health import FistHealth
from utils.functions.debug import debug

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.font.init()
        
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.font_game = pg.font.SysFont('Comic Sans MS', 60)
        
        self.exit = False
        self.is_left_clicked = False
        self.level = 0
        
        self.fist = Fist()
        self.health_sprite = FistHealth()
        self.main_sprite = pg.sprite.RenderPlain((self.health_sprite, self.fist))


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
        if self.fist.health == 0:
            self.running_level = False
            self.running = False
            print("LOST")
        if self.opponent.health == -1:
            self.running_level = False
            self.running = False
            print("WIN")

    def draw(self):
        self.screen.fill(0)
        self.opponent.draw_health_bar(self.screen)
        self.sprites.draw(self.screen)
        self.main_sprite.draw(self.screen)
        self.draw_text(str(self.fist.health), (250, 250, 250), (self.health_sprite.rect.left - 10, self.health_sprite.rect.top + 7))
        pg.display.flip()
    
    def draw_text(self, text, color, pos):
        #TODO otimizar...
        self.text_surface = self.font_game.render(text, True, color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = pos
        self.screen.blit(self.text_surface, self.text_rect)
    
    def quit(self):
        pg.quit()