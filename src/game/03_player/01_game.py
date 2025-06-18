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


class Player(pygame.sprite.Sprite):
    """
    Создание главного персонажа
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(0, 8):
            img = pygame.image.load(f'images/walk-{i}.png').convert()
            img.convert_alpha()  # Оптимизация альфа-диапазона
            # Все пиксели, цвет которых совпадает с переданным в set_colorkey() значением, станут прозрачными
            img.set_colorkey(0)
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


"""
Настройка
"""

clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode((worldx, worldy))

player = Player()
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)

"""
Главный цикл
"""

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == ord('q')):
            pygame.quit()
            sys.exit()

    world.fill(BLUE)
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
