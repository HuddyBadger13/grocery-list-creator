def build_grocery_list(recipes, selected_meals, individual_items):
    grocery_list = {}

    for meal_name, servings in selected_meals.items():
        if meal_name not in recipes:
            continue

        for ingredient_name, ingredient_info in recipes[meal_name].items():
            add_item(
                grocery_list,
                ingredient_name,
                ingredient_info["quantity"] * servings,
                ingredient_info["unit"],
                ingredient_info.get("category", "Other")
            )

    for item in individual_items:
        add_item(
            grocery_list,
            item["name"],
            item["quantity"],
            item["unit"],
            item["category"]
        )

    return grocery_list


def add_item(grocery_list, name, quantity, unit, category):
    if name in grocery_list and grocery_list[name]["unit"] == unit:
        grocery_list[name]["quantity"] += quantity
    else:
        grocery_list[name] = {
            "quantity": quantity,
            "unit": unit,
            "category": category
        }


def organize_by_category(grocery_list):
    category_order = [
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

    organized = {}

    for category in category_order:
        items = {
            name: info
            for name, info in grocery_list.items()
            if info["category"] == category
        }

        if items:
            organized[category] = dict(sorted(items.items()))

    return organized