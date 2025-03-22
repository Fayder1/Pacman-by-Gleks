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
    def find_path_step(self, start, target, direction):
        """алгоритм построения маршрута для призраков (поиск следующего тайла)"""
        x, y = start
        xt, yt = target
        tile_list = []
        distance = []
        if direction == 'up':
            if self.is_free((x, y - 1)):
                tile_list.append((x, y - 1))
            if self.is_free((x - 1, y)):
                tile_list.append((x - 1, y))
            if self.is_free((x + 1, y)): tile_list.append((x + 1, y))
        if direction == 'down':
            if self.is_free((x - 1, y)):
                tile_list.append((x - 1, y))
            if self.is_free((x, y + 1)):
                tile_list.append((x, y + 1))
            if self.is_free((x + 1, y)):
                tile_list.append((x + 1, y))
        if direction == 'right':
            if self.is_free((x, y - 1)):
                tile_list.append((x, y - 1))
            if self.is_free((x, y + 1)):
                tile_list.append((x, y + 1))
            if self.is_free((x + 1, y)):
                tile_list.append((x + 1, y))
        if direction == 'left':
            if self.is_free((x, y - 1)):
                tile_list.append((x, y - 1))
            if self.is_free((x - 1, y)):
                tile_list.append((x - 1, y))
            if self.is_free((x, y + 1)):
                tile_list.append((x, y + 1))
        for tile in tile_list:
            xn, yn = tile
            distance.append(abs(xn - xt) ** 2 + abs(yn - yt) ** 2)
        return tile_list[distance.index(min(distance))]












        """Моя частина"""
    def update_direct_pacman(self):
        """метод, выставляющий следующее направление пакмена, если такой поворот возможен"""
        next_x, next_y = self.pacman.get_position()
        if self.pacman.get_next_dir() == 'up':
            if self.labyrinth.is_free((next_x, next_y - 1)):
                self.pacman.set_curr_dir('up')
        if self.pacman.get_next_dir() == 'down':
            if self.labyrinth.is_free((next_x, next_y + 1)):
                self.pacman.set_curr_dir('down')
        if self.pacman.get_next_dir() == 'right':
            if self.labyrinth.is_free((next_x + 1, next_y)):
                self.pacman.set_curr_dir('right')
        if self.pacman.get_next_dir() == 'left':
            if self.labyrinth.is_free((next_x - 1, next_y)):
                self.pacman.set_curr_dir('left')

        if self.pacman.get_curr_dir() == 'up':
            next_y -= 1
        if self.pacman.get_curr_dir() == 'down':
            next_y += 1
        if self.pacman.get_curr_dir() == 'right':
            next_x += 1
        if self.pacman.get_curr_dir() == 'left':
            next_x -= 1
        if self.labyrinth.is_free((next_x, next_y)):
            self.pacman.set_position((next_x, next_y))

    def move_red(self):
        """метод перемещения красного призрака"""
        target = self.pacman.get_position()
        next_position = self.labyrinth.find_path_step(self.red.get_position(), target,
                                                      self.red.get_direction())
        self.red.set_direction(find_direction(self.red.get_position(), next_position))
        self.red.set_position(next_position)
        self.red.update_image()


    def move_pink(self):
        """метод перемещения розового призрака"""
        direction = self.pacman.get_curr_dir()
        target = ()
        if direction == 'up':
            target = self.pacman.get_position()[0] - 4, self.pacman.get_position()[1] - 4
        if direction == 'down':
            target = self.pacman.get_position()[0], self.pacman.get_position()[1] + 4
        if direction == 'right':
            target = self.pacman.get_position()[0] + 4, self.pacman.get_position()[1]
        if direction == 'left':
            target = self.pacman.get_position()[0] - 4, self.pacman.get_position()[1]
        next_position = self.labyrinth.find_path_step(self.pink.get_position(), target,
                                                      self.pink.get_direction())
        self.pink.set_direction(find_direction(self.pink.get_position(), next_position))
        self.pink.set_position(next_position)
        self.pink.update_image()

    def move_blue(self):
        """метод перемещения голубого призрака"""
        direction = self.pacman.get_curr_dir()
        center = ()
        if direction == 'up':
            center = self.pacman.get_position()[0] - 2, self.pacman.get_position()[1] - 2
        if direction == 'down':
            center = self.pacman.get_position()[0], self.pacman.get_position()[1] + 2
        if direction == 'right':
            center = self.pacman.get_position()[0] + 2, self.pacman.get_position()[1]
        if direction == 'left':
            center = self.pacman.get_position()[0] - 2, self.pacman.get_position()[1]
        xc, yc = center
        xr, yr = self.red.get_position()
        target = 2 * xc - xr, 2 * yc - yr
        next_position = self.labyrinth.find_path_step(self.blue.get_position(), target,
                                                      self.blue.get_direction())
        self.blue.set_direction(find_direction(self.blue.get_position(), next_position))
        self.blue.set_position(next_position)
        self.blue.update_image()
            