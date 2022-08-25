__author__ = "Alon B.R"

import pygame
import sys
import os

from paddle import Paddle
from tile import Tile

if __name__ == "__main__":  # to not cause circular import
    from ball import Ball

pygame.init()


def load_img(*paths):
    return pygame.image.load(os.path.join(*paths)).convert()


class Main:
    WIDTH = 1000
    HEIGHT = 1000
    TITLE = "Break the brick"
    FONT = pygame.font.Font(None, 20)

    def __init__(self) -> None:
        self.app = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.SCALED)
        pygame.display.set_caption(self.TITLE)

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.run = True

        # loading images

        self.paddle = Paddle(self.WIDTH // 2, self.HEIGHT - 120, 200, 20, (0, 0, 0))

        self.ball = Ball(self.WIDTH // 2, self.HEIGHT - 150, 20, 10, 20, (255, 0, 255))

        self.tile_list = []
        self.generate_tiles()

    def generate_tiles(self) -> None:
        self.tile_list = []

        self.tile_list = [
            Tile(
                pygame.transform.scale(
                    load_img("data", "Assets", "brick.png"), (Tile.SIZE_X, Tile.SIZE_Y)
                ),
                x,
                y,
            )
            for x in range(0, self.WIDTH + 1, Tile.SIZE_X)
            for y in range(0, (Tile.SIZE_Y * 10) + 1, Tile.SIZE_Y)
        ]

    def play(self) -> None:
        while self.run:
            self.app.fill((255, 255, 255))

            self.paddle.update(self.app)
            self.ball.update(self.app, self.paddle, self.tile_list)

            for tile in self.tile_list:
                tile.update(self.app)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()

            self.clock.tick(self.FPS)
            pygame.display.update()

            # deleting the tiles when colliding with the ball
            for tile in self.tile_list:
                if tile.kill:
                    self.tile_list.remove(tile)


if __name__ == "__main__":
    game = Main()
    game.play()
