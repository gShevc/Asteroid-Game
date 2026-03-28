import pygame
import sys
from logger import log_event
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH, PLAYERS_RADIUS
from logger import log_state
from circleshape import CircleShape
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH }")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots  = pygame.sprite.Group()




    Player.containers = (updatable, drawable)
    Asteroid.containers = ( asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    Shot.containers = (shots , updatable, drawable)

    my_player = Player(x = SCREEN_WIDTH / 2,  y = SCREEN_HEIGHT / 2, radius = PLAYERS_RADIUS )
    my_asteroid_field = AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60))/1000
        updatable.update(dt)

        for Asteroids_check in asteroids:
            if(Asteroids_check.collides_with(my_player)):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        for Asteroid_shot_check in asteroids:
            for shot in shots:
                if(Asteroid_shot_check.collides_with(shot)):
                    log_event("asteroid_shot")
                    Asteroid_shot_check.split()
                    shot.kill()
                    


if __name__ == "__main__":
    main()
