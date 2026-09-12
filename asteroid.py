from random import uniform
from typing import override

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    # Draw the asteroid
    @override
    def draw(self, screen: pygame.Surface) -> None:
        _ = pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH,
        )

    # Make the asteroids moving
    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt  # pyright: ignore[reportUnannotatedClassAttribute]

    # Split the asteroids
    def split(self) -> None:
        # When the osteroid is collided with a shot
        self.kill()
        # Kill asteroid less than or equal the minimum size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = uniform(20, 50)
        # Define the new asteroids' vector
        first_vector = self.velocity.rotate(angle)
        second_vector = self.velocity.rotate(-angle)
        # Spawn the new ones depending on its size plus faster movement
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = first_vector * 1.2
        second_asteroid.velocity = second_vector * 1.2


