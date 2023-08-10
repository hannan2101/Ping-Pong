from pygame import *

window = display.set_mode((750, 500))

clock = time.Clock()


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




leftPlayer = Player("neon-blue-rectangle-banner-neon-rectangle-png.jpg", 0, 200, 5, 65 , 150)
rightPlayer = Player("neon-red-rectangle-banner-neon-rectangle-png.jpg",700, 200, 5, 65, 150 )
isRunning = True
while isRunning:
    for e in event.get():
        if e.type == QUIT:
            isRunning = False
    window.fill((0, 0, 0))
    leftPlayer.reset()
    rightPlayer.reset()

    leftPlayer.update_l()
    rightPlayer.update_r()


    display.update()
    clock.tick(40) 
