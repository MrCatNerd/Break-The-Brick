import pygame

pygame.init()

SLIDING_DIVIVER = 8


class Paddle:
    def __init__(self, img, x, y):
        self.img = img
        self.rect = self.img.get_rect(x=x, y=y)

    def update(self, window):
        mx = pygame.mouse.get_pos()[0]

        dx = (mx - (self.rect.width / 2)) - self.rect.x

        self.rect.x += dx / SLIDING_DIVIVER

        window.blit(self.img, self.rect)
