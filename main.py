import pygame
import os
import sys


class SpriteSheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return image


class UnitType:
    WORKER = "Worker"
    TRANSPORTER = "Transporter"


class UnitSprite:
    def __init__(self, image):
        pass


class Unit:
    def __init__(self, unit_type, player=None, position=None, speed=0, health=1):
        self._type = unit_type
        self._player = player
        self._position = position
        self._speed = speed
        self._health = health


class Worker(Unit):
    def __init__(self, player=None, position=None):
        super().__init__(UnitType.WORKER, player, position, 3)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    sprite = pygame.sprite.Sprite()
    sprite_sheet = SpriteSheet('data/img.png')
    img = sprite_sheet.image_at(pygame.Rect(0, 0, 80, 120))
    sprite.image = img
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        # отрисовка и изменение свойств объектов
        all_sprites.draw(screen)

        # обновление экрана
        pygame.display.flip()
    pygame.quit()