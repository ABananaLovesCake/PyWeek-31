import pygame
from pygame.locals import *


class Player(object):
    def __init__(self):
        pass

    @staticmethod
    def control():
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                pass
            if event.type == MOUSEBUTTONDOWN:
                pass
