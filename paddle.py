import pygame

pygame.init()

SLIDING_DIVIVER = 8

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def update(self, window):
        mx = pygame.mouse.get_pos()[0]

        dx = (mx - (self.rect.width / 2)) - self.rect.x

        self.rect.x += dx / SLIDING_DIVIVER

        pygame.draw.rect(window, self.color, self.rect)