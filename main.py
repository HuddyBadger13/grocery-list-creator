from recipes import load_recipes
from grocery import build_grocery_list, display_grocery_list


def main():
    print("Welcome to the Grocery List Creator!")

    recipes = load_recipes()
    meal_names = list(recipes.keys())

    print("\nAvailable meals:")
    for index, meal in enumerate(meal_names, start=1):
        print(f"{index}. {meal.title()}")

    selected_meals = {}

    while True:
        choice = input("\nEnter meal number, or type 'done' to finish: ").strip().lower()

        if choice == "done":
            break

        if not choice.isdigit():
            print("Please enter a number from the list.")
            continue

        choice_number = int(choice)

        if choice_number < 1 or choice_number > len(meal_names):
            print("That number is not on the list. Try again.")
            continue

        meal_name = meal_names[choice_number - 1]

        servings_input = input(f"How many servings of {meal_name.title()}? ").strip()

        if not servings_input.isdigit():
            print("Please enter a whole number for servings.")
            continue

        servings = int(servings_input)

        if meal_name in selected_meals:
            selected_meals[meal_name] += servings
        else:
            selected_meals[meal_name] = servings

    grocery_list = build_grocery_list(recipes, selected_meals)
    display_grocery_list(grocery_list)


if __name__ == "__main__":
    main()