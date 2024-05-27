from pygame import *

font.init()

window = display.set_mode((800, 600))
display.set_caption('Menu')
clock = time.Clock()
font_txt = font.SysFont('Arial', 36)

menu_options = ['Start', 'Options', 'Exit']  # Removed 'Play' option
selected_option = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (26, 2, 238)
GREEN = (15, 194, 0)

class Button():
    def __init__(self, text, x, y, w, h, color, hover_color):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.hover_color = hover_color

    def draw(self):
        x, y = mouse.get_pos()
        if (self.x < x < self.x + self.w) and (self.y < y < self.y + self.h):
            draw.rect(window, self.hover_color, (self.x, self.y, self.w, self.h))
        else:
            draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
        text = font_txt.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=(self.x + self.w / 2, self.y + self.h / 2))
        window.blit(text, text_rect)

buttons = []

for i, option in enumerate(menu_options):
    button = Button(option, 400 - 100, 200 + i * 50, 200, 50, BLACK, RED)
    buttons.append(button)

start_image = image.load("background.jpg")  # Load your desired image here
start_image_rect = start_image.get_rect(center=(400, 300))  # Position the image at the center of the screen

run = True
game_state = 'menu'
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if game_state == 'menu':
                if e.key == K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif e.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif e.key == K_RETURN:
                    if selected_option == 0:
                        game_state = 'game'
                    elif selected_option == 1:
                        game_state = 'option'
                    elif selected_option == 2:
                        game_state = 'exit'

            if e.key == K_ESCAPE:
                game_state = 'menu'
        if e.type == MOUSEBUTTONDOWN:  # Check if the mouse button is clicked
            if e.button == 1:  # Check if left mouse button is clicked
                if game_state == 'menu':
                    if buttons[selected_option].text == 'Start':
                        game_state = 'start'

    window.fill(BLACK)
    if game_state == 'menu':
        for i, button in enumerate(buttons):
            if i == selected_option:
                button.color = BLUE
            else:
                button.color = BLACK
            button.draw()
    elif game_state == 'options':
        window.fill(WHITE)
        text = font_txt.render('OPTION', True, BLACK)
        window.blit(text, (350, 250))
    elif game_state == 'start':  # Display the image when 'Start' is selected
        window.blit(start_image, start_image_rect)

    display.update()
    clock.tick(30)
