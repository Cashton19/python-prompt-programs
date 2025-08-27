#!/usr/bin/env python
# coding: utf-8

# In[8]:


try:
    num = int(input("Enter your number:"))
    if num % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    print(f"The number {num} is {result}")
except ValueError:
    print("Enter a valid input.")

