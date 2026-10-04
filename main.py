import pygame
import sys

from asteroidfield import AsteroidField
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from circleshape import CircleShape
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0.0
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    updatable.add(AsteroidField())



    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for s in shots:
                if a.collides_with(s):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()


        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
