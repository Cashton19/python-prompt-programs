#!/usr/bin/env python
# coding: utf-8

# In[13]:


try:
    age = int(input("Enter your age:"))
    salary = float(input("Enter your salary:"))
    assert age <= 120, "Age should less than 120."
    assert age >= 0, "Age can't be negative."
    if age >= 18 and salary >= 30000:
        print("You are eligible for loan.")
    else:
        print("You are not eligible for loan.")
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Enter valid input")

