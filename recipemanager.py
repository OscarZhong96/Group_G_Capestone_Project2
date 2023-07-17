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
