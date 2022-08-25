__author__ = "Alon B.R"

import pygame
import sys
import os

from paddle import Paddle
from tile import Tile
from button import Button

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

        self.paddle = Paddle(
            pygame.transform.scale(load_img("data", "Assets", "paddle.png"), (200, 20)),
            self.WIDTH // 2,
            self.HEIGHT - 120,
        )

        self.ball = Ball(
            pygame.transform.scale(load_img("data", "Assets", "ball.png"), (20, 20)),
            self.WIDTH // 2,
            self.HEIGHT - 150,
            20,
            10,
        )

        self.tile_list = []
        self.generate_tiles()

        # main manu
        self.start_button = Button(
            pygame.transform.scale(
                load_img("data", "Assets", "start button colliding.png"), (100, 50)
            ),
            pygame.transform.scale(
                load_img("data", "Assets", "start button off.png"), (100, 50)
            ),
            self.WIDTH // 2,
            self.HEIGHT // 2,
        )

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
        self.background = pygame.transform.scale(
            load_img("data", "Assets", "background.png"),
            (self.WIDTH, self.HEIGHT),
        )
        while self.run:
            # self.app.fill((255, 255, 255))
            self.app.blit(
                self.background,
                (0, 0),
            )  # background

            if self.start_button.clicked_once:

                self.paddle.update(self.app)
                self.ball.update(self.app, self.paddle, self.tile_list)

                for tile in self.tile_list:
                    tile.update(self.app)
                self.start_button.update(False)
            else:
                self.start_button.listen(self.app)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()

            self.clock.tick(self.FPS)
            pygame.display.update()

            # deleting the tiles when colliding with the ball
            if self.start_button.clicked_once:
                for tile in self.tile_list:
                    if tile.kill:
                        self.tile_list.remove(tile)


if __name__ == "__main__":
    game = Main()
    game.play()
