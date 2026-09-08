from typing import override

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]  # pyright: ignore[reportMissingTypeArgument]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)  # pyright: ignore[reportUnannotatedClassAttribute]
        self.radius = radius  # pyright: ignore[reportUnannotatedClassAttribute]

    def draw(self, screen: pygame.Surface) -> None:  # pyright: ignore[reportUnusedParameter]
        # must override
        pass

    @override
    def update(self, dt: float) -> None:
        # must override
        pass
