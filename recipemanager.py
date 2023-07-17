class recipe:
  def __init__(self, title, ingredients, instructions, cooking_time, dietary_info):
    self.title = title
    self.ingredients = ingredients
    self.instructions = instructions
    self.cooking_time = cooking_time
    self.dietary_info = dietary_info

Macaroniandcheese= recipe("Macaroni and cheese","\n50g baguette cut into small chunks \n2 tbsp butter, plus 1 tbsp melted \n350g spiral or other short pasta\n1 garlic clove, finely chopped\n1 tsp English mustard powder\n3 tbsp plain flour\n500ml whole milk\n250g vegetarian mature cheddar grated\n50g parmesan grated",
'\n1.Heat the oil in a frying pan over a low medium heat. Toss in the onion and cook for 10 mins until softened. Crush in the garlic and stir for 1 min before adding the chicken. Turn up the heat and brown the chicken all over. Spoon over the chipotle and stir to coat for 1 min. Pour in the tomatoes and bring to the boil. Season well and reduce the heat to a gentle simmer \n\n2.Cook for 5-6 mins or until the chicken is cooked through and any excess liquid has evaporated. Stir the beans through until warmed, then remove from the heat. Warm the wraps following pack instructions. \n\n3.Divide the mix between the wraps, top with the avocado and shredded lettuce, and squeeze over the lime. Roll up and cut in half before serving.',"\nPrep 10 min\nCook 40 min","\nNutrition: per serving\n\nNutrientUnit kcal: 860 \nfat:42g\nsaturates:25g\ncarbs:88g\nsugars:9g\nfibre:0g\nprotein:38g\nsalt:1.9g")

print(Macaroniandcheese.title)
print(Macaroniandcheese.ingredients)
print(Macaroniandcheese.instructions)
print(Macaroniandcheese.cooking_time)
print(Macaroniandcheese.dietary_info)

recipes = {}  # Dictionary to store recipes

def add_recipe():
    name = input("Enter recipe name: ")
    cuisine = input("Enter cuisine: ")
    ingredients = input("Enter ingredients (separated by commas): ").split(",")
    instructions = input("Enter cooking instructions: ")

    recipe = {
        "Cuisine": cuisine,
        "Ingredients": ingredients,
        "Instructions": instructions
    }

    recipes[name] = recipe
    print("Recipe added successfully!")

def view_recipe(name):
    if name in recipes:
        recipe = recipes[name]
        print(f"Name: {name}")
        print(f"Cuisine: {recipe['Cuisine']}")
        print(f"Ingredients: {', '.join(recipe['Ingredients'])}")
        print(f"Instructions: {recipe['Instructions']}")
    else:
        print("Recipe not found!")

def delete_recipe(name):
    if name in recipes:
        del recipes[name]
        print("Recipe deleted successfully!")
    else:
        print("Recipe not found!")

def main():
    while True:
        print("\n-- Recipe Management System --")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. Delete Recipe")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_recipe()
        elif choice == "2":
            name = input("Enter recipe name: ")
            view_recipe(name)
        elif choice == "3":
            name = input("Enter recipe name: ")
            delete_recipe(name)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
