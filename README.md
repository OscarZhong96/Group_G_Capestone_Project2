# Group_G_Capestone_Project2
Online recipe management system

1. Classes: There are two classes defined in the code:

   a. `Recipe` class:
      - Purpose: This class represents a recipe and holds its information, such as title, ingredients, cooking time, dietary information, and instructions.
      - Constructor (`__init__`): The constructor initializes the attributes of a recipe object when it is created. It takes five parameters: `title`, `ingredients`, `cooking_time`, `dietary_info`, and `instructions`.

   b. `RecipeManager` class:
      - Purpose: This class manages the collection of recipes and handles operations like saving, loading, adding, deleting, and updating recipes.
      - Constructor (`__init__`): The constructor initializes the RecipeManager object. It loads data from the "recipes.json" file (if available) into the `self.datas` list.

2. Data Persistence: The `RecipeManager` class uses JSON to persist the recipe data between different sessions. The recipes are saved as a list of dictionaries in the "recipes.json" file, where each dictionary represents a recipe and contains the necessary attributes. The `json.dump()` method is used to write the data into the file, and `json.load()` is used to read the data back into the program.

3. GUI Setup:
   - The code uses Tkinter to create a simple graphical user interface (GUI).
   - The main window is created using `tk.Tk()`.
   - Three frames (`recipes_frame`, `listofrecipes_frame`, and `buttons_frame`) are created to organize the different sections of the application: recipe input, list of recipes, and recipe editor.

4. GUI Elements:
   - Labels: `tk.Label` widgets are used to display labels for each input field, such as "Title," "Cooking Time," "Dietary Information," etc.
   - Entry Widgets: `tk.Entry` widgets are used for the "Title," "Cooking Time," "Dietary Information," and "Ingredients" input fields.
   - Text Widget: `tk.Text` widget is used to allow multiline input for the "Instructions" field.
   - Listbox: `tk.Listbox` widget is used to display the list of recipes. Users can select a recipe from the list to view, delete, or edit it.
   - Scrollbar: A `tk.Scrollbar` widget is used to enable scrolling for the listbox.

5. Event Handlers (Functions):
   - `add_recipes()`: This function is called when the "Add a recipe" button is clicked. It collects the user's input from the entry and text widgets and creates a new `Recipe` object. The new recipe is then added to the `RecipeManager` using the `add_recipe()` method, which updates the list of recipes in the listbox and saves the data to the "recipes.json" file.
   - `view_recipes()`: This function is called when the "View a recipe" button is clicked. It retrieves the index of the selected recipe from the listbox and uses the `view_recipe()` method of the `RecipeManager` to display the details of the selected recipe in the entry and text widgets.
   - `delete_recipes()`: This function is called when the "Delete a recipe" button is clicked. It retrieves the index of the selected recipe from the listbox and uses the `delete_recipe()` method of the `RecipeManager` to remove the selected recipe from the list of recipes and update the listbox and "recipes.json" file.
   - `reset()`: This function is called when the "Edit a recipe" button is clicked. It retrieves the index of the selected recipe from the listbox and updates the recipe details with the values from the entry and text widgets. The updated recipe is then saved to the `RecipeManager`, and the listbox and "recipes.json" file are updated.

6. Manager and Window:
   - An instance of the `RecipeManager` class (`manager`) is created to manage the collection of recipes.
   - The `update_recipe()` method of the `manager` is called initially to populate the list of recipes in the listbox.
   - The `window.mainloop()` method starts the main event loop, which listens for user interactions and keeps the GUI responsive.
