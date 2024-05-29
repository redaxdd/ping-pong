from pygame import *
import json

width, height = 800, 600
window = display.set_mode((width, height))
display.set_caption("game") 
clock = time.Clock()

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player:
    def __init__(self, w, h):
        self.w = 50
        self.h = 50
        self.x = w // 2 - self.w // 2
        self.y = h - self.h
        self.speed = 5
        self.jump = False
        self.jump_count = 0
    
    def draw(self):
        draw.rect(window, BLUE, (self.x, self.y, self.w, self.h))
    
    def move(self, keys):
        if keys[K_d]:
            self.x += self.speed
        if keys[K_a]:
            self.x -= self.speed
        if keys[K_SPACE] and not self.jump:
            self.jump_count = 20
            self.jump = True
            
    def update(self):
        if self.jump_count > 0:
            self.y -= 15
            self.jump_count -= 1
        for platform in platforms:
            if self.y + self.h >= platform.y and self.y + self.h < platform.y + 10 \
                    and self.x + self.w >= platform.x and self.x <= platform.x + platform.w:
                self.y = platform.y - self.h
                self.jump = False
        self.y += 10 * (self.y / (height - self.h))
        if self.y > height - self.h:
            self.y = height - self.h
            self.jump = False

class Platform:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def draw(self):
        draw.rect(window, BLUE, (self.x, self.y, self.w, self.h))

class Goal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 50
        self.h = 50
    
    def draw(self):
        draw.rect(window, BLUE, (self.x, self.y, self.w, self.h))
    
    def update(self):
        global lvls, platforms, current_level
        if player.x + player.w >= self.x and player.x <= self.x + self.w \
                and player.y + player.h >= self.y and player.y <= self.y + self.h:
            print('LEVEL COMPLETE')
            current_level += 1
            if current_level < len(lvls):
                platforms.clear()
                for d in lvls[current_level]['platforms']:
                    platform = Platform(d['x'], d['y'], d['w'], d['h'])
                    platforms.append(platform)
                goal.x = lvls[current_level]['goal']['x']
                goal.y = lvls[current_level]['goal']['y']
                player.x = width // 2 - self.w // 2
                player.y = height - self.h
            else:
                print("Game completed!")
                quit()

with open('levels.json') as f:
    lvls = json.load(f)

platforms = []
current_level = 0
for d in lvls[current_level]['platforms']:
    platform = Platform(d['x'], d['y'], d['w'], d['h'])
    platforms.append(platform)

goal = Goal(lvls[current_level]['goal']['x'], lvls[current_level]['goal']['y'])
player = Player(width, height)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    keys = key.get_pressed()
    
    window.fill(WHITE)
    
    for platform in platforms:
        platform.draw()
    
    goal.draw()
    player.move(keys)
    player.update()
    player.draw()
    
    display.update()
    clock.tick(FPS)
