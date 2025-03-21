import sys
import pygame
import pygame_gui  # необхідні бібліотеки
import os

pygame.init()

# Путь к корню вашего проекта
project_root = r'C:\Users\mnebr\PycharmProjects\PythonProject'

# Директории, с которыми вы работаете
directories = ['characters', 'maps', 'screenshots', 'sounds']

# Получаем абсолютные пути для каждой из директорий
abs_paths = {dir_name: os.path.join(project_root, dir_name) for dir_name in directories}

# Теперь переменная abs_paths доступна для использования во всех функциях и частях кода
class Labyrinth:  # Класс, выстраивающий лабиринт и отвечающий за навигацию в нём
    def __init__(self, filename, free_tiles, finish_tile):
        """инициализатор класса"""
        self.map = []
        with open(f'{filename}') as input_file:
            for line in input_file:
                self.map.append(list(map(int, line.split())))
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = TILE_SIZE
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen):
        """построение лабиринта"""
        colors = {0: (0, 0, 0), 1: (5, 5, 190), 2: (50, 50, 50)}
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size,
                                   self.tile_size, self.tile_size)
                screen.fill(colors[self.get_tile_id((x, y))], rect)
    def get_tile_id(self, position):
        """вспомогательный метод, возвращающий id тайла"""
        return self.map[position[1]][position[0]]

    def is_free(self, position):
        """вспомогательный метод, возвращающий True/False если клетка свободна/занята"""
        return self.get_tile_id(position) in self.free_tiles
