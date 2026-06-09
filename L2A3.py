import pygame


pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game Screen")

WHITE = (255, 255, 255)    
BLACK = (0, 0, 0)   
RED=(45,45,45)       

rect_width = 400
rect_height = 200
rect_x = (SCREEN_WIDTH - rect_width) // 2
rect_y = (SCREEN_HEIGHT - rect_height) // 2
center_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)


font = pygame.font.Font(None, 36) 
text_surface = font.render("my first game screen", True, BLACK)

text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.fill(WHITE)

    pygame.draw.rect(screen,RED, center_rect)

    screen.blit(text_surface, text_rect)

    pygame.display.flip()
