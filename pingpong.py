import pygame
from pygame import *

pygame.mixer.init()
pygame.init()
pygame.font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x , player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height)
  def colliderect(self, rect):
      return self.rect.colliderect(rect)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - self.rect.height - 5:
            self.rect.y += self.speed

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT - self.rect.height - 5:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__(player_image, player_x, player_y, player_speed, player_width, player_height)
        self.speed_x = player_speed
        self.speed_y = player_speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= HEIGHT - self.rect.height:
            self.speed_y *= -1

WIDTH, HEIGHT = 700, 500
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Maze')
background = transform.scale(image.load("background.PNG"), (WIDTH, HEIGHT))

yellow = Player('yellow.png', 30, HEIGHT // 2 - 75, 4, 20, 150)
blue = Player1('blue.png', WIDTH - 50, HEIGHT // 2 - 75, 4, 20, 150)
ball = Ball('ball.png', WIDTH // 2 - 15, HEIGHT // 2 - 15, 4, 30, 30)

mixer.music.load("eruo.mp3")
mixer.music.play()

game_over = False
clock = time.Clock()
FPS = 60
game = True

while game:
    dt = clock.tick(FPS) / 1000.0
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if not game_over:
        window.blit(background, (0, 0))
        yellow.update()
        blue.update()
        ball.update()
        yellow.reset()
        blue.reset()
        ball.reset()
        display.update()

        if ball.rect.colliderect(yellow.rect) or ball.rect.colliderect(blue.rect):
            ball.speed_x *= -1

        if ball.rect.x < 0 or ball.rect.x > WIDTH:
            ball.rect.x = WIDTH // 2 - 15
            ball.rect.y = HEIGHT // 2 - 15
            ball.speed_x *= -1

time.wait(1000)
window.blit(background, (0, 0))
ball.reset()
yellow.reset()
blue.reset()
display.update()

pygame.quit()
quit()