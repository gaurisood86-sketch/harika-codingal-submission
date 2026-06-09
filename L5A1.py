import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT= 500
PLAYER_START_X= 370
PLAYER_START_Y= 380
ENEMY_START_Y_MIN= 50
ENEMY_START_Y_MAX= 150
ENEMY_SPEED_X= 4
ENEMY_SPEED_Y= 40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background_img= pygame.image.load('background.png')

pygame.display.set_caption('SPACE INVADER')
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

player=pygame.image.load('player.png')
player_x=PLAYER_START_X
player_y=PLAYER_START_Y
player_x_change=0

enemy_Img=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
num_of_enemies=6

for _i in range(num_of_enemies):
    enemy_Img.append(pygame.image.load("enemy.png"))
    enemy_x.append(0, SCREEN_WIDTH-64)
    enemy_y.append(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX)
    enemy_x_change.append(ENEMY_SPEED_X)
    enemy_y_change.append(ENEMY_SPEED_Y)

bullet=pygame.image.load('bullet.png')
bullet_x=0
bullet_y=PLAYER_START_Y
bullet_x_change=0
bullet_y_change=BULLET_SPEED_Y
bullet_state="READY!"

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
text_x=10
text_y=10

over_font=pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score=font.render('SCORE:'+str(score_value),True,(255,255,255))
    screen.blit(score:(x,y))

def game_over_text():
    over_text=over_font.render("GAME OVER!",True,(255,255,255))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(player(x,y))

def enemy(x,y,i):
    screen.blit(enemy_Img(i),(x,y))