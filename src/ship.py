import pygame

from debug.debug import debug
from config import *

from logs import get_logger
logger = get_logger('my_app')


class Ship(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("images/ship.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def update(self):
        self.input()
        self.move()

    def input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self):

        self.check_x()
        self.rect.centerx += self.direction.x * self.speed

    def check_x(self):

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - 64:
            self.rect.x = WIDTH - 64
