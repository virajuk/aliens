import random

import pygame

from config import *
from debug.debug import debug
from src.bug import Bug
from src.ship import Ship

from logs import get_logger
logger = get_logger('my_app')


class Builder:

    def __init__(self):

        self.display_surf = pygame.display.get_surface()

        self.bug_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.ship_sprites = pygame.sprite.Group()

        self.add_ship()

        self.no_of_bugs = 6
        self.add_bug()

    def run(self):

        self.bug_sprites.draw(self.display_surf)
        self.ship_sprites.draw(self.display_surf)
        self.ship_sprites.update()

    def add_bug(self):

        pos = (random.randint(0, WIDTH - 64), random.randint(50, int(HEIGHT*0.1)))
        bug = Bug(pos)
        if not self.check_collision(bug):
            bug.add(self.bug_sprites)
        else:
            self.add_bug()

    def add_bugs(self):

        for idx in range(0, self.no_of_bugs):
            self.add_bug()

    def check_collision(self, bug):

        for bug_sprite in self.bug_sprites:
            if bug_sprite.rect.colliderect(bug):
                return True
        return False

    def add_ship(self):

        pos = (int(WIDTH/2) - 32, HEIGHT - 64)
        ship = Ship(pos)
        ship.add(self.ship_sprites)