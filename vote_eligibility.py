#!/usr/bin/env python
# coding: utf-8

# In[10]:


try:
    age = int(input("Enter the Age(1-120):"))
    if not 0 < age <= 120:
        print("Please enter a valid age.")
    else:
        if 18 > age:
            print("Your are not eligible to vote.")
        else:
            print("Your are eligible to vote.")
except ValueError:
    print("Error: Enter a Valid input")

