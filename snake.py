import pygame


class Snake:
    def __init__(self, screen):
        self.length = 1
        self.step = 20
        self.screen = screen
        self.block = pygame.image.load('./resource/block.png').convert()
        self.block = pygame.transform.scale(self.block, (20, 20))
        self.x = [20] * self.length
        self.y = [20] * self.length
        self.direction = 'right'

    def append(self):
        self.length += 1
        self.x.append(self.x[0])
        self.y.append(self.x[0])

    def is_eat_itself(self):
        for i in range(3, self.length):
            if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                return True
        return False

    def draw(self):
        self.screen.fill((255, 255, 255))
        for i in range(self.length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def reset_location(self):
        if self.x[0] > self.screen.get_width():
            self.x[0] = 0
        if self.x[0] < 0:
            self.x[0] = self.screen.get_width()
        if self.y[0] < 0:
            self.y[0] = self.screen.get_height()
        if self.y[0] > self.screen.get_height():
            self.y[0] = 0

    def run(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'right':
            self.x[0] += self.step
        elif self.direction == 'left':
            self.x[0] -= self.step
        elif self.direction == 'up':
            self.y[0] -= self.step
        elif self.direction == 'down':
            self.y[0] += self.step
        self.reset_location()
        self.draw()
