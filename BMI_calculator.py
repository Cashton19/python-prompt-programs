#!/usr/bin/env python
# coding: utf-8

# In[9]:


try:
    height = float(input("Enter your height(cms):"))
    assert height >= 0,"Height can't be negative."
    assert height != 0,"Height can't be Zero."
    weight = float(input("Enter your weight(kgs):"))
    assert weight >= 0,"Weight can't be negative."
    height /= 100 
    BMI = weight / (height ** 2)
    print(f"Your BMI is {BMI:.2f}")
    if BMI < 18.5:
        category = "underweight"
    elif 24.9 >= BMI >= 18.5:
        category = "normal weight"
    elif 25 <= BMI <= 29.9:
        category = "overweight"
    elif BMI >= 30:
        category = "obeese"
    print (f"You are {category}")
except AssertionError as e:
    print("Error", e)
except ValueError:
    print("Enter valid input")


# In[ ]:




