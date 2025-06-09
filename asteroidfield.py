# asteroidfield.py
import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0), # Direction vector for spawning from left edge (moving right)
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT), # Position lambda for left edge
        ],
        [
            pygame.Vector2(-1, 0), # Direction vector for spawning from right edge (moving left)
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ), # Position lambda for right edge
        ],
        [
            pygame.Vector2(0, 1), # Direction vector for spawning from top edge (moving down)
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS), # Position lambda for top edge
        ],
        [
            pygame.Vector2(0, -1), # Direction vector for spawning from bottom edge (moving up)
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ), # Position lambda for bottom edge
        ],
    ]

    def __init__(self):
        # Call the parent Sprite constructor, automatically adding to containers
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0 # Timer to control asteroid spawning rate

    def spawn(self, radius, position, velocity):
        """
        Creates a new Asteroid instance and sets its properties.
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity # Set the asteroid's velocity

    def update(self, dt):
        """
        Updates the asteroid field logic, primarily spawning new asteroids.
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0 # Reset timer

            # Spawn a new asteroid at a random edge
            edge = random.choice(self.edges) # Pick a random edge to spawn from
            speed = random.randint(40, 100) # Random speed for the asteroid
            velocity = edge[0] * speed # Calculate base velocity based on edge direction and speed
            velocity = velocity.rotate(random.randint(-30, 30)) # Add a slight random rotation to velocity
            position = edge[1](random.uniform(0, 1)) # Calculate spawn position along the chosen edge
            kind = random.randint(1, ASTEROID_KINDS) # Determine asteroid size/kind
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity) # Call spawn method