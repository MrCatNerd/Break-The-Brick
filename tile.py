import pygame

pygame.init()

class Tile:  # TODO: finish this class
    SIZE_X = 50
    SIZE_Y = 20

    def __init__(self, img, x, y):
        self.img = img
        self.rect = self.img.get_rect(x=x, y=y)

        self.kill = False

    def update(self, window) -> None:

        # if self.rect.colliderect(
        #  (
        #       ball.rect.x + ball.dx,
        #        ball.rect.y + ball.dy,
        #       ball.rect.width,
        #   ball.rect.height,
        # )
        # ):
        # self.kill = True
        # elif self.kill is True:
        # self.kill = False

        window.blit(self.img, self.rect)