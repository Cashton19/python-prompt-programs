#!/usr/bin/env python
# coding: utf-8

# In[4]:


try:
    weight = float(input("Please enter your weight:"))
    unit = input("Kilograms or Pounds?? (K or L)").strip().lower()
    if unit == "k":
        weight *= 2.20462 
        print(f"Your weight is {weight:.2f} lbs.")
    elif unit == "l":
        weight /= 2.20462
        print(f"Your weight is {round(weight,2)} kgs.")
    else:
        print(f"Error:{unit} is not valid.")
except ValueError:
    print("Error: Please enter valid numeric input.")


# In[ ]:




