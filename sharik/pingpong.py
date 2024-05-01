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
    def __init__(self, x, y, w, h, color=(79, 79, 79)):
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
x1, y1 = 100, 300
x2, y2 = 100, 400

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    key_pressed = key.get_pressed()
    if key_pressed[K_w] and y1 > 0:
        y1 -= 5
    if key_pressed[K_s] and y1 < 520:
        y1 += 5
    if key_pressed[K_d] and x1 < 520:
        x1 += 5
    if key_pressed[K_a] and x1 > 0:
        x1 -= 5
    

    if key_pressed[K_UP] and y2 > 0:
        y2 -= 5
    if key_pressed[K_DOWN] and y2 < 520:
        y2 += 5
    if key_pressed[K_RIGHT] and x2 < 520:
        x2 += 5
    if key_pressed[K_LEFT] and x2 > 0:
        x2 -= 5

    window.blit(BG, (0, 0))
    Wall1.reset(x1, y1)
    Wall2.reset(x2, y2)
    display.update()
    clock.tick(60)





