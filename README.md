# Asteroids

A version of the classic [Asteroids](<https://en.wikipedia.org/wiki/Asteroids_(video_game)>) game in Python as part of my learning

## Installation & Running

### With uv (recommended)

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Clone this repository (`git clone https://github.com/H-Mateus/asteroids.git`)
3. Run: `uv run main.py`

The only dependency is pygame (version 2.6.1), so something like the following should work, but I haven't tested it:

### With pip

1. Install pygame: `pip install pygame`
2. Clone this repository (`git clone https://github.com/H-Mateus/asteroids.git`)
3. Run: `python main.py`

## How to Play

- Use wasd keys to move your ship
- Spacebar to shoot
- Destroy asteroids to earn points
- Avoid collisions - you have 3 lives
- Small asteroids = 100 points
- Medium asteroids = 50 points
- Large asteroids = 20 points
