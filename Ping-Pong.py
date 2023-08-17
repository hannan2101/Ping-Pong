from pygame import *
import time as t
from pygame import mixer
mixer.init()
clock = time.Clock()
window = display.set_mode((750, 500))

#Icon and Caption
display.set_caption("Ping-Pong")
icon = image.load('e.png')
display.set_icon(icon)

font.init()
font = font.Font(None, 30)
lscore = 0
rscore = 0
leftScore = font.render("Player 1: 0", True, (0, 0, 255))
rightScore = font.render("Player 2: 0", True, (255, 0, 0))


class GameSprite(sprite.Sprite):
    # class constructor
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()

        # every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed

        # every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Players attributes
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and leftPlayer.rect.y > 0:
            leftPlayer.rect.y -= leftPlayer.speed
        if keys_pressed[K_s] and leftPlayer.rect.y + leftPlayer.rect.height < 500:
            leftPlayer.rect.y += leftPlayer.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and rightPlayer.rect.y > 0:
           rightPlayer.rect.y -= rightPlayer.speed
        if keys_pressed[K_DOWN] and rightPlayer.rect.y + leftPlayer.rect.height < 500:
           rightPlayer.rect.y += rightPlayer.speed

#Ball attributes 
class Ball(GameSprite):
    def update_ball(self):
        global dx
        global dy
        self.rect.y -= dy
        self.rect.x -= dx
        self.checkPoint()
        if ball.rect.y <= 0 or ball.rect.y +50 >= 500:
            dy *= -1
            Collsion_sound = mixer.Sound('bounce.wav')
            Collsion_sound.play()
        if sprite.collide_rect(leftPlayer,ball) or sprite.collide_rect(rightPlayer,ball):
            dx *= -1
            Collsion_sound = mixer.Sound('bounce.wav')
            Collsion_sound.play()

        

    def checkPoint(self):
       global start_time
       global lscore
       global rscore
       global leftScore
       global rightScore
       if self.rect.x < 0 or self.rect.right > 750:
           if self.rect.x < 0:
               rscore += 1
           else:
               lscore += 1
           self.rect.x = 300
           self.rect.y = 250
           leftScore = font.render("Player 1: " + str(lscore), True, (0, 0, 255))
           rightScore = font.render("Player 2: " + str(rscore), True, (255, 0, 0))
           start_time = t.time()
            
        
 
dx = 8
#speed of ball in x direction
dy = 8
#speed of ball in y direction

ball = Ball("e.png", 300, 200, 1, 50, 50)
leftPlayer = Player("neon-blue-rectangle-banner-neon-rectangle-png.jpg", -15, 200, 5, 65 , 150)
rightPlayer = Player("neon-red-rectangle-banner-neon-rectangle-png.jpg",700, 200, 5, 65, 150 )
isRunning = True
start_time = t.time()

#Gameloop
while isRunning:
    for e in event.get():
        if e.type == QUIT:
            isRunning = False
    window.fill((0, 0, 0))
    leftPlayer.reset()
    rightPlayer.reset()
    ball.reset()
    if t.time() - start_time >= 3:
        ball.update()
    leftPlayer.update_l()
    rightPlayer.update_r()
    ball.update_ball()

    window.blit(leftScore, (150, 50))
    window.blit(rightScore, (300, 50)) 

    display.update()
    clock.tick(40) 
