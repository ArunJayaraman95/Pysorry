import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 850


# Color List
c = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (30, 30, 30)
}
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND_COLOR = (200, 200, 200)
OFFSET = 30
screen.fill(BACKGROUND_COLOR)
run = True
BOARD_LENGTH = 800
square_size = BOARD_LENGTH/16
# Draw board (16 by 16)


  
# Draw Board
# ==============================
def draw_board():
    for i in range(17):
        pygame.draw.line(screen, c["black"], (OFFSET, i * square_size + OFFSET), (OFFSET + BOARD_LENGTH, i * square_size + OFFSET), 2)


    for i in range(17):
        pygame.draw.line(screen, c["black"], (i * square_size + OFFSET, OFFSET), (i * square_size + OFFSET, OFFSET + BOARD_LENGTH), 2) 

    pygame.draw.rect(screen, BACKGROUND_COLOR, (OFFSET + square_size + 2, square_size + 30 + 2, square_size * 14 - 2, square_size * 14 - 2))
# ===============================

POSITION_LIST = [0] * 60

for i in range(16):
    off_x = OFFSET + square_size/2 + square_size * i
    off_y = OFFSET + square_size/2

    POSITION_LIST[i] = (off_x, off_y)

for i in range(16, 31):
    off_x = OFFSET + square_size/2 + square_size * 15
    off_y = OFFSET + square_size/2 + square_size * (i - 15)
    POSITION_LIST[i] = (off_x, off_y)

for i in range(31, 46):
    off_x = OFFSET + square_size/2 + square_size * 15 - square_size * (i - 30)
    off_y = OFFSET + square_size/2 + square_size * 15
    POSITION_LIST[i] = (off_x, off_y)

for i in range(46, 60):
    off_x = OFFSET + square_size/2
    off_y = OFFSET + square_size/2 + square_size * 15 - square_size * (i - 45)
    POSITION_LIST[i] = (off_x, off_y)



# pygame.draw.rect(screen, colors["green"], pygame.Rect(30, 30, 60, 60), 5)
index = 0
draw_board()
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            draw_board()
            index = (index + 1) % 60
            pygame.draw.circle(screen, c["red"], POSITION_LIST[index], 20)

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()