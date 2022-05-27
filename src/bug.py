import pygame

from config import *
from logs import get_logger
logger = get_logger('my_app')


class Bug(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("images/bug.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
