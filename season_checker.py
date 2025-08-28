#!/usr/bin/env python
# coding: utf-8

# In[13]:


try:
    month = int(input("Enter month number(1-12):"))
    assert 12 >= month > 0, "Out of range"
    if month in [12,1,2]:
        print("It's winter.")
    elif month in [3,4,5]:
        print("It's Spring.")
    elif month in [6,7,8]:
        print("It's Summer.")
    else:
        print("It's fall.")
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Enter valid input.")

