import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = pygame.transform.scale(
    pygame.image.load('images.jpg').convert_alpha(), (300, 300))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,
    SCREEN_HEIGHT // 2 ))


text = pygame.font.Font(None, 36).render('my first pygame screen ', True,
    pygame.Color('white'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pygame.display.flip()


