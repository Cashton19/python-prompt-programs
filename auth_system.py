#!/usr/bin/env python
# coding: utf-8

# In[7]:


user_name = input("Enter username").strip().lower()
password = input("Enter password")
if user_name == "casht_19":
    if password == "password123":
        print("Login successful")
    elif password == "":
        print("Error: Enter password..")
    else:
        print("Incorrect password.")
elif user_name == "":
    print("Type something in username..")
else:
    print("User not found.")

