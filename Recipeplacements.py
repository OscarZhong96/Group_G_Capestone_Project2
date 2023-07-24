import tkinter
from tkinter import *
from tkinter import ttk
window=tkinter.Tk()

datas = []
  
# Add Recipe
def add_recipes():
    global datas
    datas.append([title.get(),ingredients.get(),cookingtime_entry.get(),dietaryinfo_entry.get(),instructions_entry.get(1.0, "end-1c")])
    update_recipe()
  
# View Recipe
def view_recipes():
    title.set(datas[int(choice_listbox.curselection()[0])][0])
    ingredients.set(datas[int(choice_listbox.curselection()[0])][1])
    cookingtime.set(datas[int(choice_listbox.curselection()[0])][2])
    dietaryinfo.set(datas[int(choice_listbox.curselection()[0])][3])
    instructions_entry.delete(1.0,"end")
    instructions_entry.insert(1.0, datas[int(choice_listbox.curselection()[0])][4])
  
# Delete Recipe
def delete_recipes():
    del datas[int(choice_listbox.curselection()[0])]
    update_recipe()
  
def reset():
    title.set('')
    ingredients.set('')
    instructions_entry.delete(1.0,"end")
  
# Update recipe
def update_recipe():
    choice_listbox.delete(0,END)
    for n,p,a,g,e, in datas:
        choice_listbox.insert(END, n)

title=StringVar()
cookingtime=StringVar()
ingredients=StringVar()
dietaryinfo=StringVar()
ingredients=StringVar()



#naming the window recipe manager
window.title("Recipe Manager")
# creates a frame within the window
frame=tkinter.Frame(window)
frame.pack()
# creating a frame and separating it out by the grid system going for a
recipes_frame=tkinter.LabelFrame(frame,text="Recipes")
recipes_frame.grid(row=0,column=0, padx=20, pady=20, sticky="news")

# doesnt show anything on tkinter until you pair it with a label also need to pack and place it
# Created label named title
title_label=tkinter.Label(recipes_frame, text="Title")
title_label.grid(row=0,column=0)

cookingtime_label=tkinter.Label(recipes_frame, text="Cooking Time")
cookingtime_label.grid(row=1,column=0)

dietaryinfo_label=tkinter.Label(recipes_frame,text="Dietary information")
dietaryinfo_label.grid(row=2,column=0)

ingredients_label=tkinter.Label(recipes_frame,text="Ingredients")
ingredients_label.grid(row=3,column=0)

instructions_label=tkinter.Label(recipes_frame,text="Instructions")
instructions_label.grid(row=4,column=0)


title_entry=tkinter.Entry(recipes_frame,textvariable = title)
cookingtime_entry=tkinter.Entry(recipes_frame,textvariable=cookingtime)
dietaryinfo_entry=tkinter.Entry(recipes_frame,textvariable=dietaryinfo)
ingredients_entry=tkinter.Entry(recipes_frame,textvariable = ingredients)
instructions_entry=tkinter.Text(recipes_frame,width=20,height=10)

title_entry.grid(row=0,column=1)
cookingtime_entry.grid(row=1,column=1)
dietaryinfo_entry.grid(row=2,column=1)
ingredients_entry.grid(row=3,column=1)
instructions_entry.grid(row=4,column=1)

# so new sperate frame for listbox frame for list of recipes
listofrecipes_frame=tkinter.LabelFrame(frame,text="List of Recipes")
listofrecipes_frame.grid(row=0,column=2,padx=20,pady=20, sticky="news")
# sticky makes it consistent
choice_label=tkinter.Label(listofrecipes_frame, text= "Choose your recipe")

# listbox and scrollbar#
choice_listbox=tkinter.Listbox(listofrecipes_frame,height=20)
scrollbar=tkinter.Scrollbar(listofrecipes_frame)

# Placement of label,listbox and scrollbar
choice_label.grid(row=1,column=2)
choice_listbox.grid(row=2,column=2)
scrollbar.grid(row=2,column=3)

choice_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=choice_listbox.yview)

# adding buttons frame
buttons_frame=tkinter.LabelFrame(frame,text="Recipe Editor")
buttons_frame.grid(row=0,column=4,padx=20,pady=20, sticky="news")
# add buttons
viewbutton=tkinter.Button(buttons_frame,text="View a recipe",font="arial 12 bold",command=view_recipes)
addbutton=tkinter.Button(buttons_frame, text="Add a recipe",font="arial 12 bold",command=add_recipes)
deletebutton=tkinter.Button(buttons_frame, text="Delete a recipe",font="arial 12 bold",command=delete_recipes)
editbutton=tkinter.Button(buttons_frame,text="Edit a recipe",font="arial 12 bold",command=reset)

# button placement
viewbutton.grid(row=1, column=4)
addbutton.grid(row=2, column=4)
deletebutton.grid(row=3, column=4)
editbutton.grid(row=4, column=4)
window.mainloop()
