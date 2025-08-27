#!/usr/bin/env python
# coding: utf-8

# In[14]:


try:
    temp = int(input("Enter the temperature(C°)"))
    if temp > 75 or temp <= -20:
        print("💀RIP")
    elif temp > 50:
        print("It is hot as fuck 🔥")
    elif temp >= 30:
        print("It is hot outside")
    elif temp < 18:
        print("It is cold Outside.")
    elif temp < 10:
        print("It is cold as fuck ❄️.")
    else:
        print ("Weather is pleasant 🙂.")
except ValueError:
    print("Enter a valid input.")

