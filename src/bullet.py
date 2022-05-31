import pygame

from config import *
from logs import get_logger
logger = get_logger('my_app')


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("images/bullet.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 10

    def update(self):
        self.rect.centery += self.direction.y * self.speed
        if self.rect.centery <= 0:
            self.kill()
