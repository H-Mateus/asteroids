import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Create the screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize font for score display
    font = pygame.font.Font(None, 36)
    score = 0

    # Add live counter
    lives = 3

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
                lives -= 1
                if lives > 0:
                    # Reset player position
                    player.position = pygame.Vector2(
                        SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
                    )

                    # Clear all asteroids
                    for asteroid in asteroids:
                        asteroid.kill()

                    # Recreate asteroid field
                    asteroid_field = AsteroidField()
                else:
                    print("Game over!")
                    print(f"Score: {score}")
                    sys.exit()

            for shot in shots:
                if asteroid.collisions(shot):
                    # Add score based on size
                    if asteroid.radius == ASTEROID_MIN_RADIUS:  # Small asteroid (20)
                        score += 100
                    elif (
                        asteroid.radius == ASTEROID_MIN_RADIUS * 2
                    ):  # Medium asteroid (40)
                        score += 50
                    elif (
                        asteroid.radius == ASTEROID_MIN_RADIUS * 3
                    ):  # Large asteroid (60)
                        score += 20
                    else:
                        score += 50  # Fallback for unexpected sizes

                    asteroid.split()
                    shot.kill()

        # Render and display the score
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))
        lives_text = font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_text, (10, 40))

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
