import pygame
import random

WIDTH = 360
HEIGHT = 480
CELL_P = 0.14  # соотношения ширины клетки и поля
CELL_B = 0.04  # соотношение расстояния между клетками и ширины поля
CELL_C = (5, 6)  # количество клеток в ряду, столбце

pygame.display.set_icon(pygame.image.load("data/icon.bmp"))
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("memory puzzle")

bg_img = pygame.image.load('data/bg.bmp')

# словарь цветов
colors = {1: (255, 0, 0),
          2: (255, 130, 0),
          3: (255, 255, 0),
          4: (200, 255, 0),
          5: (0, 255, 0),
          6: (0, 255, 255),
          7: (0, 0, 255),
          8: (130, 0, 255),
          9: (255, 0, 255),
          10: (255, 0, 170)}

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Color_Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([CELL_P * WIDTH, CELL_P * WIDTH])
        self.image.fill(colors[color])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([CELL_P * WIDTH, CELL_P * WIDTH], pygame.SRCALPHA)
        self.image.fill((255, 255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            self.image.fill((255, 255, 255, 0))

        screen.blit(self.image, self.rect)


# цвет клетки
col_ind = [(i, j) for i in range(CELL_C[0]) for j in range(CELL_C[1])]
random.shuffle(col_ind)

all_color_cells = pygame.sprite.Group()
for k in range(len(col_ind)):
    i, j = col_ind[k]
    color_cell = Color_Cell(WIDTH * CELL_P * i + (i + 1) * CELL_B * WIDTH,
                            WIDTH * CELL_P * j + (j + 1) * CELL_B * WIDTH, k // 3 + 1)
    all_color_cells.add(color_cell)

# состояние клетки
data_stat = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

all_cells = pygame.sprite.Group()
for i in range(CELL_C[0]):
    for j in range(CELL_C[1]):
        cell = Cell(WIDTH * CELL_P * i + (i + 1) * CELL_B * WIDTH,
                    WIDTH * CELL_P * j + (j + 1) * CELL_B * WIDTH)
        all_cells.add(cell)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_cells.update()
    screen.blit(bg_img, (0, 0))
    all_color_cells.draw(screen)
    all_cells.draw(screen)
    pygame.display.flip()

pygame.quit()
