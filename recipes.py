import json
from pathlib import Path

RECIPES_FILE = Path("data/recipes.json")


def load_recipes():
    with open(RECIPES_FILE, "r") as file:
        return json.load(file)


def save_recipes(recipes):
    with open(RECIPES_FILE, "w") as file:
        json.dump(recipes, file, indent=4)