#!/usr/bin/env python
# coding: utf-8

# In[8]:


from math import pi 
try:
    radius = float(input("Enter the radius:"))
    height = float(input("Enter the height"))
    assert radius >= 0, "Radius can't be negative"
    assert height >= 0, "Height can't be negative"
    volume = pi*pow(radius,2)*height
    print(f"The volume of the cylinder is {volume:.2f}")
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print ("Error: Enter a valid input")

