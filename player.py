# player.py
import pygame
from circleshape import CircleShape
# Import new constant PLAYER_SHOOT_COOLDOWN
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.0 # New: Initialize the shoot cooldown timer

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def shoot(self):
        """
        Creates a new Shot object and sets its velocity.
        Also sets the cooldown timer.
        """
        new_shot = Shot(self.position.x, self.position.y)
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = forward_vector * PLAYER_SHOOT_SPEED
        # --- New: Set the cooldown timer when shooting ---
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        # -------------------------------------------------

    # --- Updated Update Method ---
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Movement
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Shooting - Only allow shooting if the timer is not active (<= 0)
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()

        # --- New: Decrease the shoot timer every frame ---
        if self.shoot_timer > 0: # Only decrease if it's currently active
            self.shoot_timer -= dt
        # -------------------------------------------------