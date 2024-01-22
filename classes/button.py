class Button:
    def __init__(self, text, textColor, pos, font):
        self.font = font
        self.text = text
        self.color = textColor
        self.text_surface = font.render(text, True, textColor)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = pos
        self.is_highlighted = False

    def draw(self, surface):
        surface.blit(self.text_surface, self.text_rect)

    def has_clicked(self, mouse_pos):
        if self.text_rect.collidepoint(mouse_pos):
            return True
        return False
            
    def update(self, mouse_pos):
        if self.text_rect.collidepoint(mouse_pos):
            self.highlight()
        elif self.is_highlighted:
            self.unhighlight()

    def highlight(self):
        self.is_highlighted = True
        self.text_surface = self.font.render(self.text, True, (0, 255, 255))

    def unhighlight(self):
        self.is_highlighted = False
        self.text_surface = self.font.render(self.text, True, self.color)
