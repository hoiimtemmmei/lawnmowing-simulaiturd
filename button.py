import pygame

pygame.init()

butt_font = pygame.font.SysFont("none",100)

class button:
    def __init__(self, x, y,width, hieght, text):
        self.rect = (x,y,width, hieght)
        self.text = text
        self.x = x
        self.y = y

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        butt_txt = butt_font.render("start", True, (250, 250, 250))
        screen.blit(butt_txt, (400, 300))