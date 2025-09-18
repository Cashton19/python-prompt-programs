#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time

my_time = int(input("Enter time(In secs):"))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's Up")

