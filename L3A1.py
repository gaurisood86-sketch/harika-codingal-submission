import pygame
import random

pygame.init()
SPRITE_COLOR_CHANGE_EVENT=pygame.USEREVENT +1
BACKGROUND_COLOR_CHANGE_EVENT=pygame.USEREVENT +2

LIGHTBLUE = pygame.Color('lightblue')
BLUE = pygame.Color('blue')
DARKBLUE = pygame.Color('darkblue')

MAGENTA = pygame.Color('magenta')
YELLOW = pygame.Color('yellow')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([height, width])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[1]= -self.velocity[1]
            boundary_hit=True

        if boundary_hit:
            pygame.every.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.every.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([YELLOW,MAGENTA,ORANGE,WHITE]))

    def change_background_color():
        