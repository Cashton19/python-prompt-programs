#!/usr/bin/env python
# coding: utf-8

# In[3]:


try:
    num = int(input("Enter your Integer:"))
    factorial = 1
    for x in range(1, num + 1):
        factorial *= x 
    print(f"Factorial of {num} is {factorial}")
except ValueError:
    print("Invalid input!")

