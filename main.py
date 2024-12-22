import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    AsteroidField()

    Player.containers = (updateable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updateable, drawable)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateable:
            obj.update(dt)

        pygame.Surface.fill(screen, "black")

        for fig in drawable:
            fig.draw(screen)

        for asteroid in asteroids:
            if asteroid.has_collision(player):
                sys.exit("Game Over!")

            for shot in shots:
                if asteroid.has_collision(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        delta = clock.tick(60) / 1000
        dt = delta


if __name__ == "__main__":
    main()
