import pygame
from pygame.locals import *


class Setting(object):
    def __init__(self):
        resolution = (1280, 720)
        self.resolution = resolution
        is_running = True
        self.is_running = is_running
        clock = pygame.time.Clock()
        delta_time = clock.tick(60) / 1000.0
        self.delta_time = delta_time
        get_mouse_position = pygame.mouse.get_pos()
        self.get_mouse_position = get_mouse_position
