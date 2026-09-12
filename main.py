import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Add groups to manage future objects
    updatable = pygame.sprite.Group()  # pyright: ignore[reportUnknownVariableType]
    drawable = pygame.sprite.Group()  # pyright: ignore[reportUnknownVariableType]
    # Add group to manage asteroids
    asteroids = pygame.sprite.Group()  # pyright: ignore[reportUnknownVariableType]
    shots = pygame.sprite.Group()  # pyright: ignore[reportUnknownVariableType]

    # Set containers for Asteroid
    Asteroid.containers = (asteroids, updatable, drawable)
    # Set containers for AsteroidField
    AsteroidField.containers = (updatable,)
    # Initialize asteroid field
    _ = AsteroidField()

    # Set containers for Player
    Player.containers = (updatable, drawable)
    # Initialize a player ship
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Set containers for Shot
    Shot.containers = (shots, updatable, drawable)

    # Clock object for setting fps
    clock = pygame.time.Clock()
    dt = 0.0

    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        _ = screen.fill("black")

        # Hook the update method in the game with group
        updatable.update(dt)

        for asteroid in asteroids:  # pyright: ignore[reportUnknownVariableType]
            # Detect collision between player ship and asteroids
            if asteroid.collides_with(player):  # pyright: ignore[reportUnknownMemberType]
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            # Detect collision between asteroid and shots
            for shot in shots:  # pyright: ignore[reportUnknownVariableType]
                if shot.collides_with(asteroid):  # pyright: ignore[reportUnknownMemberType]
                    log_event("asteroid_shot")
                    shot.kill()  # pyright: ignore[reportUnknownMemberType]
                    asteroid.split()  # pyright: ignore[reportUnknownMemberType]

        # Draw a player ship within drawable group
        # after filling the screen with black
        # but before filpping the screen
        # player.draw(screen)
        for obj in drawable:  # pyright: ignore[reportUnknownVariableType]
            obj.draw(screen)  # pyright: ignore[reportUnknownMemberType]

        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
