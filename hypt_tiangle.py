#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
try:
    side_a = float(input("Enter length of side_A:"))
    side_b = float(input("Enter length of side_B:"))
    assert side_a >= 0, "Length can't be negative"
    assert side_b >= 0, "Length can't be negative"
    hypt = math.sqrt(pow(side_a,2) + pow(side_b,2))
    print(f"The hypotenuse of the triangle is {hypt:.2f}")
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Enter valid input")

