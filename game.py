import pygame
from snake import Snake
from food import Food
import random
import time


class Game:
    def __init__(self):
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('Snake Game')
        pygame.display.flip()
        self.snake = Snake(self.screen)
        self.snake.draw()
        self.food = Food(self.screen)
        self.food.draw()

    def is_collision(self):
        if self.snake.x[0] == self.food.x and self.snake.y[0] == self.food.y:
            return True
        return False

    def random_food(self):
        self.food.x = random.randint(0, 7) * self.snake.step
        self.food.y = random.randint(0, 7) * self.snake.step
        for i in range(self.snake.length):
            if self.food.x == self.snake.x[i] and self.food.y == self.snake.y[i]:
                self.random_food()
    def show_game_over(self):
        self.screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        text = font.render('Game Over', True, (255, 0, 0))
        self.screen.blit(text, (300, 300))
        pygame.display.flip()
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.snake.move_right()
                    elif event.key == pygame.K_UP:
                        self.snake.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.snake.move_down()
            pygame.display.flip()
            self.snake.run()
            self.food.draw()
            if self.is_collision():
                self.random_food()
                self.snake.append()
            if self.snake.is_eat_itself():
                self.show_game_over()
                time.sleep(10)
            time.sleep(0.1)
