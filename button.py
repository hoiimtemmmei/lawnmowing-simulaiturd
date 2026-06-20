import pygame

pygame.init()

butt_font = pygame.font.SysFont("none",100)

class button:
    def __init__(self, x, y,width, hieght, text):
        self.rect = pygame.rect.Rect(x,y,width, hieght)
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.hieght = hieght

    def draw(self, screen, color):
            pygame.draw.rect(screen, color, self.rect, border_radius=10)
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                butt_txt = butt_font.render(f">{self.text}<", True, (250, 250, 250))
            else:
                butt_txt = butt_font.render(self.text, True, (250, 250, 250))


            buttbox = butt_txt.get_rect(center=(self.x + self.width/2,self.y + self.hieght/2))
            screen.blit(butt_txt, buttbox)

    def get_pressed(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
            else:
                return False
        else:
            return False