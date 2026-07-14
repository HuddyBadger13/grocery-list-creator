import json

def load_recipes():
    with open("data/recipes.json", "r") as file:
        recipes = json.load(file)

    return recipes