import pygame

from config import *
from logs import get_logger
logger = get_logger('my_app')


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("images/bullet.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.state = "READY"
        self.direction = pygame.math.Vector2(0, -1)

    def update(self):
        self.y -= self.change
        # self.rect.centerx += self.direction.x * self.x_speed
        # self.y -= self.change
        #
        # self.rect.centery += self.direction.x * self.x_speed
        # self.check_sides()
        pass