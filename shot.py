# shot.py
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        # Call the parent CircleShape constructor with the shot's radius
        super().__init__(x, y, SHOT_RADIUS)
        # The velocity will be set by the Player's shoot method upon creation

    def draw(self, screen):
        """
        Draws the shot as a small solid white circle.
        """
        # Parameters: surface, color, center (position), radius
        # No width parameter means it will be filled
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        """
        Moves the shot in a straight line based on its velocity.
        """
        self.position += self.velocity * dt