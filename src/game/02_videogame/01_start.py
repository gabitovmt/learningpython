import pygame
import sys

"""
Переменные
"""

worldx = 960
worldy = 720
fps = 40
ani = 4  # Циклы анимации
main = True

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

"""
Объекты
"""

"""
Настройка
"""

clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode((worldx, worldy))

"""
Главный цикл
"""

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == ord('q')):
            pygame.quit()
            sys.exit()

    world.fill(BLUE)
    pygame.display.flip()
    clock.tick(fps)
