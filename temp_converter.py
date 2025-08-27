#!/usr/bin/env python
# coding: utf-8

# In[10]:


try:
    temp = float(input("Enter the the temperature:"))
    unit = input("Enter unit of temperature(Celsius (C) or Fahrenheit (F)):").strip().upper()
    if unit == "C":
        temp = ((9/5)*temp)+32
        print(f"The temperature is {temp:.2f}°F.")
    elif unit == "F":
        temp = ((temp - 32)*5)/9
        print(f"The temperature is {temp:.2f}°C.")
    else:
        print(f"{unit} is not valid")
except ValueError:
    print("Enter only valid numeric values")


# In[ ]:




