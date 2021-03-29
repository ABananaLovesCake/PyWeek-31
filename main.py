from settings import *
from player_controls import *

pygame.init()
screen = pygame.display.set_mode(
    size=Setting().resolution
)
while Setting().is_running:
    Player.control()
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
    pygame.display.update()


if __name__ == '__main__':
    pass
