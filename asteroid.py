# asteroid.py
import pygame
import random # New: Import the random module
# New: Import ASTEROID_MIN_RADIUS from constants
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    # --- New Method: split() ---
    def split(self):
        # 1. Immediately kill this asteroid (it's always destroyed upon hit)
        self.kill()

        # 2. If the asteroid's radius is at or below the minimum, it's a small asteroid
        #    and does not split further. Just return.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # 3. Otherwise, spawn 2 new smaller asteroids
        # Generate a random angle for the split (between 20 and 50 degrees)
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current velocity
        # The new asteroids will also move 20% faster (multiplied by 1.2)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Compute the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the first new asteroid at the current asteroid's position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        # Create the second new asteroid at the current asteroid's position
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
    # ---------------------------