# Asteroids

An arcade-style Asteroids clone written in Python with [pygame](https://www.pygame.org/),
built as a guided project on [Boot.dev](https://boot.dev).

Fly a triangular ship around a 1280×720 window, shoot drifting asteroids, and try not to
get hit. When an asteroid is shot it splits into two smaller, faster ones, so the field
gets more crowded the longer you survive. A single collision with an asteroid ends the run.

## Features

- Rotating, thrusting player ship confined to the window (no wrap-around)
- Rate-limited shooting (0.3 s cooldown)
- Asteroids spawned from random screen edges with random size (20–60 px) and speed
- Asteroids split into two smaller, faster asteroids until they reach the minimum size
- Circle-based collision detection between ship, asteroids, and shots
- Optional JSONL telemetry for game state and events

## Requirements

- Python 3.13 or newer
- pygame 2.6.1 (pinned in `pyproject.toml` / `uv.lock`)
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Run it

With uv (handles the virtualenv and dependencies for you):

```sh
uv run main.py
```

Without uv:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install "pygame==2.6.1"
python main.py
```

Close the game window (or Ctrl+C in the terminal) to quit.

## Controls

| Key | Action |
| --- | --- |
| `W` | Thrust forward |
| `S` | Thrust backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Fire a shot (0.3 s cooldown) |

## Logging

The game writes two JSON Lines files next to the code (both git-ignored and
overwritten on each run):

- `game_state.jsonl` — a snapshot roughly once per second for the first 16 seconds
  (screen size, sprite counts, sampled positions/velocities/radii)
- `game_events.jsonl` — discrete events: `player_hit`, `asteroid_shot`, `asteroid_split`

## Project layout

| File | Purpose |
| --- | --- |
| `main.py` | Game loop: input, updates, collisions, drawing, 60 FPS clock |
| `constants.py` | All tunable values (window size, speeds, radii, spawn rate) |
| `circleshape.py` | Base sprite: position, velocity, radius, circle collision |
| `player.py` | Ship rendering, rotation, movement, shooting |
| `shot.py` | Projectile sprite |
| `asteroid.py` | Asteroid sprite, drawing, and splitting logic |
| `asteroidfield.py` | Timed spawning of asteroids from the screen edges |
| `logger.py` | JSONL state/event logging used by the game loop |

## Tuning

Game feel is controlled entirely by `constants.py` — window size, ship radius and speed,
turn rate, shot speed/cooldown/radius, asteroid sizes, spawn rate, and how many asteroid
kinds exist.

## Notes

This is a learning project, so there is no test suite or packaging step yet;
verification is simply running the game and playing it.
