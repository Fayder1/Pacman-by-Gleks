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
