import pygame

class Role:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/mario.jpeg')
        self.image = pygame.transform.scale(self.image, (150, 200))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)