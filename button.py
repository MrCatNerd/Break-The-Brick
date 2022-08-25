import pygame

pygame.init()


class Button:
    def __init__(self, img_on, img_off, x, y, state=False):
        self.img_on = img_on
        self.img_off = img_off

        self.rect_on = self.img_on.get_rect(x=x, y=y)
        self.rect_off = self.img_off.get_rect(x=x, y=y)

        self.state = state
        self.clicked_once = False

    def listen(self, window):
        mx, my = pygame.mouse.get_pos()

        if self.state:
            if (
                mx >= self.rect_on.x
                and mx <= self.rect_on.x + self.rect_on.width
                and my >= self.rect_on.y
                and my <= self.rect_on.y + self.rect_on.height
                and any(pygame.mouse.get_pressed())
            ):
                self.state = True
                self.clicked_once = True
            elif self.state:
                self.state = False
        elif not self.state:
            if (
                mx >= self.rect_off.x
                and mx <= self.rect_off.x + self.rect_off.width
                and my >= self.rect_off.y
                and my <= self.rect_off.y + self.rect_off.height
                and any(pygame.mouse.get_pressed())
            ):
                self.state = True
            elif self.state:
                self.state = False

        if self.state or (
            mx >= self.rect_on.x
            and mx <= self.rect_on.x + self.rect_on.width
            and my >= self.rect_on.y
            and my <= self.rect_on.y + self.rect_on.height
        ):
            window.blit(self.img_on, self.rect_on)
        else:
            window.blit(self.img_off, self.rect_off)

    def update(self, window=False):
        """used if you want to update your button(if its not 1 use only button)
        because if you switch loops or use if statements, you need to reset the button"""
        if self.state:
            self.state = False

            if window is not False:
                window.blit(self.img_on, self.rect_on)
        elif window is not False:
            window.blit(self.img_off, self.rect_off)
