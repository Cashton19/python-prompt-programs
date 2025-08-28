#!/usr/bin/env python
# coding: utf-8

# In[20]:


try:
    age = int(input("Enter your age:"))
    assert age >= 0, "Age should not be negative"
    if 12 >= age >= 0:
        category = "Child"
    elif 19 >= age >= 13:
        category = "Teenager"
    elif 59 >= age >= 20:
        category = "Adult"
    elif 100 >= age >= 60:
        category = "Senior"
    else:
        category = None
        print("You are a vampire 🧛‍♂️")
    print(f"You are a {category}") if category != None else None
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Enter valid input.")

