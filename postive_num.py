#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Write a program to keep asking for user input until they enter a positive number.
while True:
    try:
        num_count = 0
        while num_count <= 0:
            num_count = float(input("Enter a positive number:"))
            if num_count == 0:
                print("Number can't be zero")
            elif num_count < 0:
                print(f"{num_count} is not a positive number")
        print(f"{num_count} is a positive number")
        break
    except ValueError:
        print("Enter valid input!")

