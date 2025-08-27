#!/usr/bin/env python
# coding: utf-8

# In[24]:


try:
    score = int(input("Enter your score:"))
    if score < 0 or score > 100:
        print(f"{score} is not a valid score")
    else:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"The score {score} is graded {grade}.")
except ValueError:
    print("Error: Enter valid input.")

