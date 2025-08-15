import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            # small asteroids just die
            return
        else:
            # larger asteroids should split into two asteroids, get smaller, faster, and meaner
            new_angle = random.uniform(20, 50)
            one = self.velocity.rotate(new_angle)
            two = self.velocity.rotate(-new_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            for new_asteroid in one, two:
                asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                asteroid.velocity = new_asteroid * 1.2
