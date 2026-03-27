import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH, PLAYERS_RADIUS
from logger import log_state
from circleshape import CircleShape
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH }")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    my_player = Player(x = SCREEN_WIDTH / 2,  y = SCREEN_HEIGHT / 2, radius = PLAYERS_RADIUS )
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill("black")
        my_player.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60))/1000


#        print(dt)

if __name__ == "__main__":
    main()
