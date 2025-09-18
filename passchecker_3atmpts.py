#!/usr/bin/env python
# coding: utf-8

# In[9]:


from getpass import getpass
MAX_attempts = 3
for attempts in range(MAX_attempts):
    Password = getpass("Enter your password:")
    if Password == "Cashton":
        print("Access Granted")
        break
    attempts_left = MAX_attempts - (attempts + 1)
    if attempts_left == 0:
        print("Wrong password. No more attempts left")
    else:
        print(f"Wrong password. {attempts_left} attempts left")


