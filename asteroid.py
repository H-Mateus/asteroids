import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            screen, color="white", center=(self.position), radius=self.radius, width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        spawn_angle = random.uniform(20, 50)
        random_angle1 = self.velocity.rotate(spawn_angle)
        random_angle2 = self.velocity.rotate(-spawn_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = random_angle1 * 1.2
        asteroid2.velocity = random_angle2 * 1.2
