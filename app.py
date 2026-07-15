from flask import Flask, render_template, request, redirect, url_for
from recipes import load_recipes, save_recipes
from grocery import build_grocery_list, organize_by_category

app = Flask(__name__)

CATEGORIES = [
    "Produce",
    "Meat & Seafood",
    "Dairy & Eggs",
    "Bread & Bakery",
    "Frozen Foods",
    "Pantry",
    "Condiments",
    "Spices & Seasonings",
    "Beverages",
    "Supplements",
    "Other"
]


@app.route("/", methods=["GET", "POST"])
def index():
    recipes = load_recipes()
    grocery_list = None

    if request.method == "POST":
        selected_meals = {}
        individual_items = []

        for meal_name in recipes:
            servings = request.form.get(f"servings_{meal_name}")

            if servings and servings.isdigit() and int(servings) > 0:
                selected_meals[meal_name] = int(servings)

        item_names = request.form.getlist("item_name")
        item_quantities = request.form.getlist("item_quantity")
        item_units = request.form.getlist("item_unit")
        item_categories = request.form.getlist("item_category")

        for name, quantity, unit, category in zip(
            item_names,
            item_quantities,
            item_units,
            item_categories
        ):
            if name.strip() and quantity.strip():
                individual_items.append({
                    "name": name.strip().title(),
                    "quantity": float(quantity),
                    "unit": unit.strip(),
                    "category": category
                })

        grocery_list = build_grocery_list(recipes, selected_meals, individual_items)
        grocery_list = organize_by_category(grocery_list)

    return render_template(
        "index.html",
        recipes=recipes,
        categories=CATEGORIES,
        grocery_list=grocery_list
    )


@app.route("/add-meal", methods=["POST"])
def add_meal():
    recipes = load_recipes()

    meal_name = request.form.get("meal_name").strip().lower()
    ingredient_names = request.form.getlist("ingredient_name")
    ingredient_quantities = request.form.getlist("ingredient_quantity")
    ingredient_units = request.form.getlist("ingredient_unit")
    ingredient_categories = request.form.getlist("ingredient_category")

    new_recipe = {}

    for name, quantity, unit, category in zip(
        ingredient_names,
        ingredient_quantities,
        ingredient_units,
        ingredient_categories
    ):
        if name.strip() and quantity.strip():
            new_recipe[name.strip().title()] = {
                "quantity": float(quantity),
                "unit": unit.strip(),
                "category": category
            }

    if meal_name and new_recipe:
        recipes[meal_name] = new_recipe
        save_recipes(recipes)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)