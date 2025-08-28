#!/usr/bin/env python
# coding: utf-8

# In[46]:


ani_name = input("Enter the animal sound:").lower().strip()
if ani_name == "":
    print("Type something...")
elif (ani_name.isalpha() == False):
    print("Animal can't be a number")
elif ani_name == "dog":
    print("Woof!")
elif ani_name == "cat":
    print("Meow!")
elif ani_name == "duck":
    print("Quack!")
elif ani_name == "cow":
    print("Moo!")
elif ani_name == "lion":
    print("Roar!")
else:
    print(f"Unknown animal '{ani_name}'")

