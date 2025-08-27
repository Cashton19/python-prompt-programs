#!/usr/bin/env python
# coding: utf-8

# In[5]:


day = input("Enter the day of the week(Monday,Tuesday,etc..):").strip().replace(" ", "").lower()
if day == "":
    print("Enter something..")
elif day in ["saturday","sunday"]:
    print("It's weekend 🌞😎🏖️")
elif day in ["monday","tuesday","wednesday","thursday","friday"]:
    print("It's not weekend 😫")
else:
    print("Unknown day")

