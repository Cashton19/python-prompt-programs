#!/usr/bin/env python
# coding: utf-8

# In[6]:


try:
    height = float(input("Enter the height of the triangle:"))
    base = float(input("Enter the base of the triangle:"))
    assert height >= 0, "Height can't be negative"
    assert base >= 0, "Base can't be negavtive"
    area = (1/2)*height*base
    print(f"The area of the triangle is {area:.2f}")
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Enter only numeric values")

