#!/usr/bin/env python
# coding: utf-8

# In[10]:


try:
    num_1 = float(input("Enter your first number:"))
    operator = input("Enter one of these operators(+,-,*,/):").replace(" ", "")
    num_2 = float(input("Enter your second number"))
    if operator == "+":
        result = num_1 + num_2
        print(f"{num_1:.2f} {operator} {num_2:.2f} = {result:.2f}")
    elif operator == "-":
        result = num_1 - num_2
        print(f"{num_1:.2f} {operator} {num_2:.2f} = {result:.2f}")
    elif operator == "/":
        if num_2 == 0:
            print("Denominator can't be zero")
        else:
            result = num_1 / num_2
            print(f"{num_1:.2f} {operator} {num_2:.2f} = {result:.2f}")
    elif operator == "*":
        result = num_1 * num_2
        print(f"{num_1:.2f} {operator} {num_2:.2f} = {result:.2f}")
    else:
        print(f"{operator} is not an operator")

except ValueError:
    print("Error: enter valid input")


# In[ ]:




