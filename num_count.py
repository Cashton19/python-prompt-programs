#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from time import sleep
print("Number from Zero to four:")
sleep(1)
for x in range(0,5):
    print(f"Number = {x}")
sleep(1)
print("Number from one to five:")
y = 1
while y <= 5:
    print(f"Number = {y}")
    y += 1
sleep(1)
print("Even numbers from 2 to 10")
for z in range(2,11,2):
    print(f"Number = {z}")
sleep(1)
print("Odd numbers from 1 to 20")
for a in range(1,20,2):
    print(a , end = ", ") if a != 19 else print(a, end = ".")
sleep(1)
print("\nNumbers from 41 to 50 in descending order")
for a in range(50,40,-1):
    print(f"Number = {a}")

