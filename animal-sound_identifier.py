#!/usr/bin/env python
# coding: utf-8

# In[8]:


animal_name = input("Enter animal name:").strip().lower()
match animal_name:
    case "dog":
        sound = "Woof!"
    case "cat":
        sound = "“Meow!" 
    case "cow":
        sound = "Moo!"
    case "duck":
        animal = "Quack!"
    case "lion":
        sound = "Roar!"
    case "":
        print("Error: Nothing is entered")
    case _:
        sound = "Unknown animal sound."
print(f"Animal:{animal_name}")
print(f"Sound: {sound}")

