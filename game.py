import pygame
from snake import Snake
from food import Food
import random
import time
from constant import BACKGROUND, SQUARE_RECT, SQUARE_COLOR, SPEED


class Game:
    def __init__(self):
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.screen.fill(BACKGROUND)
        pygame.draw.rect(self.screen, SQUARE_COLOR, pygame.Rect(SQUARE_RECT), 2)
        pygame.display.set_caption('Snake Game')
        pygame.display.flip()
        self.snake = Snake(self.screen)
        self.snake.draw()
        self.food = Food(self.screen)
        self.food.draw()
        self.is_pause = False

    def is_collision(self):
        if self.snake.locations[0].x == self.food.x and self.snake.locations[0].y == self.food.y:
            return True
        return False

    def random_food(self):
        self.food.x = random.randint(60, 520) // 20 * 20
        self.food.y = random.randint(60, 520) // 20 * 20
        for i in range(self.snake.length):
            if self.food.x == self.snake.locations[i].x and self.food.y == self.snake.locations[i].y:
                self.random_food()

    def show_game_over(self):
        self.screen.fill(BACKGROUND)
        font = pygame.font.Font(None, 48)
        text_game_over = font.render('Game Over', True, (255, 0, 0))
        self.screen.blit(text_game_over, (200, 200))
        text_show_score = font.render('Score: ' + str(self.snake.length-2), True, (66, 245, 108))
        self.screen.blit(text_show_score, (220, 250))
        text_continue = pygame.font.Font(None, 20).render('Press space to continue', True, (245, 242, 66))
        self.screen.blit(text_continue, (210, 300))
        pygame.display.flip()
        while self.is_pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.is_pause = False
                        self.reset()
                if event.type == pygame.QUIT:
                    self.is_pause = False
                    self.running = False

    def reset(self):
        self.snake = Snake(self.screen)
        self.snake.draw()
        self.food = Food(self.screen)
        self.food.draw()

    def show_score(self):
        font = pygame.font.Font(None, 28)
        text = font.render('Score: ' + str(self.snake.length-2), True, (66, 135, 245))
        self.screen.blit(text, (20, 20))
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
            self.show_score()
            if self.is_collision():
                self.random_food()
                self.snake.append()
            if self.snake.is_eat_itself() or self.snake.is_eat_square():
                self.is_pause = True
                self.show_game_over()

            time.sleep(SPEED)
