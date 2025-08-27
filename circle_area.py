#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math
try:
    radius = float(input("Enter the raduis of the circle"))
    assert radius >= 0, "Radius can't be less than zero"
    area = math.pi*((radius)**2)
    print(f"The area of the circle is {area:.2f} ")
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Enter valid input")

