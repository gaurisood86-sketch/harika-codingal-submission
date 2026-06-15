import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event Color Change")

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(new_color)

sprite1 = Sprite((255, 0, 0), 150, 175)
sprite2 = Sprite((0, 0, 255), 400, 175)

all_sprites = pygame.sprite.Group(sprite1, sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for the custom event
        if event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.change_color()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
