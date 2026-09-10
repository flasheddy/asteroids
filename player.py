from typing import override

import pygame

from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # pyright: ignore[reportUnannotatedClassAttribute]
        self.shot_cooldown_timer = 0.0  # pyright: ignore[reportUnannotatedClassAttribute]

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Draw the player ship
    @override
    def draw(self, screen: pygame.Surface) -> None:
        points = self.triangle()
        _ = pygame.draw.polygon(
            screen,
            "white",
            points,
            LINE_WIDTH,
        )

    # Rotate the player ship
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    # Move the player ship
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector  # pyright: ignore[reportUnannotatedClassAttribute]

    # Make shooting
    def shoot(self) -> None:
        # Rate limit
        if self.shot_cooldown_timer > 0:
            return
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        


    # Bind keys with rotation and movement
    @override
    def update(self, dt: float) -> None:
        # Rate limit
        self.shot_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        # Rotation keys
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Movement keys
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Shooting keys
        if keys[pygame.K_SPACE]:
            self.shoot()
