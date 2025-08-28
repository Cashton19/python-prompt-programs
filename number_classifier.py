#!/usr/bin/env python
# coding: utf-8

# In[7]:


try:
    num = float(input("Enter the number:"))
    if num > 0:
        print(f"The number {num} is positive")
    elif num == 0:
        print(f"The number {num:.0f} is Zero")
    else:
        print(f"The number {num} is negative")
except ValueError:
    print("Enter valid input.")

