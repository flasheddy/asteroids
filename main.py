import pygame

from logger import log_state

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize a player ship
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    spaceship = Player(x, y)

    # Clock object for setting fps
    clock = pygame.time.Clock()
    dt = 0.0

    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # Hook the update method in the game
        spaceship.update(dt)

        # Draw a player ship after filling the screen with black
        # but before filpping the screen
        spaceship.draw(screen)

        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
