from pygame import *

window = display.set_mode((600, 600))
display.set_caption("ping-pong")
BG = transform.scale(image.load("background.jpg"), (600, 600))
clock = time.Clock()
speed_y = 3
speed_x = 3

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
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            if self.rect.y > 0:
                self.rect.y -= 5 
        elif keys[K_s]:
            if self.rect.y < 410:
                self.rect.y += 5 

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            if self.rect.y > 0:
                self.rect.y -= 5 
        elif keys[K_DOWN]:
            if self.rect.y < 410:
                self.rect.y += 5 

Wall1 = Wall(0, 180, 20, 190)
Wall2 = Wall(570, 180, 20, 190)
ball = transform.scale(image.load("мяч.png"), (80, 80))
ball_rect = ball.get_rect(center=(250, 250))  # Создаем прямоугольник для мяча

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    ball_rect.x += speed_x
    ball_rect.y += speed_y
    
    # Отталкивание мяча от верхней и нижней границ поля
    if ball_rect.y > 520 or ball_rect.y < 0:
        speed_y *= -1
        
    # Проверяем столкновение мяча с ракетками
    if ball_rect.colliderect(Wall1.rect) or ball_rect.colliderect(Wall2.rect):
        speed_x *= -1
        
    window.blit(BG, (0, 0))
    window.blit(ball, ball_rect.topleft)  # Отображаем мяч в новом местоположении
    Player1.update(Wall1)
    Player2.update(Wall2)
    Wall1.reset()
    Wall2.reset()
    display.update()
    clock.tick(60)
