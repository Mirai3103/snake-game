import pygame
from constant import SIZE, BACKGROUND, SQUARE_RECT, SQUARE_COLOR, SQUARE_X2, SQUARE_Y2, SQUARE_Y1, SQUARE_X1
import copy


class SnakeBodyStatus:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


class Snake:
    def __init__(self, screen):
        self.length = 2
        self.step = SIZE
        self.screen = screen
        head_right = pygame.image.load('./resource/snakehead.png').convert_alpha()
        head_right = pygame.transform.scale(head_right, (SIZE, SIZE))
        self.head = {
            'right': head_right,
            'left': pygame.transform.rotate(head_right, 180),
            'up': pygame.transform.rotate(head_right, 90),
            'down': pygame.transform.rotate(head_right, 270)
        }
        body_horizontal = pygame.image.load('./resource/snakebody.png').convert_alpha()
        body_horizontal = pygame.transform.scale(body_horizontal, (SIZE, SIZE))
        self.body = {
            'right': body_horizontal,
            'left': body_horizontal,
            'up': pygame.transform.rotate(body_horizontal, 90),
            'down': pygame.transform.rotate(body_horizontal, 90)
        }
        last_body_right = pygame.image.load('./resource/lastbody.png').convert_alpha()
        last_body_right = pygame.transform.scale(last_body_right, (SIZE, SIZE))
        self.last_body = {
            'right': last_body_right,
            'left': pygame.transform.rotate(last_body_right, 180),
            'up': pygame.transform.rotate(last_body_right, 90),
            'down': pygame.transform.rotate(last_body_right, 270)
        }

        self.locations = [SnakeBodyStatus(120, 120, 'right'), SnakeBodyStatus(120, 120, 'right')]
        self.direction = 'right'

    def append(self):
        self.length += 1
        self.locations.append(copy.copy(self.locations[self.length - 2]))

    def is_eat_itself(self):
        if self.length > 3:
            for i in range(3, self.length):
                if self.locations[0].x == self.locations[i].x and self.locations[0].y == self.locations[i].y:
                    return True
        return False

    def draw(self):
        self.screen.fill(BACKGROUND)
        pygame.draw.rect(self.screen, SQUARE_COLOR, pygame.Rect(SQUARE_RECT), 2)
        for i in range(self.length):
            if i == 0:
                self.screen.blit(self.head[self.locations[i].direction], (self.locations[i].x, self.locations[i].y))
            elif i == self.length - 1:
                self.screen.blit(self.last_body[self.locations[i].direction],
                                 (self.locations[i].x, self.locations[i].y))
            else:
                self.screen.blit(self.body[self.locations[i].direction], (self.locations[i].x, self.locations[i].y))
        pygame.display.flip()

    def move_left(self):
        if self.locations[0].direction != 'right':
            self.locations[0].direction = 'left'

    def move_right(self):
        if self.locations[0].direction != 'left':
            self.locations[0].direction = 'right'

    def move_up(self):
        if self.locations[0].direction != 'down':
            self.locations[0].direction = 'up'

    def move_down(self):
        if self.locations[0].direction != 'up':
            self.locations[0].direction = 'down'

    def is_eat_square(self):
        if self.locations[0].x < SQUARE_X1 or self.locations[0].y < SQUARE_Y1 or self.locations[0].x > SQUARE_X2 or \
                self.locations[0].y > SQUARE_Y2:
            return True
        return False

    def run(self):
        for i in range(self.length - 1, 0, -1):
            self.locations[i].x = self.locations[i - 1].x
            self.locations[i].y = self.locations[i - 1].y
            self.locations[i].direction = self.locations[i - 1].direction
        if self.locations[0].direction == 'right':
            self.locations[0].x += self.step
        elif self.locations[0].direction == 'left':
            self.locations[0].x -= self.step
        elif self.locations[0].direction == 'up':
            self.locations[0].y -= self.step
        elif self.locations[0].direction == 'down':
            self.locations[0].y += self.step
        self.draw()
