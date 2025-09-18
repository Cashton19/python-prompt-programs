#!/usr/bin/env python
# coding: utf-8

# In[14]:


try:
    table = int(input("Enter till which table you want to print:"))
    if table > 20:
        print("You only get till twenty (>.<)")
    else:
        for t in range(1, table + 1):     # loop over each table
            print(f"Table of {t}:")
            for x in range(1, 11):        # loop for 1–10
                print(f"{x} x {t} = {x * t}")
            print("\n")
except ValueError:
    print("Invalid input!")

