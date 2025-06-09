# circleshape.py
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # --- New Method for Collision Detection ---
    def collides_with(self, other_circle_shape):
        """
        Checks if this CircleShape is colliding with another CircleShape.
        Collision occurs if the distance between their centers is
        less than or equal to the sum of their radii.

        Args:
            other_circle_shape (CircleShape): The other CircleShape object to check collision against.

        Returns:
            bool: True if a collision is detected, False otherwise.
        """
        distance = self.position.distance_to(other_circle_shape.position)
        return distance <= (self.radius + other_circle_shape.radius)