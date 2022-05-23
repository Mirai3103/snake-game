import pygame


class Food:
    def __init__(self, screen):
        self.screen = screen
        self.food = pygame.image.load('./resource/food.png').convert_alpha()
        self.food = pygame.transform.scale(self.food, (20, 20))
        self.x = 60
        self.y = 60

    def draw(self):
        self.screen.blit(self.food, (self.x, self.y))
        pygame.display.flip()
