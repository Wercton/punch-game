import pygame as pg
from classes.game import Game
from classes.button import Button

class Menu(Game):
    def start(self):
        self.start_button = Button("iniciar", (250, 0, 250), (400, 200), self.font_game)
        self.exit_button = Button("sair", (250, 0, 250), (400, 250), self.font_game)
        self.buttons = [self.start_button, self.exit_button]
        self.choosing = True
        self.game_open()

    def game_open(self):
        while self.choosing and not self.exit:
            self.main_screen()
            if self.playing == True:
                self.run()
                self.choosing = True
                pg.mouse.set_visible(1)
        pg.quit()

    def main_screen(self):
        self.choosing = True
        self.playing = False
        while self.choosing:
            self.screen.fill(0)
            for button in self.buttons:
                button.draw(self.screen)
            self.main_screen_events()
            pg.display.flip()

    def main_screen_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.choosing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.start_button.has_clicked(pg.mouse.get_pos()):
                    self.choosing = False
                    self.playing = True
                elif self.exit_button.has_clicked(pg.mouse.get_pos()):
                    self.choosing = False
                
        self.check_buttons_collision()

    def check_buttons_collision(self):
        for button in self.buttons:
            button.update(pg.mouse.get_pos())
