import pygame

from config import *
from src.builder import Builder
from debug.debug import debug


class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ACID RAIN")
        self.background = pygame.image.load("images/background.jpg")
        self.fps = 60
        self.running = True
        self.clock = pygame.time.Clock()

        self.builder = Builder(self.screen)
        self.over = False

    def run(self):

        while self.running:

            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():

                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q):

                    self.running = False

            self.builder.run()
            pygame.display.update()
            self.clock.tick(self.fps)

        pygame.quit()
