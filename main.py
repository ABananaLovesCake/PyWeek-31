from settings import *
from player_controls import *

pygame.init()
screen = pygame.display.set_mode(
    size=Setting().resolution
)
while Setting().is_running:
    Player.control()
    pygame.display.update()


if __name__ == '__main__':
    pass
