import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Unit:
    def __init__(self, board_position=None, unit_type=0):
        self.all_sprites = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image("hat.png")
        sprite.rect = sprite.image.get_rect()
        self.all_sprites.add(sprite)

    def draw(self, screen):
        self.all_sprites.draw(screen)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    unit = Unit()

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        # отрисовка и изменение свойств объектов
        unit.draw(screen)

        # обновление экрана
        pygame.display.flip()
    pygame.quit()