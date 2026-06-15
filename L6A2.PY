import pygame
import random
import math

pygame.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("ALIEN INVADER!")

background_img=pygame.image.load('background.png')
enemy_img=pygame.image.load('enemy.png')
bullet_img=pygame.image.load('bullet.png')
player_img=pygame.image.load('player.jpg')

player_x=320
player_y=520
player_x_change=0

enemy_x=random.randint(0,736)
enemy_y=random.randint(50,150)
enemy_y_change=3

bullet_x=0
bullet_y=520
bullet_y_change=10
bullet_state="ready!"


score=0
font=pygame.font.Font(None,36)
timer_font=pygame.font.Font(None,36)

total_ticks=120
start_ticks=pygame.time.get_ticks() 

def show_score():
    value=font.render('score:'+ str(score), True, (255,255,255))
    screen.blit(value,(10,10))

def show_timer(time_left):
    timer_text=timer_font.render('TIME LEFT:'+ str(time_left), True, (255,255,255))
    screen.blit(timer_text,(650,10))

def player(x,y):
    screen.blit(player_img,(x,y))

def enemy(x,y):
    screen.blit(enemy_img,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="FIRE!"
    screen.blit(bullet_img,(x+16,y+19))

def isCollision(ex,ey,bx,by):
    distance=math.sqrt((ex-bx)**2+(ey-by)**2)
    return distance < 27

running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background_img,(0,0))

    seconds_passed=(pygame.time.get_ticks()-start_ticks)//1000
    time_left=total_ticks-seconds_passed

    if time_left<=0:
        running=False

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
          running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
             player_x_change=-6

            if event.key==pygame.K_RIGHT:
             player_x_change=6

            if event.type==pygame.K_SPACE and bullet_state=="ready!":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change=0

    player_x += player_x_change
    player_x=max(0,min(player_x,736))

    enemy_y += enemy_y_change

    if enemy_y >600:
        enemy_x=random.randint(0,736)
        enemy_y=random.randint(50,150)

    if isCollision(enemy_x,enemy_y,bullet_x,bullet_y):
        bullet_y=520
        bullet_state="ready!"
        score +=1
        enemy_x=random.randint(0,736)
        enemy_y=random.randint(50,150)

    if bullet_y =="fire!":
        fire_bullet(bullet_x,bullet_y)
        bullet_y-=bullet_y_change

    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    show_score()
    show_timer(time_left)

    pygame.display.update()

pygame.quit



        
