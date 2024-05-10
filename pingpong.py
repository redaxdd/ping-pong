from pygame import *

window = display.set_mode((600, 600))
display.set_caption("ping-pong")
BG = transform.scale(image.load("background.jpg"), (600, 600))
clock = time.Clock()

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

Wall1 = Wall(0, 180, 20, 190)
Wall2 = Wall(570, 180, 20, 190)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    # Получаем состояние клавиш
    keys = key.get_pressed()
    
    # Управление для Wall1 (W - вверх, S - вниз)
    if keys[K_w]:
        if Wall1.rect.y > 0:
            Wall1.rect.y -= 5  # Изменяем положение на 5 вверх
    elif keys[K_s]:
        if Wall1.rect.y < 410:
            Wall1.rect.y += 5  # Изменяем положение на 5 вниз
    
    # Управление для Wall2 (стрелка вверх - вверх, стрелка вниз - вниз)
    if keys[K_UP]:
        if Wall2.rect.y > 0:
            Wall2.rect.y -= 5  # Изменяем положение на 5 вверх
    elif keys[K_DOWN]:
        if Wall2.rect.y < 410:
            Wall2.rect.y += 5  # Изменяем положение на 5 вниз
    
    window.blit(BG, (0, 0))
    Wall1.reset()
    Wall2.reset()
    display.update()
    clock.tick(60)





