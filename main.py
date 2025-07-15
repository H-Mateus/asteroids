# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame

import asteroidfield
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # Create the screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create clock object and delta variable
    clock = pygame.time.Clock()
    dt = 0

    # create the player
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    # create the asteroid field
    asteroid_field = AsteroidField()

    while 1 > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="black")
        for group in drawable:
            group.draw(screen)
        for group in updatable:
            group.update(dt)

        # Check for asteroid collision with the player
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit()
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
