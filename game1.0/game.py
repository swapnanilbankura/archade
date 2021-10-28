import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()
mixer.init()
# create the screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('images/Bg7.jpeg')
background=pygame.transform.scale(background,(800,600))

#music
music=pygame.mixer.Sound('New folder/bgmusic.wav')
music.play(-1)
# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('images/Bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


#scoreicon



icon=pygame.image.load('images/Trophy.png')
icon=pygame.transform.scale(icon,(64,64))

textX = 10
testY = 10
#tokenicon



icon2=pygame.image.load('images/coin.png')
icon2=pygame.transform.scale(icon2,(64,64))

textX3 = 200
testY3 = 10
#score
score_value=0
font = pygame.font.Font('freesansbold.ttf', 32)

textX2 = 80
testY2= 30

#Token
token_value=0
font = pygame.font.Font('freesansbold.ttf', 32)

textX1 = 280
testY1= 30

#exit and playagain
exit_img=pygame.image.load('images/exit button.png').convert_alpha()
exit_img=pygame.transform.scale(exit_img,(72,40))
replay_img=pygame.image.load('images/playagain.png').convert_alpha()
replay_img=pygame.transform.scale(replay_img,(72,40))

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
#buttonclass
class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topright=(x,y)
        self.clicked=False
    def draw(self):
        action=False
        #get mouse position
        pos=pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False
            
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action
exit_button=Button(750,10,exit_img)
replay_button=Button(600,10,replay_img)

def icon1(x,y):
    screen.blit(icon, (x, y))
def tokenicon(x,y):
    screen.blit(icon2, (x, y))

def show_score(x, y):
    score = font.render(" : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_token(x, y):
    token = font.render(" : " + str(token_value), True, (255, 255, 255))
    screen.blit(token, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    music.stop()
    game_over1=pygame.mixer.Sound('New folder/gameover.wav')
    game_over1.play(0)
    pygame.time.wait(int(game_over1.get_length()*1000))
    
    

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

    

# It is better to make a function called insert_image which takes a image and x, y coordinate. That would reduce several lines. For enemy, the input image could just be enemyImg[i] rather than being a seperate function


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop

running = True
while running:
    
    
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    exit_button.draw()
    replay_button.draw()
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.7
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    
                   
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    if exit_button.draw():
        
        for j in range(num_of_enemies):
                enemyY[j] = 2000
        game_over_text()
    if replay_button.draw():
        for event in pygame.event.get():
             
            running = True
        

        
        
        

        
    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            
          
            for j in range(num_of_enemies):
                
                enemyY[j] = 2000
           
            
            
            game_over_text()
            
            
        

        
            
            break
            

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            
            
            bulletY = 480
            bullet_state = "ready"
            score_value += 10
            
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
            score=str(score_value)
            l=len(score)
            if l>=3:
                token_value=15*int(score[0:(l-2)])


            

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    

    player(playerX, playerY)
    icon1(textX, testY)
    show_token(textX1, testY1)
    show_score(textX2, testY2)
    tokenicon(textX3, testY3)

    pygame.display.update()