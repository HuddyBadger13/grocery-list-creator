def build_grocery_list(recipes, selected_meals):
    grocery_list = {}

    for meal_name, servings in selected_meals.items():
        if meal_name not in recipes:
            print(f"Warning: '{meal_name}' is not in your recipes.")
            continue

        ingredients = recipes[meal_name]

        for ingredient_name, ingredient_info in ingredients.items():
            quantity = ingredient_info["quantity"] * servings
            unit = ingredient_info["unit"]

            if ingredient_name in grocery_list:
                if grocery_list[ingredient_name]["unit"] == unit:
                    grocery_list[ingredient_name]["quantity"] += quantity
                else:
                    print(f"Warning: Unit mismatch for {ingredient_name}.")
            else:
                grocery_list[ingredient_name] = {
                    "quantity": quantity,
                    "unit": unit,
                    "category": ingredient_info.get("category", "Other")
}

    return grocery_list


def display_grocery_list(grocery_list):
    categories = {}

    for ingredient_name, ingredient_info in grocery_list.items():
        category = ingredient_info.get("category", "Other")

        if category not in categories:
            categories[category] = []

        categories[category].append((ingredient_name, ingredient_info))

    print("\nGrocery List:")
    print("=" * 30)

    for category, items in categories.items():
        print(f"\n{category}")
        print("-" * len(category))

        for ingredient_name, ingredient_info in items:
            quantity = ingredient_info["quantity"]
            unit = ingredient_info["unit"]

            print(f"- {ingredient_name}: {quantity} {unit}")