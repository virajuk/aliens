import pygame

from config import *
from logs import get_logger
logger = get_logger('my_app')


class Bug(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("images/bug.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(1, 0)
        self.x_speed = 3
        self.y_change = 64

    def update(self):
        self.rect.centerx += self.direction.x * self.x_speed
        self.move()

    def move(self):
        if self.rect.x <= 0:
            self.direction.x = 1
            self.rect.centery += self.y_change
        elif self.rect.x >= WIDTH - 64:
            self.direction.x = -1
            self.rect.centery += self.y_change
        else:
            pass
