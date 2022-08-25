import pygame
import random

from main import Main


pygame.init()


class Ball:
    def __init__(self, img, x, y, vel_x, vel_y) -> None:
        self.img = img
        self.rect = self.img.get_rect(x=x, y=y)
        self.vel_x = vel_x
        self.vel_y = vel_y

    def update(self, window, paddle, tile_list) -> None:
        dx = 0
        dy = 0

        dx += self.vel_x
        dy += self.vel_y

        if self.rect.y < 0:
            self.vel_y = abs(self.vel_y)

        elif self.rect.y + self.rect.height > Main.HEIGHT:
            self.vel_y = abs(self.vel_y) * -1

        if self.rect.x < 0:
            self.vel_x = abs(self.vel_x)

        elif self.rect.x + self.rect.width > Main.WIDTH:
            self.vel_x = abs(self.vel_x) * -1

        #  paddle collision detection

        # x

        if paddle.rect.colliderect(
            (self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height)
        ):
            if dx > 0:
                dx = paddle.rect.x - (self.rect.x + self.rect.width)
            elif dx < 0:
                dx = self.rect.x - (paddle.rect.x + paddle.rect.width)

            self.vel_x *= -1
            self.vel_x += random.randint(-7, 7)
            self.vel_x = min(self.vel_x, 15)
            self.vel_x = max(self.vel_x, -15)
            if self.vel_x == 0:
                self.vel_x = -10

        # y
        if paddle.rect.colliderect(
            (self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height)
        ):
            if dy > 0:
                dy = paddle.rect.y - (self.rect.y + self.rect.height)
            elif dy < 0:
                dy = self.rect.y - (paddle.rect.y + paddle.rect.height)

            self.vel_y *= -1
            self.vel_y += random.randint(-7, 7)
            self.vel_y = min(self.vel_y, 15)
            self.vel_y = max(self.vel_y, -15)
            if self.vel_y == 0:
                self.vel_y = -10

        # tile collision detection
        for tile in tile_list:
            # x
            if tile.rect.colliderect(
                (self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height)
            ):
                if dx >= 0:
                    dx = tile.rect.x - (self.rect.x + self.rect.width)
                    self.vel_x = abs(self.vel_x) * -1
                elif dx < 0:
                    dx = self.rect.x - (tile.rect.x + tile.rect.width)
                    self.vel_x = abs(self.vel_x)
                tile.kill = True
            # y
            if tile.rect.colliderect(
                (self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height)
            ):
                if dy > 0:
                    dy = tile.rect.y - (self.rect.y + self.rect.height)
                    self.vel_y = abs(self.vel_y) * -1
                elif dy < 0:
                    dy = self.rect.y - (tile.rect.y + tile.rect.height)
                    self.vel_y = abs(self.vel_y)
                tile.kill = True

        # adding values
        self.rect.x += dx
        self.rect.y += dy

        # drawing position
        window.blit(self.img, self.rect)
