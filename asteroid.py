from typing import override

import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH


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
