from pathlib import Path

BASE = Path(__file__).parents[1]

SECRET = BASE.joinpath("secret.json")
