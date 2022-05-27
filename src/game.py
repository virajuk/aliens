import pygame


class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((1600, 900))
        pygame.display.set_caption("ACID RAIN")
        self.background = pygame.image.load("images/background.jpg")
        self.fps = 60
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q):

                    self.running = False

            self.screen.blit(self.background, (0, 0))
            pygame.display.update()
            self.clock.tick(self.fps)

        pygame.quit()
