#!/usr/bin/env python
# coding: utf-8

# In[10]:


light = input("Enter trafic color(Red,Yellow or Green):").strip().replace(" ","").lower()
if light == "red":
       print("Stop!")
elif light == "yellow":
       print("Caution!")
elif light == "green":
       print("Go!")
elif light == "":
       print("Type something..")
else:
       print("Invalid format: Enter Red, Yellow or Green")

