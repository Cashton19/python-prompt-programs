#!/usr/bin/env python
# coding: utf-8

# In[40]:


try:
    year = int(input("Enter your year:"))
    assert str(year).find("-") == (-1),"Year can't be negative"
    assert len(str(year)) <= 4, "Year should not be greater than 4 digits"
    assert len(str(year)) >= 4, "Year should not be lesser than 4 digits"
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} is not a leap year")
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Invalid input.")

