from recipes import load_recipes
from grocery import build_grocery_list, display_grocery_list


def main():
    print("Welcome to the Grocery List Generator!")

    recipes = load_recipes()

    print("\nAvailable meals:")
    for meal in recipes:
        print("-", meal)

    selected_meals = {}

    while True:
        meal_choice = input("\nEnter a meal name, or type 'done' to finish: ").strip().lower()

        if meal_choice == "done":
            break

        if meal_choice not in recipes:
            print("That meal is not in the recipe list. Try again.")
            continue

        servings = int(input(f"How many servings of {meal_choice}? "))

        selected_meals[meal_choice] = servings

    grocery_list = build_grocery_list(recipes, selected_meals)
    display_grocery_list(grocery_list)


if __name__ == "__main__":
    main()