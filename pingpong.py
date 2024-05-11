from pygame import *

window = display.set_mode((600, 600))
display.set_caption("ping-pong")
BG = transform.scale(image.load("background.jpg"), (600, 600))
clock = time.Clock()
speed_y = 1
speed_x = 1

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, filename, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Wall(sprite.Sprite):
    def __init__(self, x, y, w, h, color=(12, 79, 79)):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update():
        keys = key.get_pressed()
        if keys[K_w]:
            if Wall1.rect.y > 0:
                Wall1.rect.y -= 5 
        elif keys[K_s]:
            if Wall1.rect.y < 410:
                Wall1.rect.y += 5 
class Player2(GameSprite):
    def update():
        keys = key.get_pressed()
        if keys[K_UP]:
            if Wall2.rect.y > 0:
                Wall2.rect.y -= 5 
        elif keys[K_DOWN]:
            if Wall2.rect.y < 410:
                Wall2.rect.y += 5 

Wall1 = Wall(0, 180, 20, 190)
Wall2 = Wall(570, 180, 20, 190)
ball = transform.scale(image.load("мяч.png"), (80, 80))

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            if finish != True:
                ball.rect.x += speed_x
                ball.rect.y += speed_y
            if ball.rect.y > win_height-50 or ball.rect.y < 0:
                speed_y *= -1
            if sprite.collide_rect(Wall1, ball) or sprite.collide_rect(Wall2, ball):
                speed_x *= -1
    window.blit(BG, (0, 0))
    window.blit(ball, (250, 250))
    Player1.update()
    Player2.update()
    Wall1.reset()
    Wall2.reset()
    display.update()
    clock.tick(60)